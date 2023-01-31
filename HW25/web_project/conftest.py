from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
import pytest

from web_project.pages.login_page import LoginPage

path = '/home/helga/Hillel_QA/drivers/chromedriver/chromedriver'

@pytest.fixture
def driver():
    driver = Chrome(service=Service(path))
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# @pytest.fixture
# def get_login_page(self,driver):
#     login_page = LoginPage (driver)
#     return login_page