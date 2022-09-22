import requests
import json
import time

def get_mockup(varaint_ID,image_URL,placement,headers,nft):

    url = "https://api.printful.com/mockup-generator/create-task/71"

    mockup_url = ""

    if nft == "Goblintown":
        width = 1800
        height = 1800
        top = 300
        left = 0
    elif nft == "Mutant Ape" or nft == "Bored Ape":
        width = 1400
        height = 1400
        top = 500
        left = 200

    body = {
            "variant_ids": [
                varaint_ID
            ],
            "format": "jpg",
            "files": [
                {
                "placement": placement,
                "image_url": image_URL,
                "position": {
                "area_width": 1800,
                "area_height": 2400,
                "width": width,
                "height": height,
                "top": top,
                "left": left
                }
                }
            ]
            }
    # time.sleep(2)
    res = requests.post(url, headers= headers, data= json.dumps(body)).json()
    # print(res)
    task_key = res["result"]["task_key"]
    # print(task_key)
    
    time.sleep(5)

    status = 'pending'
    
    while status=='pending':
        res_mockup = requests.get("https://api.printful.com/mockup-generator/task?task_key=" + task_key, headers=headers).json()
        # print(res_mockup)
        status = res_mockup['result']['status']
        print("Pending..........")
        time.sleep(3)
    
    mockup_url = res_mockup['result']['mockups'][0]['mockup_url']
    print("Mockup Completed !!")

    return mockup_url

