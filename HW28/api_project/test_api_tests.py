"""
Для ресурса  , написать тест(ы) для проверки создания поста.

Пользователь для которого создается пост должен быть создан для теста, и удален после теста.

Постараться написать структурировано и красиво:)

"""
from pprint import pprint

import requests

from .helpers.helper_config import get_create_user_url
from .helpers.status_codes import StatusCodes

headers = {"Accept" : "application/json",
           "Content-Type" : "application/json",
           "Authorization" : "Bearer 853ca9386e4300ab03a1828e8cd7b76f99070f2321d18ff9ac70dc279ec6c863"}

# def test_create_user(api_user,create_user):
#     assert create_user.json()["name"] == api_user["name"]
#     assert create_user.json ()["gender"] == api_user["gender"]
#     assert create_user.json ()["email"] == api_user["email"]
#     assert create_user.json ()["status"] == api_user["status"]
#     assert create_user.status_code == StatusCodes.CREATED.value
#
def test_create_post_and_delete_user(api_user,create_user):
    req_user_id = create_user.json()["id"]
    url = get_create_user_url()
    data = {
        'title': 'First post',
        'body': 'Hello world!'
    }
    create_post = requests.post(f'{url}/{req_user_id}/posts', json=data, headers=headers)

    print(create_post.json())
    res_user_id = create_post.json()['user_id']
    res_user_title = create_post.json()['title']
    res_user_body = create_post.json()['body']

    get_user_posts = requests.get(f'{url}/{req_user_id}/posts', headers=headers)

    print(get_user_posts.json())
    assert res_user_id == req_user_id
    assert res_user_title == data['title']
    assert res_user_body == data['body']
    assert get_user_posts.status_code == StatusCodes.OK.value

    user_info = requests.get (f'{url}/{req_user_id}', headers=headers)
    print(user_info.json())

    requests.delete(f'{url}/{req_user_id}', headers=headers)

    response_posts_after_del = requests.get(f'{url}/{req_user_id}/posts', headers=headers)

    user_info = requests.get(f'{url}/{req_user_id}', headers=headers)

    assert user_info.status_code == StatusCodes.NOT_FOUND.value
    assert user_info.json()['message'] == 'Resource not found'
    assert not response_posts_after_del.json()
