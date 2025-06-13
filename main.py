import requests
from time import sleep
import pandas as pd

api_key = "RGAPI-fa24e926-c2b0-4acc-8469-2ada76834b6b"
server_account = 'AMERICAS'
server_summoner = 'la2'
tag_line = "tuma"
game_name = "BIUTIFUL KING"

endpoint_account = f"https://{server_account}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}?api_key={api_key}"

user_dic = requests.get(endpoint_account).json()
print(user_dic)

encrypted_PUUID = user_dic['puuid']

endpoint_match = f"https://{server_summoner}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{encrypted_PUUID}?api_key={api_key}"

summoner_dic = requests.get(endpoint_match).json()
print(summoner_dic)