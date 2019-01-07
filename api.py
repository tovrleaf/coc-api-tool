import conf.api_config as config
import os
from apiclient.coc_api import CocApi
from apiclient.storage.file_storage import FileStorage


bearer_token = config.bearer
api_endpoint = config.endpoint

api = CocApi(bearer_token, api_endpoint, 'v1')
storage = FileStorage('%s/data' % os.getcwd())

clan_tag = 'LCC8CL'
clan_data = api.get_clan(clan_tag)
storage.save_clan(clan_tag, clan_data)

player_tag = '82CGCYPJJ'
player_data = api.get_player(player_tag)
storage.save_player(player_tag, player_data)
