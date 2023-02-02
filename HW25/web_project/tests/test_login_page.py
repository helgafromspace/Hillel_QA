
from web_project.pages.login_page import LoginPage
from web_project.conftest import User
import time
import pytest

def test_user_can_login_from_main_page_with_valid_login_and_password(driver,login_page):
    login_page.perform_successful_login()
    login_page.go_to_profile_page(driver)
    login_page.check_email_concordance()


def test_user_can_login_from_main_page_with_valid_email_and_password(driver,login_page):
    login_page.perform_successful_login(email_flag=True)
    login_page.go_to_profile_page(driver)
    login_page.check_email_concordance()


def test_user_cant_login_with_invalid_login(driver, login_page, invalid_user):
    login_page.perform_unsuccessful_login(invalid_user)
    login_page.error_message_for_invalid_creds_is_displayed()

def test_user_cant_login_with_invalid_email(driver, login_page, invalid_user):
    login_page.perform_unsuccessful_login(invalid_user)
    login_page.error_message_for_invalid_creds_is_displayed ()


def test_user_cant_login_with_correct_login_and_incorrect_password(driver, login_page):
    login_page.perform_successful_login(change_password=True)
    login_page.error_message_for_invalid_creds_is_displayed ()


def test_user_cant_login_with_incorrect_login_and_correct_password(driver, login_page):
    login_page.perform_successful_login(change_login=True)
    login_page.error_message_for_invalid_creds_is_displayed ()


