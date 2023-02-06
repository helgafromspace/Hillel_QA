import pytest
from web_project.helpers.resources import Resources


def test_user_can_go_to_register_popup_from_main_page(driver, register_page):
    register_page.open_register_form()
    assert register_page.register_form.is_displayed ()

def test_register_popup_has_required_fields_for_registration(driver, register_page):
    register_page.register_form_has_required_fields()
    assert register_page.input_register_email.is_displayed ()
    assert register_page.email_label.is_displayed ()
    assert register_page.email_label.text == Resources.RegisterPage.EMAIL_LABEL_TEXT
    assert register_page.email_field_notification.is_displayed ()
    assert register_page.email_field_notification.text == Resources.RegisterPage.EMAIL_FIELD_NOTIFICATION_TEXT

    assert register_page.input_register_login.is_displayed ()
    assert register_page.login_label.is_displayed ()
    assert register_page.login_label.text == Resources.RegisterPage.LOGIN_LABEL_TEXT
    assert register_page.login_field_notification.is_displayed ()
    assert register_page.login_field_notification.text == Resources.RegisterPage.LOGIN_FIELD_NOTIFICATION_TEXT

    assert register_page.input_register_password.is_displayed ()
    assert register_page.password_label.is_displayed ()
    assert register_page.password_label.text == Resources.RegisterPage.PASSWORD_LABEL_TEXT

    assert register_page.submit_button.is_displayed ()
    assert register_page.submit_button.text == Resources.RegisterPage.SUBMIT_BUTTON_TEXT

@pytest.mark.parametrize('email_param',['ahjhsajshj.gmail.com', ' ', 'gmail.com'])
def test_user_cant_register_with_invalid_email(driver,register_page,email_param):
    register_page.open_register_form()
    register_page.enter_invalid_email(email_param)
    assert register_page.email_invalidity_checker.is_displayed ()
    assert register_page.email_invalidity_checker.text == Resources.RegisterPage.EMAIL_INVALIDITY_MESSAGE

@pytest.mark.parametrize('login_param',['E', 'df', 'login_with_more_than_30_letters'])
def test_user_cant_register_with_invalid_login(driver,register_page,login_param):
    register_page.open_register_form()
    register_page.enter_invalid_login(login_param)
    assert register_page.login_invalidity_checker.is_displayed ()
    assert register_page.login_invalidity_checker.text == Resources.RegisterPage.LOGIN_INVALIDITY_MESSAGE

@pytest.mark.parametrize('password_param',['1', '5'])
def test_user_cant_register_with_invalid_password(driver,register_page,password_param):
    register_page.open_register_form()
    register_page.enter_invalid_password(password_param)
    assert register_page.password_invalidity_checker.is_displayed ()
    assert register_page.password_invalidity_checker.text == Resources.RegisterPage.PASSWORD_INVALIDITY_MESSAGE

def test_user_cant_register_with_blank_fields(driver,register_page):
    register_page.perform_unsuccessfull_registration_with_empty_credentials_fields()
    assert register_page.empty_name_error.is_displayed ()
    assert register_page.empty_name_error.text == Resources.RegisterPage.EMPTY_NAME_ERROR
    assert register_page.login_field_error.is_displayed ()
    assert register_page.login_field_error.text == Resources.RegisterPage.LOGIN_FIELD_ERROR
    assert register_page.password_invalidity_checker.is_displayed ()
    assert register_page.password_invalidity_checker.text == Resources.RegisterPage.PASSWORD_INVALIDITY_MESSAGE
    assert register_page.email_field_error.is_displayed ()
    assert register_page.email_field_error.text == Resources.RegisterPage.EMAIL_INVALIDITY_MESSAGE








