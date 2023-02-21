from configparser import ConfigParser
import os
def get_root_directory():
    return os.path.split(__file__)[0]

print(get_root_directory())
def get_config():
    config = ConfigParser()
    config.read(os.path.join(get_root_directory(),'config.ini'))
    return config

def get_db_path():
    return get_config().get('project','db_path')