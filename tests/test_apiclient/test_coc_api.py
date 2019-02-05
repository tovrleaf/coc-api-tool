from apiclient.coc_api import CocApi
import mock
import requests


def test_constructor():
    key = 'some_key'
    url = 'http://foo'
    version = 'v0'
    api = CocApi(key, url, version)
    assert api.bearer == key
    assert api.endpoint == url
    assert api.endpoint_version == version


def test_clan():
    bearer = 'bar1'
    endpoint = 'biz1'
    version = 'v1'
    tag = 'foo1'
    api = CocApi(bearer, endpoint, version, False)
    request = api.get_clan(tag)
    helper_request(request, bearer, endpoint, version, tag, 'clans')


def test_player():
    bearer = 'bar2'
    endpoint = 'biz2'
    version = 'v2'
    tag = 'foo2'
    api = CocApi(bearer, endpoint, version, False)
    request = api.get_player(tag)
    helper_request(request, bearer, endpoint, version, tag, 'players')


def test_coc_request_get():
    with mock.patch('requests.get'):
        param1 = 'a'
        param2 = 'b'
        r = CocApi.CocRequest(param1, param2)
        r.get()
        requests.get.assert_called_once_with(param1, headers=param2)


def test_coc_api_extract_data():
    class stub():
        content = 'pp'

    with mock.patch('apiclient.coc_api.CocApi.CocRequest.get',
                    return_value=stub):
        api = CocApi('a', 'b', 'c')
        assert api.get_player(4) == 'pp'


def helper_request(request, bearer, endpoint, version, tag, token):
    assert type(request).__name__ == 'CocRequest'
    assert type(request.headers).__name__ == 'dict'
    assert request.uri.startswith(endpoint)
    assert '/' + version + '/' in request.uri
    assert '/' + token + '/' in request.uri
    assert request.uri.endswith(tag)
    assert bearer in request.headers.get('authorization')
