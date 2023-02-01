
from web_project.pages.login_page import LoginPage
from web_project.conftest import User
import time

def test_user_can_login_from_main_page_with_login_and_password(driver,login_page):
    login_page.perform_successful_login()

    assert login_page.login_popup.is_displayed ()
    assert login_page.profile_dropdown.is_displayed()

def test_user_can_login_from_main_page_with_email_and_password(driver,login_page):
    login_page.perform_successful_login(email_flag=True)
    assert login_page.login_popup.is_displayed ()
    assert login_page.profile_dropdown.is_displayed()


def test_user_cant_login_with_invalid_login(driver, login_page, invalid_user):
    login_page.perform_unsuccessful_login(invalid_user.login,invalid_user.password)

    assert login_page.login_popup.is_displayed ()
    assert login_page.login_invalid_creds_error.is_displayed()
    assert login_page.login_invalid_creds_error.text == 'Введен неверный логин или пароль.\nРекомендуем вместо логина вводить email.'



def test_user_cant_login_with_invalid_email(driver, login_page, invalid_user):
    login_page.perform_unsuccessful_login(invalid_user.login,invalid_user.password,invalid_user.email)

    assert login_page.login_popup.is_displayed ()
    assert login_page.login_invalid_creds_error.is_displayed()
    assert login_page.login_invalid_creds_error.text == 'Введен неверный логин или пароль.\nРекомендуем вместо логина вводить email.'


def test_user_cant_login_with_correct_login_and_incorrect_password(driver, login_page):
    login_page.perform_successful_login(change_password=True)
    assert login_page.login_popup.is_displayed ()
    assert login_page.login_invalid_creds_error.is_displayed ()
    assert login_page.login_invalid_creds_error.text == 'Введен неверный логин или пароль.\nРекомендуем вместо логина вводить email.'

def test_user_cant_login_with_incorrect_login_and_correct_password(driver, login_page):
    login_page.perform_successful_login(change_login=True)
    assert login_page.login_popup.is_displayed ()
    assert login_page.login_invalid_creds_error.is_displayed ()
    assert login_page.login_invalid_creds_error.text == 'Введен неверный логин или пароль.\nРекомендуем вместо логина вводить email.'

