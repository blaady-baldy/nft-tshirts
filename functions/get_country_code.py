from dotenv import load_dotenv
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_country_code(country):
    headers = {
        'Accept': 'application/json',
    }

    params = {
        'value': country,
        'app_id': os.getenv('COUNTRY_CODE_API_ID'),
        'app_key': os.getenv('COUNTRY_CODE_API_KEY'),
    }
    response = requests.get('https://api-2445580194301.production.gw.apicast.io/1.0/region/country/code.php', params=params, headers=headers).json()

    return response['ISO ALPHA-2']