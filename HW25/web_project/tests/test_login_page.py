from web_project.helpers.resources import Resources


def test_user_can_login_from_main_page_with_valid_login_and_password(driver,login_page, valid_user):
    login_page.login_link.click ()
    assert login_page.login_popup.is_displayed()
    login_page.enter_login(valid_user.login)
    login_page.enter_password(valid_user.password)
    login_page.click_login_button()
    login_page.go_to_profile_page()
    assert login_page.profile_page_header.is_displayed()
    assert login_page.profile_page_header.text == Resources.LoginPage.PROFILE_PAGE_HEADER_TEXT
    assert login_page.get_profile_email_field() == valid_user.email


def test_user_can_login_from_main_page_with_valid_email_and_password(driver,login_page, valid_user):
    login_page.perform_successful_login(valid_user,email_flag=True)
    login_page.go_to_profile_page()
    assert login_page.profile_page_header.is_displayed()
    assert login_page.profile_page_header.text == Resources.LoginPage.PROFILE_PAGE_HEADER_TEXT
    assert login_page.get_profile_email_field() == valid_user.email


def test_user_cant_login_with_unregistered_login(driver, login_page, unregistered_user):
    login_page.perform_unsuccessful_login(unregistered_user)
    assert login_page.login_popup.is_displayed()
    assert login_page.login_invalid_creds_error.is_displayed()
    assert login_page.login_invalid_creds_error.text == Resources.LoginPage.INCORRECT_CREDS_ERROR_MESSAGE

def test_user_cant_login_with_unregistered_email(driver, login_page, unregistered_user):
    login_page.perform_unsuccessful_login(unregistered_user)
    assert login_page.login_popup.is_displayed()
    assert login_page.login_invalid_creds_error.is_displayed()
    assert login_page.login_invalid_creds_error.text == Resources.LoginPage.INCORRECT_CREDS_ERROR_MESSAGE


def test_user_cant_login_with_correct_login_and_incorrect_password(driver, login_page, valid_user):
    login_page.perform_successful_login(valid_user,change_password=True)  # Why here successful login used if we enter incorrect login?
    assert login_page.login_invalid_creds_error.is_displayed()
    assert login_page.login_invalid_creds_error.text == Resources.LoginPage.INCORRECT_CREDS_ERROR_MESSAGE

def test_user_cant_login_with_incorrect_login_and_correct_password(driver, login_page,valid_user):
    login_page.perform_successful_login(valid_user, change_login=True)  # Why here successful login used if we enter incorrect login?
    assert login_page.login_invalid_creds_error.is_displayed()
    assert login_page.login_invalid_creds_error.text == Resources.LoginPage.INCORRECT_CREDS_ERROR_MESSAGE

def test_user_can_logout_from_main_page(driver,login_page,valid_user):
    login_page.perform_successful_login(valid_user)
    login_page.perform_logout()
    assert login_page.login_link.is_displayed()


