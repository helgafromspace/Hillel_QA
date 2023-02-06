
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from web_project.helpers.helper_config import get_base_url
from web_project.pages.base_page import BasePage
import time

class RegisterPage(BasePage):

    REGISTER_LINK_LOCATOR = (By.CSS_SELECTOR, 'a.b-tophead__register')
    REGISTER_FORM_LOCATOR = (By.ID, 'registration')
    INPUT_REGISTER_EMAIL_LOCATOR = (By.ID, 'email')
    INPUT_REGISTER_LOGIN_LOCATOR = (By.ID, 'name')
    INPUT_REGISTER_PASSWORD = (By.ID, 'password1')
    SUBMIT_BUTTON_LOCATOR = (By.XPATH, "//button[@name='submit']")
    EMAIL_INVALIDITY_CHECKER_LOCATOR = (By.CSS_SELECTOR, '#result-registration-email span.string-error')
    LOGIN_INVALIDITY_CHECKER_LOCATOR = (By.CSS_SELECTOR, '#result-registration-login span.string-error')
    PASSWORD_INVALIDITY_CHECKER_LOCATOR = (By.CSS_SELECTOR,'#register-popup-errors ul li:nth-child(3)')
    EMPTY_NAME_ERROR_LOCATOR = (By.CSS_SELECTOR,'#register-popup-errors ul li:first-child')
    LOGIN_FIELD_ERROR_LOCATOR = (By.CSS_SELECTOR, '#register-popup-errors ul li:nth-child(2)')
    EMAIL_FIELD_ERROR_LOCATOR = (By.CSS_SELECTOR, '#register-popup-errors ul li:last-child')
    EMAIL_FIELD_NOTIFICATION_LOCATOR = (By.CSS_SELECTOR, '#result-registration-email span.string-error')
    LOGIN_FIELD_NOTIFICATION_LOCATOR = (By.CSS_SELECTOR,'#result-registration-login span.string-error')
    EMAIL_LABEL_LOCATOR = (By.CSS_SELECTOR,"label[for='email']")
    LOGIN_LABEL_LOCATOR = (By.CSS_SELECTOR,"label[for='name']")
    PASSWORD_LABEL_LOCATOR = (By.CSS_SELECTOR, "label[for='password1']")


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
    def input_register_login(self):
        return self.element_is_present (RegisterPage.INPUT_REGISTER_LOGIN_LOCATOR)

    @property
    def input_register_password(self):
        return self.element_is_present (RegisterPage.INPUT_REGISTER_PASSWORD)

    @property
    def submit_button(self):
        return self.element_is_present (RegisterPage.SUBMIT_BUTTON_LOCATOR)

    @property
    def email_invalidity_checker(self):
        return self.element_is_present(RegisterPage.EMAIL_INVALIDITY_CHECKER_LOCATOR)

    @property
    def login_invalidity_checker(self):
        return self.element_is_present (RegisterPage.LOGIN_INVALIDITY_CHECKER_LOCATOR)

    @property
    def password_invalidity_checker(self):
        return self.element_is_present (RegisterPage.PASSWORD_INVALIDITY_CHECKER_LOCATOR)

    @property
    def empty_name_error(self):
        return self.element_is_present (RegisterPage.EMPTY_NAME_ERROR_LOCATOR)

    @property
    def login_field_error(self):
        return self.element_is_present (RegisterPage.LOGIN_FIELD_ERROR_LOCATOR)

    @property
    def email_field_error(self):
        return self.element_is_present (RegisterPage.EMAIL_FIELD_ERROR_LOCATOR)

    @property
    def email_field_notification(self):
        return self.element_is_present (RegisterPage.EMAIL_FIELD_NOTIFICATION_LOCATOR)

    @property
    def login_field_notification(self):
        return self.element_is_present (RegisterPage.LOGIN_FIELD_NOTIFICATION_LOCATOR)
    @property
    def email_label(self):
        return self.element_is_present (RegisterPage.EMAIL_LABEL_LOCATOR)

    @property
    def login_label(self):
        return self.element_is_present (RegisterPage.LOGIN_LABEL_LOCATOR)

    @property
    def password_label(self):
        return self.element_is_present (RegisterPage.PASSWORD_LABEL_LOCATOR)

    def navigate(self):
        self.driver.get(get_base_url())

    def open_register_form(self):
        self.register_link.click()

    def register_form_has_required_fields(self):
        self.open_register_form()


    def enter_invalid_email(self,invalid_register_email):
        self.input_register_email.send_keys(invalid_register_email)
        time.sleep(5)
        self.click_submit_button()


    def enter_invalid_login(self,invalid_register_login):
        self.input_register_login.send_keys(invalid_register_login)
        time.sleep(5)
        self.click_submit_button()

    def enter_invalid_password(self,invalid_register_password):
        self.input_register_password.send_keys(invalid_register_password)
        time.sleep(5)
        self.click_submit_button()


    def click_submit_button(self):
        self.submit_button.click()

    def perform_unsuccessfull_registration_with_empty_credentials_fields(self):
        self.open_register_form()
        self.click_submit_button()
        time.sleep(3)











