
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from web_project.helpers.browsers import Browser
from web_project.helpers.custom_exceptions import UnsupportedBrowserException
from web_project.helpers.helper_config import get_browser_name
from web_project.helpers.helpers import User
from web_project.pages.login_page import LoginPage
from web_project.pages.register_page import RegisterPage



@pytest.fixture(scope="session")
def browser_name():
    return get_browser_name()

@pytest.fixture
def driver(browser_name):
    if browser_name.lower() == Browser.CHROME:
        path = '/home/helga/Hillel_QA/drivers/chromedriver/chromedriver'
        driver = Chrome(service=Service(path))
        # driver = webdriver.Chrome (service=ChromeService (ChromeDriverManager ().install ()))
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
def invalid_user():
    return User('WT','12346','dhjshdks.gmail.com')



@pytest.fixture()
def valid_user(driver,register_page):
    valid_user = register_page.perform_successfull_registration()
    # following steps are performed due to page refresh problems after automatic user registration
    driver.delete_all_cookies()
    driver.refresh ()
    return valid_user

