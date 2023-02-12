import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_project.helpers.helper_config import get_base_url
from web_project.helpers.resources import Resources
from web_project.pages.base_page import BasePage


class RegisterPage(BasePage):

    REGISTER_LINK_LOCATOR = (By.CSS_SELECTOR, 'a.b-tophead__register')
    REGISTER_FORM_LOCATOR = (By.ID, 'registration')
    INPUT_REGISTER_EMAIL_LOCATOR = (By.ID, 'email')
    INPUT_REGISTER_LOGIN_LOCATOR = (By.ID, 'name')
    INPUT_REGISTER_PASSWORD = (By.ID, 'password1')
    SUBMIT_BUTTON_LOCATOR = (By.XPATH, "//button[@name='submit']")
    EMAIL_INVALIDITY_CHECKER_LOCATOR = (By.CSS_SELECTOR, '#result-registration-email span.string-error')
    LOGIN_INVALIDITY_CHECKER_LOCATOR = (By.CSS_SELECTOR, '#result-registration-login span.string-error')
    REGISTER_ERROR_LIST = (By.ID, 'register-popup-errors')
    PASSWORD_INVALIDITY_CHECKER_LOCATOR = (By.CSS_SELECTOR,'#register-popup-errors ul li:nth-child(3)')
    EMPTY_NAME_ERROR_LOCATOR = (By.CSS_SELECTOR,'#register-popup-errors ul li:first-child')
    LOGIN_FIELD_ERROR_LOCATOR = (By.CSS_SELECTOR, '#register-popup-errors ul li:nth-child(2)')
    EMAIL_FIELD_ERROR_LOCATOR = (By.CSS_SELECTOR, '#register-popup-errors ul li:last-child')
    EMAIL_FIELD_NOTIFICATION_LOCATOR = (By.CSS_SELECTOR, '#result-registration-email span.string-error')
    LOGIN_FIELD_NOTIFICATION_LOCATOR = (By.CSS_SELECTOR,'#result-registration-login span.string-error')
    EMAIL_LABEL_LOCATOR = (By.CSS_SELECTOR,"label[for='email']")
    LOGIN_LABEL_LOCATOR = (By.CSS_SELECTOR,"label[for='name']")
    PASSWORD_LABEL_LOCATOR = (By.CSS_SELECTOR, "label[for='password1']")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def register_link(self):
        return self.element_is_present(RegisterPage.REGISTER_LINK_LOCATOR)

    @property
    def register_form(self):
        return self.element_is_present(RegisterPage.REGISTER_FORM_LOCATOR)

    @property
    def input_register_email(self):
        return self.element_is_present(RegisterPage.INPUT_REGISTER_EMAIL_LOCATOR)

    @property
    def input_register_login(self):
        return self.element_is_present(RegisterPage.INPUT_REGISTER_LOGIN_LOCATOR)

    @property
    def input_register_password(self):
        return self.element_is_present(RegisterPage.INPUT_REGISTER_PASSWORD)

    @property
    def submit_button(self):
        return self.element_is_present(RegisterPage.SUBMIT_BUTTON_LOCATOR)

    @property
    def email_invalidity_checker(self):
        return self.element_is_present(RegisterPage.EMAIL_INVALIDITY_CHECKER_LOCATOR)

    @property
    def login_invalidity_checker(self):
        return self.element_is_present(RegisterPage.LOGIN_INVALIDITY_CHECKER_LOCATOR)

    @property
    def password_invalidity_checker(self):
        return self.element_is_present(RegisterPage.PASSWORD_INVALIDITY_CHECKER_LOCATOR)

    @property
    def empty_name_error(self):
        return self.element_is_present(RegisterPage.EMPTY_NAME_ERROR_LOCATOR)

    @property
    def login_field_error(self):
        return self.element_is_present(RegisterPage.LOGIN_FIELD_ERROR_LOCATOR)

    @property
    def email_field_error(self):
        return self.element_is_present(RegisterPage.EMAIL_FIELD_ERROR_LOCATOR)

    @property
    def email_field_notification(self):
        return self.element_is_present(RegisterPage.EMAIL_FIELD_NOTIFICATION_LOCATOR)

    @property
    def login_field_notification(self):
        return self.element_is_present(RegisterPage.LOGIN_FIELD_NOTIFICATION_LOCATOR)
    @property
    def email_label(self):
        return self.element_is_present(RegisterPage.EMAIL_LABEL_LOCATOR)

    @property
    def login_label(self):
        return self.element_is_present(RegisterPage.LOGIN_LABEL_LOCATOR)

    @property
    def password_label(self):
        return self.element_is_present(RegisterPage.PASSWORD_LABEL_LOCATOR)

    @allure.step ('Go to main page')
    def navigate(self):
        self.driver.get(get_base_url())

    @allure.step ('Click on register_link to open the register form')
    def open_register_form(self):
        self.register_link.click()

    @allure.step ('Check if register form has required fields')
    def register_form_has_required_fields(self):
        self.open_register_form()

    @allure.step ('Enter invalid email {register_email}')
    def enter_invalid_email(self,register_email):
        self.input_register_email.send_keys(register_email)
        WebDriverWait(self.driver, 5).until(
            lambda wd: wd.find_element(*RegisterPage.EMAIL_INVALIDITY_CHECKER_LOCATOR).text == Resources.RegisterPage.EMAIL_INVALIDITY_MESSAGE)

    @allure.step ('Enter invalid login {register_login}')
    def enter_invalid_login(self,register_login):
        self.input_register_login.send_keys(register_login)
        WebDriverWait(self.driver, 5).until(
            lambda wd: wd.find_element(*RegisterPage.LOGIN_INVALIDITY_CHECKER_LOCATOR).text == Resources.RegisterPage.LOGIN_INVALIDITY_MESSAGE)

    @allure.step ('Enter invalid password {register_password}')
    def enter_invalid_password(self,register_password):
        self.input_register_password.send_keys(register_password)

    @allure.step ('Click on submit button')
    def click_submit_button(self):
        self.submit_button.click()

    @allure.step('Enter register email {email}')
    def enter_register_email(self,email):
        self.input_register_email.send_keys(email)

    @allure.step('Enter register login {login}')
    def enter_register_login(self,login):
        self.input_register_login.send_keys(login)

    @allure.step('Enter register password {password}')
    def enter_register_password(self,password):
        self.input_register_password.send_keys(password)
    def perform_successful_registration(self,user):
        self.enter_register_email(user.email)
        self.enter_register_login(user.login)
        self.enter_register_password(user.password)
        self.click_submit_button()

    def perform_unsuccessfull_registration_with_empty_credentials_fields(self):
        self.open_register_form()
        self.click_submit_button()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(RegisterPage.REGISTER_ERROR_LIST))



