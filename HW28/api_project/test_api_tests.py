"""
Для ресурса  , написать тест(ы) для проверки создания поста.

Пользователь для которого создается пост должен быть создан для теста, и удален после теста.

Постараться написать структурировано и красиво:)

"""


import requests

from .helpers.headers import CreateUserHeaders
from .helpers.helper_config import get_create_user_url
from .helpers.status_codes import StatusCodes
from .helpers.helper_functions import create_post

def test_create_post(create_user):
    req_user_id = create_user.json()["id"]
    url = get_create_user_url()
    data = {
        'title': 'First post',
        'body': 'Hello world!'
    }

    created_post = create_post(req_user_id, data)
    assert created_post.status_code == StatusCodes.CREATED.value

    res_user_id = created_post.json()['user_id']
    res_user_title = created_post.json()['title']
    res_user_body = created_post.json()['body']

    get_user_posts = requests.get(f'{url}/{req_user_id}/posts', headers=CreateUserHeaders.headers)

    assert res_user_id == req_user_id
    assert res_user_title == data['title']
    assert res_user_body == data['body']
    assert len(get_user_posts.json()) == 1

def test_create_post_with_empty_data(create_user):
    req_user_id = create_user.json()["id"]
    url = get_create_user_url()
    data = {
        'title': '',
        'body': ''
    }
    created_post = create_post(req_user_id, data)

    assert created_post.status_code == StatusCodes.UNPROCESSABLE_ENTITY.value
    assert len(created_post.json()) == 2
    assert created_post.json()[0]['field'] == 'title'
    assert created_post.json()[0]['message'] == "can't be blank"
    assert created_post.json()[1]['field'] == 'body'
    assert created_post.json()[1]['message'] == "can't be blank"

    get_user_posts = requests.get(f'{url}/{req_user_id}/posts', headers=CreateUserHeaders.headers)

    assert get_user_posts.status_code == StatusCodes.OK.value
    assert get_user_posts.json() == []

def test_create_2_posts(create_user):
    req_user_id = create_user.json()["id"]
    url = get_create_user_url()
    data = {
        'title': 'First post',
        'body': 'Hello world!'
    }
    created_1_post = create_post(req_user_id, data)

    res_1_user_id = created_1_post.json()['user_id']

    data2 = {
        'title': 'Second post',
        'body': 'Hello world 2!'
    }
    created_2_post = create_post(req_user_id, data2)

    res_2_user_id = created_2_post.json()['user_id']

    assert created_2_post.status_code == StatusCodes.CREATED.value

    get_user_posts = requests.get(f'{url}/{req_user_id}/posts', headers=CreateUserHeaders.headers)
    posts_list = get_user_posts.json()

    assert get_user_posts.status_code == StatusCodes.OK.value
    assert len(get_user_posts.json()) == 2
    assert res_1_user_id == res_2_user_id
    assert posts_list[0]['user_id'] == req_user_id
    assert posts_list[1]['user_id'] == req_user_id
    assert posts_list[0]['title'] == data2['title']
    assert posts_list[0]['body'] == data2['body']
    assert posts_list[1]['title'] == data['title']
    assert posts_list[1]['body'] == data['body']


# def test_get_info_after_del(create_user):
#     req_user_id = 408971
#     url = get_create_user_url()
#     get_user_posts_after_del = requests.get(f'{url}/{req_user_id}/posts', headers=CreateUserHeaders.headers)
#     user_info = requests.get (f'{url}/{req_user_id}', headers=CreateUserHeaders.headers)
#     print(user_info.json())
#     print(get_user_posts_after_del.json())
#     assert get_user_posts_after_del.json() == []
#     print (get_user_posts_after_del.status_code)

