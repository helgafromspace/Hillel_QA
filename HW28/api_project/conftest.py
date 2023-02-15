import pytest
import requests

from .helpers.helper_config import get_create_user_url
from .helpers.helper_functions import login_generator, gender_generator, email_generator, \
    status_generator
from .helpers.user import UserApi


@pytest.fixture()
def api_user():
    return UserApi (login_generator (), gender_generator (), email_generator (), status_generator()).json_constructor()

@pytest.fixture()
def create_user(api_user):
    headers = {"Accept": "application/json",
               "Content-Type": "application/json",
               "Authorization": "Bearer 853ca9386e4300ab03a1828e8cd7b76f99070f2321d18ff9ac70dc279ec6c863"}
    response = requests.post(get_create_user_url(), json=api_user, headers=headers)
    return response






