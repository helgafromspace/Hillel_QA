from configparser import ConfigParser
import os
def get_root_directory():
    return os.path.split(os.path.split(__file__)[0])[0]

print(get_root_directory())
def get_config():
    config = ConfigParser()
    config.read(os.path.join(get_root_directory(),'config.ini'))
    return config

def get_create_user_url():
    return get_config().get('project','create_user_url')