import requests

HTTP_OK = 200


class BaseConnector:
    def __init__(self, host):
        self._api_base = 'https://{}'.format(host)

    def do_post(self, endpoint, data=None, params=None):
        return self._do_http(requests.post, endpoint, data, params)

    def do_put(self, endpoint, data=None, params=None):
        return self._do_http(requests.put, endpoint, data, params)

    def do_delete(self, endpoint, data=None, params=None):
        return self._do_http(requests.delete, endpoint, data, params)

    def do_get(self, endpoint, data=None, params=None):
        return self._do_http(requests.get, endpoint, data, params)

    def _do_http(self, method, endpoint, data, params):
        return method('{}/{}'.format(self._api_base, endpoint),
                      data=data,
                      params=params,
                      headers={'Content-Type': 'application/json'})
