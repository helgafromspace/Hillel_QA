from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def element_is_present(self,locator,timeout=5):
        return WebDriverWait (self.driver, timeout=timeout).until(EC.visibility_of_element_located(locator))

    def hidden_element_is_present(self,locator,timeout=10):
        return WebDriverWait (self.driver, timeout=timeout).until(EC.presence_of_element_located(locator))

    def is_element_not_displayed(self, locator, timeout=5) :
        try:
            WebDriverWait (self.driver, timeout=timeout).until (EC.visibility_of_element_located(locator))
            is_not_displayed = False
        except TimeoutException :
            is_not_displayed = True
        return is_not_displayed


