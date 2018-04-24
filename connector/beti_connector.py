import json

import requests
from connector.base_connector import BaseConnector

HTTP_OK = 200

TOKEN_KEY = 'token'


class BetiConnector(BaseConnector):
    def __init__(self, host, user, password, brand_id):
        super(BetiConnector, self).__init__(host)
        self._auth_data = {"brandId": brand_id, "login": user, "password": password}
        self._token = None

    def _do_http(self, method, endpoint, data, params):
        return method('{}/{}'.format(self._api_base, endpoint),
                      data=data,
                      params=params,
                      headers={'Authorization': 'Bearer {}'.format(self._get_token()),
                               'Content-Type': 'application/json'})

    def _get_token(self):
        if self._token is None:
            self._token = self._generate_token()
        return self._token

    def _generate_token(self):
        response = requests.post('{}/{}'.format(self._api_base, 'auth/signin'),
                                 data=json.dumps(self._auth_data),
                                 headers={'Content-Type': 'application/json'})
        if response.status_code == HTTP_OK:
            return response.json()[TOKEN_KEY]
        raise Exception('Auth failed, status code : {}'.format(response.status_code))
