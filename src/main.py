from steam import Steam
from datetime import datetime
import configparser
import json

config = configparser.ConfigParser()
config.read('cfg.ini')
key = config.get('api', 'steamapikey')

sc = Steam(key)
result = sc.users.get_owned_games("76561198203717873")
print(result)
with open('temp.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

