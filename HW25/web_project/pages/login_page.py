from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_project.helpers.helpers import create_registered_user
from web_project.pages.base_page import BasePage

path = '/home/helga/Hillel_QA/drivers/chromedriver/chromedriver'

class LoginPage(BasePage):

    def __init__(self, driver: WebDriver, valid_registered_login=None, valid_registered_password = None):
        self.driver = driver
        self.valid_registered_login = valid_registered_login
        self.valid_registered_password = valid_registered_password

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


    def navigate(self):
        self.driver.get('https://hdrezka.ag/')

    def set_registered_credentials(self):
        data = create_registered_user(self.driver)
        self.valid_registered_login, self.valid_registered_password = data

    def get_registered_creds(self) :
        self.set_registered_credentials ()
        return self.valid_registered_login, self.valid_registered_password

    def enter_login(self,login):
        if not self.valid_registered_login is None:
            return self.input_login.send_keys(self.valid_registered_login)
        else:
            self.set_registered_credentials()
            return self.input_login.send_keys (self.valid_registered_login)

    def enter_password(self,password):
        if not self.valid_registered_password is None :
            return self.input_password_login.send_keys(self.valid_registered_password)
        else:
            self.set_registered_credentials()
            return self.input_login.send_keys (self.valid_registered_login)

    def click_login_button(self):
        self.login_button.click()


