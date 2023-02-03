
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from web_project.helpers.helpers import login_generator, User, email_generator, password_generator
from web_project.pages.login_page import LoginPage
from web_project.pages.register_page import RegisterPage

path = '/home/helga/Hillel_QA/drivers/chromedriver/chromedriver'

@pytest.fixture
def driver():
    driver = Chrome(service=Service(path))
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    return login_page

@pytest.fixture
def register_page(driver):
    register_page = RegisterPage(driver)
    register_page.navigate()
    return register_page


@pytest.fixture(scope = 'session')
def invalid_user():
    return User('WTO','123465464','dhjshdks.gmail.com')



@pytest.fixture()
def valid_user(driver,register_page):
    valid_user = register_page.perform_successfull_registration()
    # following steps are performed due to page refresh problems after automatic user registration
    driver.delete_all_cookies()
    driver.refresh ()
    return valid_user

