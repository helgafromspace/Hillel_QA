from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from web_project.helpers.helpers import email_generator, login_generator, password_generator, test_register_data_writer, \
    create_registered_user

path = '/home/helga/Hillel_QA/drivers/chromedriver/chromedriver'

def test_user_can_go_to_register_popup_from_main(driver):
    driver.get('https://hdrezka.ink/')

    register_button = driver.find_element(By.CSS_SELECTOR, 'a.b-tophead__register')
    register_button.click()
    wait = WebDriverWait(driver, 5)
    register_popup = wait.until(EC.visibility_of_element_located((By.ID, 'register-popup')))
    assert register_popup.is_displayed()

    time.sleep(5)
    driver.quit()


def test_user_can_register_with_valid_data(driver):
    driver.get ('https://hdrezka.ink/')

    register_button = driver.find_element (By.CSS_SELECTOR, 'a.b-tophead__register')
    register_button.click ()
    wait = WebDriverWait (driver, 5)
    register_popup = wait.until (EC.visibility_of_element_located ((By.ID, 'register-popup')))
    assert register_popup.is_displayed ()

    valid_register_email = email_generator()
    input_register_email = driver.find_element(By.ID, 'email')
    input_register_email.send_keys(valid_register_email)
    email_validity_checker = wait.until (EC.visibility_of_element_located ((By.CSS_SELECTOR, '#result-registration-email span.string-ok')))
    assert email_validity_checker.is_displayed()
    assert email_validity_checker.text == 'Можно использовать данный email для регистрации'

    valid_register_login = login_generator()
    input_register_login = driver.find_element (By.ID, 'name')
    input_register_login.send_keys(valid_register_login)
    login_validity_checker = wait.until (EC.visibility_of_element_located ((By.CSS_SELECTOR, '#result-registration-login span.string-ok')))
    assert login_validity_checker.is_displayed ()
    assert login_validity_checker.text == 'Можно использовать данный логин для регистрации'

    valid_register_password = password_generator()
    input_register_password = driver.find_element (By.ID, 'password1')
    input_register_password.send_keys(valid_register_password)

    test_register_data_writer(valid_register_email, valid_register_login, valid_register_password)

    register_submit_button = driver.find_element(By.XPATH, "//button[@name='submit']")
    register_submit_button.submit()

    login_button = driver.find_element(By.CSS_SELECTOR, 'a.b-tophead__login')
    login_button.click()


# def test_user_can_login_from_main_page(driver):
#     data = create_registered_user()
#     valid_register_login, valid_register_password = data
#     driver.get('https://hdrezka.ink/')
#     wait = WebDriverWait (driver, 5)
#     login_button = driver.find_element(By.CSS_SELECTOR, 'a.b-tophead__login')
#     login_button.click()
#
#     login_popup = wait.until (EC.visibility_of_element_located ((By.ID, 'login-popup')))
#     assert login_popup.is_displayed ()
#
#     input_login = driver.find_element (By.ID, 'login_name')
#     input_login.send_keys(valid_register_login)
#
#     input_password_login = driver.find_element (By.ID, 'login_password')
#     input_password_login.send_keys(valid_register_password)
#
#     login_button = driver.find_element(By.CSS_SELECTOR,'#login-popup button.login_button')
#     login_button.click()
#
#     profile_dropdown = wait.until (EC.visibility_of_element_located ((By.XPATH, "//span[@class='b-tophead-dropdown'] [text()='Профиль']")))
#     assert profile_dropdown.is_displayed()
#
#     time.sleep(10)
