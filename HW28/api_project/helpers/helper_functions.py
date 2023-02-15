from random import randint, choice

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