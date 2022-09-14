import json
import requests


url = "https://jsonplaceholder.typicode.com/users"
data = requests.get(url)

with open ('users.json','w') as e:
            e.write(json.dumps(data.json(),indent=4))