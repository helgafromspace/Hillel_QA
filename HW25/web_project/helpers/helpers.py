from random import *

import time

# path = '/home/helga/Hillel_QA/drivers/chromedriver/chromedriver'
names_list = ['susan', 'mandy', 'catarina', 'daisysmile', 'lenie', 'ken', 'sole', 'oleksandr', 'ranley', 'jan', 'lascel',
              'sersey', 'joffrey','sansa', 'sheldon','pete']
surnames_list = ['doels', 'babers', 'teriggs', 'monsons', 'seeks', 'stark', 'thunderson', 'cullen', 'lanister', 'jaggins',
                 'smithens','harelson','kavidson']


class User:
    def __init__(self,login,password,email):
        self.login = login
        self.password = password
        self.email = email

def email_generator():
    domains_list = ['@yahoo.com', '@com.ua', '@com.de', '@gmail.com']
    seq = choice(names_list) + choice(surnames_list)
    for _ in range(5):
        seq += chr(randint(48,57))
    current_email = seq + choice(domains_list)
    return current_email

def login_generator():
    seq = choice(names_list).capitalize() + choice(surnames_list).capitalize()
    for _ in range(2):
        seq += chr(randint(48,57)) + chr(randint(48,57))
    return seq

def password_generator():
    seq = ''
    for _ in range(5):
        seq += chr(randint(48,57)) + chr(randint(65,90))+chr(randint(97,122))
    return seq


def test_register_data_writer(*args):
    test_data =''
    for i in args:
        test_data += i +','
    test_data = test_data[:-1]
    with open('/home/helga/Hillel_QA/HW25/web_project/helpers/register_page_data.py', 'a') as f:
        f.writelines(test_data + '\n')
    f.close()

