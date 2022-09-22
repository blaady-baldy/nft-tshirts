from itertools import product
import requests
import json
from requests.structures import CaseInsensitiveDict
import os
from dotenv import load_dotenv

from functions.product_data import variant_id
from functions.item_url import get_item_url
from functions.mockup import get_mockup
from functions.place_order import place_order

load_dotenv()

store_url = "https://api.printful.com/store/products"

headers = CaseInsensitiveDict()

#                           TAKING DATA FROM THE USER

def process(nft, token_ID, color, size,placement,choice, recipient):

    ###                        DATA SEGMENT

    item_url = get_item_url(nft, token_ID)
    variant_ID = variant_id(color,size)
    headers["Authorization"] = os.getenv("printful_api_key")

    mockup_url = get_mockup(variant_ID,item_url,placement,headers,nft)
    success=[]
    success.append(mockup_url)

    if choice=="Get Mockup":
        return success
    
    body = {
        "sync_product": {
            "name": nft + " T-shirt : #" + str(token_ID),
            "thumbnail": item_url
        },
        "sync_variants": [
            {
                "retail_price": "14.00",
                "variant_id": variant_ID,
                "files": [
                    {
                        "type": placement,
                        "url": item_url,
                        "position": {
                        "area_width": 1800,
                        "area_height": 2400,
                        "width": 1600,
                        "height": 1600,
                        "top": 400,
                        "left": 100
                        }
                    }
                ]
            }
        ]
        }

    #                                   SENDING POST REQUEST TO PRINTFUL
    response = requests.post(store_url, headers= headers, data= json.dumps(body)).json()
    # success.append(output(response, variant_ID, headers))
    product_ID = str(response["result"]["id"])
    print("Product Completed !!! ")
    order_ID = place_order(product_ID, variant_ID, headers, recipient)
    success.append(order_ID)
    print("Order id = " + order_ID)
    return success
