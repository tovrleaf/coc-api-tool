import requests
import conf.api_config as config

bearer_token=config.bearer
api_endpoint=config.endpoint

def build_headers():
  return {"Accept": "application/json", "authorization": "Bearer {}".format(bearer_token)}

def build_uri(section):
  return api_endpoint + '/' + section


def get_clan(tag):
  r = requests.get(
    build_uri('clans') + '/%23{}'.format(tag),
    headers=build_headers())
  print r.content

def get_player(tag):
  r = requests.get(
    build_uri('players') + '/%23{}'.format(tag),
    headers=build_headers())
  print r.content

get_clan('LCC8CL')
