import conf.api_config as config
import os
from apiclient.coc_api import CocApi
from apiclient.storage.storage_factory import StorageFactory
from apiclient.mapper.mapper_factory import MapperFactory
import json

bearer_token = config.bearer
api_endpoint = config.endpoint
api_version = config.version

api = CocApi(bearer_token, api_endpoint, api_version)
storage = StorageFactory.factory('file', '%s/data' % os.getcwd())

clan_tag = 'LCC8CL'
storage.refresh_clan(clan_tag)
# clan_data = api.get_clan(clan_tag)
# storage.save_clan(clan_tag, clan_data)

# player_tag = '82CGCYPJJ'
# player_data = api.get_player(player_tag)
# storage.save_player(player_tag, player_data)

clan_data = storage.read_clan(clan_tag)
clan_mapper = MapperFactory.factory('clan')
clan_model = clan_mapper.map_dict_to_model(json.loads(clan_data), None, True)

print clan_model.name
print clan_model.members
for _, m in clan_model.member_list.iteritems():
    print m.name

# player_data = storage.read_player(player_tag)
# print player_data
