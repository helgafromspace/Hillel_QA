import pytest
import requests

from .helpers.headers import CreateUserHeaders
from .helpers.helper_config import get_create_user_url
from .helpers.helper_functions import login_generator, gender_generator, email_generator, \
    status_generator
from .helpers.user import UserApi


@pytest.fixture()
def api_user():
    return UserApi(login_generator(), gender_generator(), email_generator(), status_generator())

@pytest.fixture()
def create_user(api_user):
    url = get_create_user_url()
    response = requests.post(url, json=api_user.json_constructor(), headers=CreateUserHeaders.headers)
    req_user_id = response.json()["id"]
    yield response
    requests.delete(f'{url}/{req_user_id}', headers=CreateUserHeaders.headers)








