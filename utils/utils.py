import time

HTTP_OK = 200
HTTP_CREATED = 201
HTTP_ACCEPTED = 202

USER_ID_KEY = 'playerUUID'

PUBLISH_DELAY = 5


def jdefault(data):
    json = data.__dict__
    return {key.replace('_', ''): json.pop(key) for key in json.copy()}


def retrieve_user_id(response):
    return response.json()[USER_ID_KEY]


def check_status_code_is_ok(response):
    check_status_code(response, HTTP_OK)


def check_status_code_is_created(response):
    check_status_code(response, HTTP_CREATED)


def check_status_code_is_accepted(response):
    check_status_code(response, HTTP_ACCEPTED)


def check_status_code(response, expected_code):
    assert response.status_code == expected_code


def wait_for_data(request, url, tries):
    for n in range(tries):
        response = request(url)
        time.sleep(PUBLISH_DELAY)
        if response.status_code is not HTTP_OK:
            continue
        break
    check_status_code_is_ok(response)
    return response.json()
