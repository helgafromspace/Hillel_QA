
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

@pytest.fixture()
def valid_user(driver):
    driver.get ('https://hdrezka.ag/')

    register_button = driver.find_element (By.CSS_SELECTOR, 'a.b-tophead__register')
    register_button.click ()
    wait = WebDriverWait (driver, 5)

    register_popup = wait.until (EC.visibility_of_element_located ((By.ID, 'register-popup')))

    valid_register_email = email_generator()
    input_register_email = driver.find_element(By.ID, 'email')
    input_register_email.send_keys(valid_register_email)
    valid_register_login = login_generator()
    input_register_login = driver.find_element (By.ID, 'name')
    input_register_login.send_keys(valid_register_login)

    valid_register_password = password_generator()
    input_register_password = driver.find_element (By.ID, 'password1')
    input_register_password.send_keys(valid_register_password)

    register_submit_button = driver.find_element(By.XPATH, "//button[@name='submit']")
    register_submit_button.click()

    driver.delete_all_cookies()
    driver.refresh ()


    return User(valid_register_login, valid_register_password,valid_register_email)

