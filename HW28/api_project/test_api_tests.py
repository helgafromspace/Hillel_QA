"""
Для ресурса  , написать тест(ы) для проверки создания поста.

Пользователь для которого создается пост должен быть создан для теста, и удален после теста.

Постараться написать структурировано и красиво:)

"""


import requests

from .helpers.headers import CreateUserHeaders
from .helpers.helper_config import get_create_user_url
from .helpers.status_codes import StatusCodes


def test_create_post(api_user, create_user):
    req_user_id = create_user.json()["id"]
    url = get_create_user_url()
    data = {
        'title': 'First post',
        'body': 'Hello world!'
    }
    create_post = requests.post(f'{url}/{req_user_id}/posts', json=data, headers=CreateUserHeaders.headers)
    assert create_post.status_code == StatusCodes.CREATED.value

    res_user_id = create_post.json()['user_id']
    res_user_title = create_post.json()['title']
    res_user_body = create_post.json()['body']

    get_user_posts = requests.get(f'{url}/{req_user_id}/posts', headers=CreateUserHeaders.headers)

    assert res_user_id == req_user_id
    assert res_user_title == data['title']
    assert res_user_body == data['body']
    assert len(get_user_posts.json()) == 1

def test_create_post_with_empty_data(api_user,create_user):
    req_user_id = create_user.json()["id"]
    url = get_create_user_url()
    data = {
        'title': '',
        'body': ''
    }
    create_post = requests.post(f'{url}/{req_user_id}/posts', json=data, headers=CreateUserHeaders.headers)

    assert create_post.status_code == StatusCodes.UNPROCESSABLE_ENTITY.value
    assert len(create_post.json()) == 2
    assert create_post.json()[0]['field'] == 'title'
    assert create_post.json()[0]['message'] == "can't be blank"
    assert create_post.json()[1]['field'] == 'body'
    assert create_post.json()[1]['message'] == "can't be blank"

    get_user_posts = requests.get(f'{url}/{req_user_id}/posts', headers=CreateUserHeaders.headers)

    assert get_user_posts.status_code == StatusCodes.OK.value
    assert get_user_posts.json() == []

def test_create_2_posts(api_user, create_user):
    req_user_id = create_user.json()["id"]
    url = get_create_user_url()
    data = {
        'title': 'First post',
        'body': 'Hello world!'
    }
    create_1_post = requests.post(f'{url}/{req_user_id}/posts', json=data, headers=CreateUserHeaders.headers)

    res_1_user_id = create_1_post.json()['user_id']

    data2 = {
        'title': 'Second post',
        'body': 'Hello world 2!'
    }
    create_2_post = requests.post(f'{url}/{req_user_id}/posts', json=data2, headers=CreateUserHeaders.headers)

    res_2_user_id = create_2_post.json()['user_id']

    assert create_2_post.status_code == StatusCodes.CREATED.value

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

