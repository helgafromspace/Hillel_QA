from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from web_project.helpers.helpers import create_registered_user
from web_project.pages.base_page import BasePage

path = '/home/helga/Hillel_QA/drivers/chromedriver/chromedriver'

class LoginPage(BasePage):

    def __init__(self, driver: WebDriver, user_login=None, user_password=None):
        self.driver = driver
        self.user_login = user_login
        self.user_password = user_password

    @property
    def login_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'a.b-tophead__login')

    @property
    def login_popup(self):
        wait = WebDriverWait (self.driver, 5)
        return wait.until (EC.visibility_of_element_located ((By.ID, 'login-popup')))

    @property
    def input_login(self):
        return self.driver.find_element (By.ID, 'login_name')

    @property
    def input_password_login(self):
        return self.driver.find_element (By.ID, 'login_password')

    @property
    def login_button(self):
        return self.driver.find_element(By.CSS_SELECTOR,'#login-popup button.login_button')

    @property
    def profile_dropdown(self):
        wait = WebDriverWait (self.driver, 5)
        return wait.until (EC.visibility_of_element_located ((By.XPATH, "//span[@class='b-tophead-dropdown'] [text()='Профиль']")))

    @property
    def login_invalid_creds_error(self):
        wait = WebDriverWait (self.driver, 5)
        return wait.until (
            EC.visibility_of_element_located ((By.XPATH, "//ul[@id='login-popup-errors']/li[contains(text(),'Введен неверный логин или пароль.')]")))

    def navigate(self):
        self.driver.get('https://hdrezka.ag/')

    def set_registered_credentials(self):
        data = create_registered_user(self.driver)
        self.user_login, self.user_password, self.user_email = data

    def get_registered_creds(self) :
        self.set_registered_credentials ()
        return self.user_login, self.user_password, self.user_email

    def enter_login(self,login):
        return self.input_login.send_keys(login)

    def enter_password(self,password):
        return self.input_password_login.send_keys(password)

    def click_login_button(self):
        self.login_button.click()

    def perform_successful_login(self,email_flag=False, change_password=False, change_login=False):
        creds = self.get_registered_creds ()
        if change_login:
            self.user_login = creds[0] + 2* chr(randint(65,90))
        else:
            self.user_login = creds[0]
        if change_password:
            self.user_password = creds[1] + chr(randint(65,90))
        else:
            self.user_password = creds[1]
        self.user_email= creds[2]
        self.login_link.click()
        if email_flag:
            self.enter_login (self.user_email)
        else:
            self.enter_login (self.user_login)
        self.enter_password (self.user_password)
        time.sleep(5)
        self.click_login_button()
        return self


    def perform_unsuccessful_login(self, login,password,email,email_flag=False):
        self.login_link.click()
        if email_flag:
            self.enter_login(email)
        else:
            self.enter_login(login)
        self.enter_password (password)
        self.click_login_button()
        return self





