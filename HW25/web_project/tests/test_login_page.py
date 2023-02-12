from web_project.helpers.resources import Resources
from web_project.helpers.user import User
import allure

@allure.feature('Login')
@allure.story('Successful login')
def test_user_can_login_from_main_page_with_valid_login_and_password(driver,login_page, valid_user):
    login_page.click_login_link()
    assert login_page.login_popup.is_displayed()
    login_page.enter_login(valid_user.login)
    login_page.enter_password (valid_user.password)
    login_page.click_login_button()
    login_page.go_to_profile_page()
    assert login_page.profile_page_header.is_displayed()
    assert login_page.profile_page_header.text == Resources.LoginPage.PROFILE_PAGE_HEADER_TEXT
    assert login_page.get_profile_email_field() == valid_user.email

@allure.feature('Login')
@allure.story('Successful login')
def test_user_can_login_from_main_page_with_valid_email_and_password(driver,login_page, valid_user):
    login_page.perform_successful_login(valid_user,email_flag=True)
    login_page.go_to_profile_page()
    assert login_page.profile_page_header.is_displayed()
    assert login_page.profile_page_header.text == Resources.LoginPage.PROFILE_PAGE_HEADER_TEXT
    assert login_page.get_profile_email_field() == valid_user.email

@allure.feature('Login')
@allure.story('Unsuccessful login')
def test_user_cant_login_with_unregistered_login(driver, login_page, unregistered_user):
    login_page.perform_unsuccessful_login(unregistered_user)
    assert login_page.login_popup.is_displayed()
    assert login_page.login_invalid_creds_error.is_displayed()
    assert login_page.login_invalid_creds_error.text == Resources.LoginPage.INCORRECT_CREDS_ERROR_MESSAGE

@allure.feature('Login')
@allure.story('Unsuccessful login')
def test_user_cant_login_with_unregistered_email(driver, login_page, unregistered_user):
    login_page.perform_unsuccessful_login(unregistered_user,email_flag=True)
    assert login_page.login_popup.is_displayed()
    assert login_page.login_invalid_creds_error.is_displayed()
    assert login_page.login_invalid_creds_error.text == Resources.LoginPage.INCORRECT_CREDS_ERROR_MESSAGE

@allure.feature('Login')
@allure.story('Unsuccessful login')
def test_user_cant_login_with_correct_login_and_incorrect_password(driver, login_page, valid_user,unregistered_user):
    test_user = User(valid_user.login,unregistered_user.password,valid_user.email)
    login_page.perform_unsuccessful_login(test_user)
    assert login_page.login_invalid_creds_error.is_displayed()
    assert login_page.login_invalid_creds_error.text == Resources.LoginPage.INCORRECT_CREDS_ERROR_MESSAGE

@allure.feature('Login')
@allure.story('Unsuccessful login')
def test_user_cant_login_with_incorrect_login_and_correct_password(driver, login_page,valid_user,unregistered_user):
    test_user = User (unregistered_user.login, valid_user.password, valid_user.email)
    login_page.perform_unsuccessful_login(test_user)
    assert login_page.login_invalid_creds_error.is_displayed()
    assert login_page.login_invalid_creds_error.text == Resources.LoginPage.INCORRECT_CREDS_ERROR_MESSAGE

@allure.feature('Login')
@allure.story('Unsuccessful login')
def test_user_cant_login_with_correct_email_and_incorrect_password(driver, login_page, valid_user,unregistered_user):
    test_user = User (valid_user.login, unregistered_user.password, valid_user.email)
    login_page.perform_unsuccessful_login(test_user,email_flag=True)
    assert login_page.login_invalid_creds_error.is_displayed()
    assert login_page.login_invalid_creds_error.text == Resources.LoginPage.INCORRECT_CREDS_ERROR_MESSAGE

@allure.feature('Login')
@allure.story('Unsuccessful login')
def test_user_cant_login_with_incorrect_email_and_correct_password(driver, login_page, valid_user,unregistered_user):
    test_user = User (valid_user.login, unregistered_user.password, unregistered_user.email)
    login_page.perform_unsuccessful_login(test_user,email_flag=True)
    assert login_page.login_invalid_creds_error.is_displayed()
    assert login_page.login_invalid_creds_error.text == Resources.LoginPage.INCORRECT_CREDS_ERROR_MESSAGE

@allure.feature('Login')
@allure.story('Successful logout')
def test_user_can_logout_from_main_page(driver,login_page,valid_user):
    login_page.perform_successful_login(valid_user)
    login_page.perform_logout()
    assert login_page.login_link.is_displayed()


