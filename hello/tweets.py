import requests 
import pandas as pd 
twitter_data = []
payload = {

    api_key: '33970ae47d7781b19485ab4a9f4502a8',
    query: 'covid-19 vaccine',
    num: '25'
} 

response = requests.get(
    'https://api.scrapper.com/structured/twitter/search', params = payload
)
data = response.json()