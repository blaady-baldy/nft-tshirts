import requests

def get_bored_ape_image_url(token):
    # token = int(input())

    url = "https://ipfs.io/ipfs/QmeSjSinHpPnmXmspMjwiXyN6zS4E9zccariGR3jxcaWtq/" +str(token)

    res = requests.get(url).json()
    image = res["image"][7:]
    # print(image)

    image_url = "https://ipfs.io/ipfs/"+image
    return image_url