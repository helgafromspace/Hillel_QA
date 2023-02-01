from random import randint

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from web_project.helpers.helpers import create_registered_user, login_generator, User
from web_project.pages.login_page import LoginPage

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
    login_page = LoginPage (driver)
    login_page.navigate()
    return login_page


@pytest.fixture(scope = 'session')
def invalid_user():
    return User('WTO','123465464','dhjshdks.gmail.com')

