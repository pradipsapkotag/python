from distutils.log import debug
from flask import Flask
import json

app = Flask(__name__)

@app.route('/Q1', methods = ['GET'])
def question1():
    with open ('products.json','r') as f:
            data = json.loads(f.read())
    # f= open('products.json','r')
    # data = json.loads(f.read())
    # f.close()
    maximumprice = 0
    maximumrating = 0

    for item in data['products']:
        if(maximumprice<item['price']):
            maximumprice= item['price']
            item1 = item
        if(maximumrating<item['rating']):
            maximumrating=item['rating']
            item2 = item

    return f'<pre>{json.dumps(item1,indent=4)}</pre> <pre>{json.dumps(item2,indent=4)}</pre>' 



@app.route('/Q2/<int:ide>',methods = ['GET', 'POST'])
def question2(ide):
    with open ('products.json','r') as f:
            data = json.loads(f.read())
    # f= open('products.json','r')
    # data = json.loads(f.read())
    # f.close()
    try:
        for i in range(len(data['products'])):
            try:
                if(data['products'][i]['id']==ide):
                    item1 = data['products'][i]
                    del data['products'][i]
            except:
                pass
        with open ('products.json','w') as e:
            e.write(json.dumps(data))
        status = {'status':'success'}
        return f'<pre>{json.dumps(status,indent=4)}</pre><pre>{json.dumps(item1,indent=4)}</pre>'
    except:
        return '<p>Item not found</p>'



@app.route('/Q4', methods = ['GET', 'POST'])
def question4():
    with open ('products.json','r') as f:
            data = json.loads(f.read())
    # f= open('products.json','r')
    # data = json.loads(f.read())
    # f.close()
    for item in data['products']:
        if(item['category']=='smartphones'):
            item['category']='Smartphones'
            # print(json.dumps(item,indent = 4))
    with open ('products.json','w') as e:
            e.write(json.dumps(data))
    return '<p>{"status":"success"}</p>'



@app.route('/Q3', methods = ['GET', 'POST'])
def question3():
    with open ('products.json','r') as f:
            data = json.loads(f.read())
    # f= open('products.json','r')
    # data = json.loads(f.read())
    # f.close()
    nd = {
            "id": data['products'][-1]['id']+1,
            "title": "iPhone 9",
            "description": "An apple mobile which is nothing like apple",
            "price": 549,
            "discountPercentage": 12.96,
            "rating": 4.69,
            "stock": 94,
            "brand": "Apple",
            "category": "Smartphones",
            "thumbnail": "https://dummyjson.com/image/i/products/1/thumbnail.jpg",
            "images": [
                "https://dummyjson.com/image/i/products/1/1.jpg",
                "https://dummyjson.com/image/i/products/1/2.jpg",
                "https://dummyjson.com/image/i/products/1/3.jpg",
                "https://dummyjson.com/image/i/products/1/4.jpg",
                "https://dummyjson.com/image/i/products/1/thumbnail.jpg"
            ]
        }
    data['products'].append(nd)
    with open ('products.json','w') as e:
            e.write(json.dumps(data))
    status = {'status':'success'}
    return (f"<pre>{json.dumps(status,indent=4)}<pre><pre>{json.dumps(data['products'][-1],indent=4)}</pre>")






@app.route('/Q5', methods = ['GET'])
def question5():
    with open ('products.json','r') as f:
            data = json.loads(f.read())
    # f= open('products.json','r')
    # data = json.loads(f.read())
    # f.close()
    it=[]
    for item in data['products']:
        if(item['rating']>4 and item['discountPercentage']>10):
            it.append({k:v for k,v in item.items() if k == 'title' or k=='description' or k=='brand' or k=='price'})
            # print(json.dumps(it,indent = 4))
    return f'<pre>{json.dumps(it,indent=4)}</pre>'



app.run(debug=True)