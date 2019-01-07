import requests
import conf.api_config as config
from apiclient.coc_api import CocApi

bearer_token=config.bearer
api_endpoint=config.endpoint

api = CocApi(bearer_token, api_endpoint, 'v1')
print api.get_clan('LCC8CL')
