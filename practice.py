import json
from random import randint
def adduser():
    f= open('users.json','r')
    data = json.loads(f.read())
    f.close()
    nd = {
        "id": data[-1]['id']+1,
        "name": data[randint(0,len(data)-1)]['name'],
        "username": data[randint(0,len(data)-1)]['username'],
        "email": data[randint(0,len(data)-1)]['email'],
        "address": data[randint(0,len(data)-1)]['address'],
        "phone": data[randint(0,len(data)-1)]['phone'],
        "website": data[randint(0,len(data)-1)]['website'],
        "company": data[randint(0,len(data)-1)]['company']
    }
    data.append(nd)
    with open ('products.json','w') as e:
            e.write(json.dumps(data))
    status = {'status':'success','message': 'User added'}
    return f'<pre>{json.dumps(status,indent=4)}</pre><pre>{json.dumps(nd,indent=4)}</pre>'


adduser()