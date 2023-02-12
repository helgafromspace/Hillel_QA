from random import randint
import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_project.pages.base_page import BasePage
from web_project.helpers.helper_config import get_base_url


path = '/home/helga/Hillel_QA/drivers/chromedriver/chromedriver'

class LoginPage(BasePage):

    LOGIN_LINK_LOCATOR = (By.CSS_SELECTOR, 'a.b-tophead__login')
    LOGIN_POP_UP_LOCATOR = (By.ID, 'login-popup')
    INPUT_LOGIN_LOCATOR = (By.ID, 'login_name')
    INPUT_PASSWORD_LOCATOR = (By.ID, 'login_password')
    LOGIN_BUTTON_LOCATOR = (By.CSS_SELECTOR,'#login-popup button.login_button')
    DROPDOWN_MENU_LOCATOR = (By.XPATH, "//span[@class='b-tophead-dropdown']")
    PROFILE_DROPDOWN_LOCATOR = (By.XPATH, "//span[@class='b-tophead-dropdown'] [text()='Профиль']")
    PROFILE_SETTINGS_LOCATOR = (By.CSS_SELECTOR,".b-tophead-dropdown li a[href*='settings']")
    LOGOUT_LINK_LOCATOR = (By.CSS_SELECTOR, ".b-tophead-dropdown li a[href*='logout']")
    LOGIN_INVALID_CREDS_ERROR_LOCATOR = (By.XPATH, "//ul[@id='login-popup-errors']/li[contains(text(),'Введен неверный логин или пароль.')]")
    PROFILE_HEADER_LOCATOR = (By.TAG_NAME,'h1')
    PROFILE_EMAIL_FIELD_LOCATOR =(By.NAME, 'email')


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

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

    @property
    def profile_page_header(self):
        return self.element_is_present(LoginPage.PROFILE_HEADER_LOCATOR)
    @property
    def dropdown_menu(self):
        return self.element_is_present (LoginPage.DROPDOWN_MENU_LOCATOR)

    @allure.step ('Go to main page')
    def navigate(self):
        self.driver.get(get_base_url())

    @allure.step ('Enter login/email {login}')
    def enter_login(self,login):
        return self.input_login.send_keys(login)

    @allure.step ('Enter password {password}')
    def enter_password(self,password):
        return self.input_password_login.send_keys(password)

    @allure.step ('Click on login button')
    def click_login_button(self):
        self.login_button.click()

    @allure.step('Click on login_link')
    def click_login_link(self):
        self.login_link.click()

    def perform_login(self,user,email_flag=False):
        self.click_login_link()
        if email_flag:
            self.enter_login(user.email)
        else:
            self.enter_login(user.login)
        self.enter_password(user.password)
        self.click_login_button()
        return self

    @allure.step ('Go to profile page')
    def go_to_profile_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.profile_dropdown).move_to_element(self.profile_settings).click().perform()

    @allure.step ('Get email in profile field')
    def get_profile_email_field(self):
        ''' Check if user's email in profile email field is concordant to the email user was registered with '''
        profile_email_field = self.element_is_present(LoginPage.PROFILE_EMAIL_FIELD_LOCATOR)
        email_value = profile_email_field.get_attribute('value')
        return email_value

    @allure.step ('Perform logout')
    def perform_logout(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.profile_dropdown).move_to_element(self.logout_link).click().perform()
