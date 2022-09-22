from functions.get_image.bored_ape_yatch import get_bored_ape_image_url
from functions.get_image.goblintown import get_goblin_image_url
from functions.get_image.mutant_ape_yatch import get_mutant_ape_image_url

def get_item_url(nft, token_ID):

    if nft == "Goblintown":
        item_url = get_goblin_image_url(token_ID)
    elif nft == "Mutant Ape":
        item_url = get_mutant_ape_image_url(token_ID)
    elif nft == "Bored Ape":
        item_url = get_bored_ape_image_url(token_ID)

    return item_url
    