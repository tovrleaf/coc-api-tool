import conf.api_config as config
import os
from apiclient.coc_api import CocApi
from apiclient.storage.storage_factory import StorageFactory


bearer_token = config.bearer
api_endpoint = config.endpoint
api_version = config.version

api = CocApi(bearer_token, api_endpoint, api_version)
storage = StorageFactory.factory('file', '%s/data' % os.getcwd())

clan_tag = 'LCC8CL'
clan_data = api.get_clan(clan_tag)
storage.save_clan(clan_tag, clan_data)

player_tag = '82CGCYPJJ'
player_data = api.get_player(player_tag)
storage.save_player(player_tag, player_data)

clan_data = storage.read_clan(clan_tag)
print clan_data

pclailayer_data = storage.read_player(player_tag)
print player_data
