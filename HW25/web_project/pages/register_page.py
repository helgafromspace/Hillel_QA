from selenium.webdriver import ActionChains

from web_project.helpers.helpers import email_generator, login_generator, password_generator, User, \
    test_register_data_writer
from web_project.helpers.resources import Resources
from web_project.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time

class RegisterPage(BasePage):

    REGISTER_LINK_LOCATOR = (By.CSS_SELECTOR, 'a.b-tophead__register')
    REGISTER_FORM_LOCATOR = (By.ID, 'registration')
    INPUT_REGISTER_EMAIL_LOCATOR = (By.ID, 'email')
    EMAIL_VALIDITY_CHECKER_LOCATOR = (By.CSS_SELECTOR, '#result-registration-email span.string-ok')
    INPUT_REGISTER_LOGIN_LOCATOR = (By.ID, 'name')
    LOGIN_VALIDITY_CHECKER = (By.CSS_SELECTOR, '#result-registration-login span.string-ok')
    INPUT_REGISTER_PASSWORD = (By.ID, 'password1')
    SUBMIT_BUTTON_LOCATOR = (By.XPATH, "//button[@name='submit']")


    def __init__(self, driver: WebDriver, user_login=None, user_password=None, user_email=None):
        super().__init__(driver)
        self.user_login = user_login
        self.user_password = user_password
        self.user_email = user_email

    @property
    def register_link(self):
        return self.element_is_present (RegisterPage.REGISTER_LINK_LOCATOR)

    @property
    def register_form(self):
        return self.element_is_present (RegisterPage.REGISTER_FORM_LOCATOR)

    @property
    def input_register_email(self):
        return self.element_is_present (RegisterPage.INPUT_REGISTER_EMAIL_LOCATOR)

    @property
    def email_validity_checker(self):
        return self.element_is_present (RegisterPage.EMAIL_VALIDITY_CHECKER_LOCATOR)

    @property
    def input_register_login(self):
        return self.element_is_present (RegisterPage.INPUT_REGISTER_LOGIN_LOCATOR)

    @property
    def login_validity_checker(self):
        return self.element_is_present (RegisterPage.LOGIN_VALIDITY_CHECKER)

    @property
    def input_register_password(self):
        return self.element_is_present (RegisterPage.INPUT_REGISTER_PASSWORD)

    @property
    def submit_button(self):
        return self.element_is_present (RegisterPage.SUBMIT_BUTTON_LOCATOR)

    def navigate(self):
        self.driver.get('https://hdrezka.ag/')

    def open_register_form(self):
        self.register_link.click()

        assert self.register_form.is_displayed()

    def enter_valid_email(self):
        valid_register_email = email_generator()
        self.user_email = valid_register_email
        self.input_register_email.send_keys(valid_register_email)

        assert self.email_validity_checker.is_displayed()
        assert self.email_validity_checker.text == Resources.RegisterPage.EMAIL_VALIDITY_MESSAGE

    def enter_valid_login(self):
        valid_register_login = login_generator()
        self.user_login = valid_register_login
        self.input_register_login.send_keys(valid_register_login)

        assert self.login_validity_checker.is_displayed()
        assert self.login_validity_checker.text == Resources.RegisterPage.LOGIN_VALIDITY_MESSAGE

    def enter_valid_password(self):
        valid_register_password = password_generator()
        self.user_password = valid_register_password
        self.input_register_password.send_keys (valid_register_password)

    def enter_valid_credentials(self):
        self.enter_valid_email()
        self.enter_valid_login()
        self.enter_valid_password()
        test_register_data_writer (self.user_email, self.user_login, self.user_password)

    def click_submit_button(self):
        self.submit_button.click()

    def perform_successfull_registration(self):
        self.open_register_form ()
        self.enter_valid_credentials ()
        self.click_submit_button()
        return User(self.user_login, self.user_password, self.user_email)


