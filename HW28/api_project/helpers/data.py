class Data:
    pass

class CreatePostData(Data):
    valid_data_1_post = {
        'title': 'First post',
        'body': 'Hello world!',
    }

    invalid_empty_data = {
        'title': '',
        'body': '',
    }

    valid_data_2_post = {
        'title': 'Second post',
        'body': 'Hello world 2!',
    }

    invalid_data_excessive_field = {
        'title': 'Third post',
        'name': 'James',
        'body': 'Hello world 3',
    }

