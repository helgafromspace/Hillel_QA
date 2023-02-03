from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

from web_project.helpers.helpers import email_generator, login_generator, password_generator, test_register_data_writer

path = '/home/helga/Hillel_QA/drivers/chromedriver/chromedriver'

def test_user_can_go_to_register_popup_from_main(driver, register_page):
    register_page.open_register_form()

# @pytest.mark.xfail(reason="Main page doesn\'t refresh after entering credentials but creds are in base though")
def test_user_can_register_with_valid_data(driver,register_page):
    register_page.perform_successfull_registration()




