from random import randint

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time

from web_project.helpers.resources import Resources
from web_project.pages.base_page import BasePage

path = '/home/helga/Hillel_QA/drivers/chromedriver/chromedriver'

class LoginPage(BasePage):

    LOGIN_LINK_LOCATOR = (By.CSS_SELECTOR, 'a.b-tophead__login')
    LOGIN_POP_UP_LOCATOR = (By.ID, 'login-popup')
    INPUT_LOGIN_LOCATOR = (By.ID, 'login_name')
    INPUT_PASSWORD_LOCATOR = (By.ID, 'login_password')
    LOGIN_BUTTON_LOCATOR = (By.CSS_SELECTOR,'#login-popup button.login_button')
    PROFILE_DROPDOWN_LOCATOR = (By.XPATH, "//span[@class='b-tophead-dropdown'] [text()='Профиль']")
    PROFILE_SETTINGS_LOCATOR = (By.CSS_SELECTOR,".b-tophead-dropdown li a[href*='settings']")
    LOGOUT_LINK_LOCATOR = (By.CSS_SELECTOR, ".b-tophead-dropdown li a[href*='logout']")
    LOGIN_INVALID_CREDS_ERROR_LOCATOR = (By.XPATH, "//ul[@id='login-popup-errors']/li[contains(text(),'Введен неверный логин или пароль.')]")
    PROFILE_HEADER_LOCATOR = (By.TAG_NAME,'h1')
    PROFILE_EMAIL_FIELD_LOCATOR =(By.NAME, 'email')


    def __init__(self, driver: WebDriver, user_login=None, user_password=None, user_email=None):
        super().__init__(driver)
        self.user_login = user_login
        self.user_password = user_password
        self.user_email = user_email

    @property
    def login_link(self):
        return self.element_is_present(LoginPage.LOGIN_LINK_LOCATOR)

    @property
    def login_popup(self):
        return self.element_is_present(LoginPage.LOGIN_POP_UP_LOCATOR)

    @property
    def input_login(self):
        return self.element_is_present(LoginPage.INPUT_LOGIN_LOCATOR)

    @property
    def input_password_login(self):
        return self.element_is_present(LoginPage.INPUT_PASSWORD_LOCATOR)

    @property
    def login_button(self):
        return self.element_is_present(LoginPage.LOGIN_BUTTON_LOCATOR)

    @property
    def profile_dropdown(self):
        return self.element_is_present(LoginPage.PROFILE_DROPDOWN_LOCATOR)


    @property
    def profile_settings(self):
        return self.hidden_element_is_present(LoginPage.PROFILE_SETTINGS_LOCATOR)

    @property
    def logout_link(self):
        return self.hidden_element_is_present (LoginPage.LOGOUT_LINK_LOCATOR)

    @property
    def login_invalid_creds_error(self):
        return self.element_is_present (LoginPage.LOGIN_INVALID_CREDS_ERROR_LOCATOR)

    def navigate(self):
        self.driver.get('https://hdrezka.ag/')

    def set_registered_credentials(self,valid_user):
        self.user_login, self.user_password, self.user_email = valid_user.login, valid_user.password, valid_user.email

    def get_registered_creds(self,valid_user) :
        self.set_registered_credentials (valid_user)
        return self.user_login, self.user_password, self.user_email

    def enter_login(self,login):
        return self.input_login.send_keys(login)

    def enter_password(self,password):
        return self.input_password_login.send_keys(password)

    def click_login_button(self):
        self.login_button.click()

    def perform_successful_login(self,valid_user,email_flag=False, change_password=False, change_login=False):
        self.get_registered_creds (valid_user)
        if change_login:
            self.user_login = self.user_login + 2* chr(randint(65,90))
        if change_password:
            self.user_password = self.user_password + chr(randint(65,90))

        self.login_link.click()

        if email_flag:
            self.enter_login (self.user_email)
        else:
            self.enter_login (self.user_login)

        self.enter_password (self.user_password)
        time.sleep(3)

        self.click_login_button()

        assert self.login_popup.is_displayed ()

        return self


    def perform_unsuccessful_login(self, user,email_flag=False):
        self.login_link.click()
        if email_flag:
            self.enter_login(user.email)
        else:
            self.enter_login(user.login)
        self.enter_password (user.password)
        self.click_login_button()
        time.sleep (2)
        assert self.login_popup.is_displayed ()
        return self

    def error_message_for_invalid_creds_is_displayed(self):

        assert self.login_invalid_creds_error.is_displayed ()
        assert self.login_invalid_creds_error.text == Resources.LoginPage.INCORRECT_CREDS_ERROR_MESSAGE


    def go_to_profile_page(self,driver):
        action = ActionChains(driver)
        action.move_to_element(self.profile_dropdown).move_to_element(self.profile_settings).click().perform()
        h1 = self.element_is_present(LoginPage.PROFILE_HEADER_LOCATOR)
        assert h1.is_displayed()
        assert h1.text == 'Настройки профиля'

    def check_email_concordance(self):
        ''' Check if user's email in profile email field is concordant to the email user was registered with '''

        profile_email_field = self.element_is_present(LoginPage.PROFILE_EMAIL_FIELD_LOCATOR)
        email_value = profile_email_field.get_attribute('value')
        assert email_value ==self.user_email

    def perform_logout(self,driver):
        action = ActionChains(driver)
        action.move_to_element(self.profile_dropdown).move_to_element(self.logout_link).click().perform()
        assert self.login_link.is_displayed()