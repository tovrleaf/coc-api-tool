import requests


class CocApi(object):

    def __init__(self, bearer, endpoint, endpoint_version, execute=True):
        self.bearer = bearer
        self.endpoint = endpoint
        self.endpoint_version = endpoint_version
        self.execute = execute

    def get_clan(self, tag):
        r = self.__create_request('clans', tag)
        if self.execute is True:
            return r.get().content
        return r

    def get_player(self, tag):
        r = self.__create_request('players', tag)
        if self.execute is True:
            return r.get().content
        return r

    def __create_request(self, section, tag):
        return self.CocRequest(
            self.__build_uri(section) + '/%23{}'.format(tag),
            self.__build_headers())

    def __build_uri(self, section):
        return self.endpoint + '/' + self.endpoint_version + '/' + section

    def __build_headers(self):
        return {"Accept": "application/json",
                "authorization": "Bearer {}".format(self.bearer)}

    class CocRequest(object):

        def __init__(self, uri, headers, execute=False):
            self.uri = uri
            self.headers = headers

        def get(self):
            return requests.get(self.uri, headers=self.headers)
