from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

from web_project.helpers.helpers import email_generator, login_generator, password_generator, test_register_data_writer


path = '/home/helga/Hillel_QA/drivers/chromedriver/chromedriver'

def test_user_can_go_to_register_popup_from_main_page(driver, register_page):
    register_page.open_register_form()

def test_register_popup_has_required_elements_for_registration(driver, register_page):
    register_page.register_form_has_required_elements()

def test_user_can_register_with_valid_data(driver,register_page):
    register_page.perform_successfull_registration()

@pytest.mark.parametrize('email_param',['ahjhsajshj.gmail.com', ' ', 'gmail.com'])
def test_user_cant_register_with_invalid_email(driver,register_page,email_param):
    register_page.open_register_form()
    register_page.enter_invalid_email(email_param)

@pytest.mark.parametrize('login_param',['E', 'df', 'login_with_more_than_30_letters'])
def test_user_cant_register_with_invalid_login(driver,register_page,login_param):
    register_page.open_register_form()
    register_page.enter_invalid_login(login_param)

@pytest.mark.parametrize('password_param',['1', '5'])
def test_user_cant_register_with_invalid_password(driver,register_page,password_param):
    register_page.open_register_form()
    register_page.enter_invalid_password(password_param)

def test_user_cant_register_with_blank_fields(driver,register_page):
    register_page.perform_unsuccessfull_registration_with_empty_credentials_fields()






