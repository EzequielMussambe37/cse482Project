from steam import Steam
from datetime import datetime
import configparser
import json

config = configparser.ConfigParser()
config.read('cfg.ini')
key = config.get('api', 'steamapikey')

sc = Steam(key)
result = sc.users.get_owned_games("76561198203717873")
#result = sc.apps.get_app_details(420)
with open('temp.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

user_id = sc.users.search_user("Jokitech")


#gameid = sc.apps.get_app_details(420, "US", None, "genre")
#print(gameid)
# arguments: steamid
user = sc.users.get_account_public_info("76561198203717873")

