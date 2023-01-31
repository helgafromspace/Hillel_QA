from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

from web_project.helpers.helpers import create_registered_user
from web_project.pages.login_page import LoginPage



def test_user_can_login_from_main_page(driver):

    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.valid_registered_login, login_page.valid_registered_password = login_page.get_registered_creds ()

    login_page.login_link.click()

    login_page.enter_login (login_page.valid_registered_login)
    login_page.enter_password (login_page.valid_registered_password)

    login_page.click_login_button()


    assert login_page.login_popup.is_displayed ()
    assert login_page.profile_dropdown.is_displayed()