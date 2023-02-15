from random import randint, choice

import requests

from api_project.helpers.headers import CreateUserHeaders
from api_project.helpers.helper_config import get_create_user_url

names_list = ['susy', 'valerie', 'cathrine', 'dolly', 'sasori', 'alexander', 'sandy', 'burnold', 'steven', 'jane', 'kessy',
              'mike', 'kaiser','willy', 'ram']
surnames_list = ['does', 'brinf', 'dariggs', 'goons', 'kreeks', 'bildin', 'xanders', 'reene', 'deen', 'draggins',
                 'rith', 'silland']
domains_list = ['@boss.com', '@com.ua', '@com.au', '@gmail.com']

gender = ['male','female']

status_list = ['active','inactive']
def email_generator():
    seq = choice(names_list) + choice(surnames_list)
    for _ in range(5):
        seq += chr(randint(48,57))
    current_email = seq + choice(domains_list)
    return current_email

def login_generator():
    seq = choice(names_list).capitalize() + ' '+ choice(surnames_list).capitalize()
    return seq

def gender_generator():
    return choice(gender)

def status_generator():
    return choice(status_list)


def test_get_info_after_del(req_user_id):
    url = get_create_user_url()
    get_user_posts_after_del = requests.get(f'{url}/{req_user_id}/posts', headers=CreateUserHeaders.headers)
    user_info = requests.get(f'{url}/{req_user_id}', headers=CreateUserHeaders.headers)
    print(user_info.json())
    print(get_user_posts_after_del.json())