import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from web_project.helpers.browsers import Browser
from web_project.helpers.custom_exceptions import UnsupportedBrowserException
from web_project.helpers.helper_config import get_browser_name, get_screenshot_directory
from web_project.helpers.user import User
from web_project.pages.login_page import LoginPage
from web_project.pages.register_page import RegisterPage
import datetime



@pytest.fixture(scope="session")
def browser_name():
    return get_browser_name()

@pytest.fixture
def driver(browser_name):
    if browser_name.lower() == Browser.CHROME:
        # path = '/home/helga/Hillel_QA/drivers/chromedriver/chromedriver'
        # driver = Chrome(service=Service(path))
        driver = webdriver.Chrome (service=ChromeService (ChromeDriverManager ().install ()))
        driver.maximize_window()
    elif browser_name.lower() == Browser.FIREFOX:
        driver = webdriver.Firefox (service=FirefoxService (GeckoDriverManager ().install ()))
    else:
        raise UnsupportedBrowserException(browser_name)
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
def unregistered_user():
    return User('WT','12346','dhjshdks.gmail.com')


@pytest.fixture()
def valid_user():
    return User('SarahDrasner','123456789','sarahdrasner@gmail.com')

@pytest.fixture()
def register_user():
    return User('SimmonsNikolessd','123456789','sasjasaksjakjsaksjalq12781218@gmail.com')


@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == 'call' and rep.failed:
        driver = item.funcargs["driver"]
        file_name = f"{item.name}_{datetime.datetime.now().strftime('%Y_%m_%d-%H_%M')}.png"
        file_path = os.path.join(get_screenshot_directory(),file_name)
        driver.save_screenshot(file_path)
        allure.attach(driver.get_screenshot_as_png(),name='Fail test', attachment_type=allure.attachment_type.PNG)