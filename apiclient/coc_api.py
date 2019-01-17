import requests


class CocApi(object):

    def __init__(self, bearer, endpoint, endpoint_version):
        self.bearer = bearer
        self.endpoint = endpoint
        self.endpoint_version = endpoint_version

    def get_clan(self, tag):
        r = self.__make_request('clans', tag)
        return r.content

    def get_player(self, tag):
        r = self.__make_request('players', tag)
        return r.content

    def __make_request(self, section, tag):
        return requests.get(
            self.__build_uri(section) + '/%23{}'.format(tag),
            headers=self.__build_headers())

    def __build_uri(self, section):
        return self.endpoint + '/' + self.endpoint_version + '/' + section

    def __build_headers(self):
        return {"Accept": "application/json",
                "authorization": "Bearer {}".format(self.bearer)}
