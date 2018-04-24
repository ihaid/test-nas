import configparser

import pytest

from connector.base_connector import BaseConnector


@pytest.fixture(scope='session')
def config():
    configuration = configparser.ConfigParser()
    configuration.read('test_config.ini')
    return configuration


@pytest.fixture(scope='session')
def base_connector(config):
    base_config = config['beti']
    return BaseConnector(base_config.get('host', ''))
