import json
import logging

from connector.beti_connector import BetiConnector
from utils import utils
from utils.user_data_builder import User

CONF_FILE = 'test_config.ini'
BRAND_ID_KEY = 'brand_id'
UUID_KEY = 'playerUUID'
HOST_KEY = 'host'

TRIES = 3

logging.basicConfig(filename="test_app.log", level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger("ex")


def test_user(base_connector, config):
    log.info('Test started')
    user_data = User()
    email = user_data.email
    password = user_data.password
    host, brand_id = _config(config)
    data = json.dumps(utils.jdefault(user_data))
    signup_response = base_connector.do_post('profile/public/signup',
                                             data=data,
                                             params='brandId={}'.format(brand_id))
    utils.check_status_code_is_ok(signup_response)
    user_id = utils.retrieve_user_id(signup_response)
    log.info('User: {} created with password: {}. User id is: {}'
             .format(email, password, user_id))
    auth = BetiConnector(host, email, password, brand_id)
    log.info('Successfully authorized')
    profile = utils.wait_for_data(auth.do_get, 'profile/profiles/{}'
                                  .format(user_id), TRIES)

    assert user_id in profile.get(UUID_KEY)

    log.info('Test ended')


def _config(config):
    host = config['beti'].get(HOST_KEY, '')
    brand_id = config['beti'].get(BRAND_ID_KEY, '')
    return host, brand_id
