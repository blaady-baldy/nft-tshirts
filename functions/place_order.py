from time import sleep
import requests
import json
import time

def place_order(id, variant_ID, headers, recipient):

    product_data = requests.get("https://api.printful.com/store/products/" + str(id), headers=headers).json()
    current_time = str(round(time.time()))

    sleep(1)

    product = product_data['result']['sync_variants'][0]['product']
    files = product_data['result']['sync_variants'][0]['files']
    options = product_data['result']['sync_variants'][0]['options']
    
    body = {
    "external_id": current_time,
        "shipping": "STANDARD",
        "recipient": recipient,
        "items": [
                {
                "id": id,
                "variant_id": variant_ID,
                "sync_variant_id": product_data['result']['sync_variants'][0]['id'],
                "external_variant_id": product_data['result']['sync_variants'][0]['external_id'],
                "quantity": 1,
                "price": "14.00",
                "retail_price": "14.00",
                "name": product_data['result']['sync_product']['name'],
                "product": product,
                "files": files,
                "options": options 
                }
            ],
            
        #This WILL BE DEPLAYED ON PACKING SLIP 
    "retail_costs": {
        "currency": "USD",
        "subtotal": "14.00",
        "discount": "0.00",
        "shipping": "14.00",
        "total": "28.00"
    },
    "gift": {
        "subject": "To Devansh",
        "message": "Have a nice day"
    }
    }

    res = requests.post(url="https://api.printful.com/orders", headers=headers, data=json.dumps(body)).json()
    print("*"*50)
    print("Order Placed")
    return str(res['result']['id'])