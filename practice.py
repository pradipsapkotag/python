import json

def question3():
    f= open('products.json','r')
    data = json.loads(f.read())
    f.close()
    nd = {
            "id": 31,
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
    # with open ('products.json','w') as e:
    #         e.write(json.dumps(data))
    returun  (f"<p>{"status":"success"}</p><pre>{json.dumps(data['products'][-1],indent=4)}</pre>")
question3()

# original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
# it1 = {k:v for k,v in original_dict.items() if  k=='john'}
# it2 = {k:v for k,v in original_dict.items() if k=='jack'}
# print(json.dumps(original_dict,indent=4))
# print(json.dumps(it1.update(it2),indent=4))