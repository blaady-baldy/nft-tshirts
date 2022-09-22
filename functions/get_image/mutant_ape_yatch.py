import requests

def get_mutant_ape_image_url(token):
    # token = int(input())

    url = "https://boredapeyachtclub.com/api/mutants/" +str(token)

    res = requests.get(url).json()
    image = res["image"][7:]
    # print(image)

    image_url = "https://ipfs.io/ipfs/"+image
    return image_url
