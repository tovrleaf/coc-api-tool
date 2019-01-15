import requests


class CocApi(object):

    def __init__(self, bearer, endpoint, endpoint_version):
        self.bearer = bearer
        self.endpoint = endpoint
        self.endpoint_version = endpoint_version

    def get_clan(self, tag):
        r = requests.get(
            self.__build_uri('clans') + '/%23{}'.format(tag),
            headers=self.__build_headers())
        return r.content

    def get_player(self, tag):
        r = requests.get(
            self.__build_uri('players') + '/%23{}'.format(tag),
            headers=self.__build_headers())
        return r.content

    def __build_uri(self, section):
        return self.endpoint + '/' + self.endpoint_version + '/' + section

    def __build_headers(self):
        return {"Accept": "application/json",
                "authorization": "Bearer {}".format(self.bearer)}
