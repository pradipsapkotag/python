from distutils.log import debug
from flask import Flask

from random import randint
import json

app = Flask(__name__)

# this will show all details
@app.route('/showall', methods = ['GET'])
def showall():
    f= open('users.json','r')
    data = json.loads(f.read())
    
    return f"<pre>{json.dumps(data,indent = 4)}</pre>" 


# this will delete based on given id
@app.route('/delete/<int:ide>',methods = ['GET', 'POST'])
def delete(ide):
    f= open('users.json','r')
    data = json.loads(f.read())
    f.close()
    status = {'status':'failed','message':'User not deleted'}
    try:
        for i in range(len(data)):
            try:
                if(data[i]['id']==ide):
                    item = data[i]
                    status['status'] = 'Success'
                    status['message']='User deleted'
                    del data[i]
            except:
                pass
        with open ('users.json','w') as e:
            e.write(json.dumps(data))
        return f'<pre>{json.dumps(status,indent=4)}</pre><pre>{json.dumps(item,indent=4)}</pre>'
    except :
        return f'<pre>{json.dumps(status,indent=4)}</pre>'
    
    
    
# this will update users.json

@app.route('/adduser', methods = ['GET', 'POST'])
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
    with open ('users.json','w') as e:
            e.write(json.dumps(data))
    status = {'status':'success','message': 'User added'}
    return f'<pre>{json.dumps(status,indent=4)}</pre><pre>{json.dumps(nd,indent=4)}</pre>'









app.run(debug=True)