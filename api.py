import requests
import conf.api_config as config

bearer_token=config.bearer

r = requests.get(
  'https://api.clashofclans.com/v1/players/%2382CGCYPJJ',
  headers={"Accept": "application/json", "authorization": "Bearer {}".format(bearer_token)})
print r.content
