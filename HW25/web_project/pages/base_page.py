from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def element_is_present(self,locator,timeout=5):
        return WebDriverWait (self.driver, timeout=timeout).until(EC.visibility_of_element_located(locator))

    def hidden_element_is_present(self,locator,timeout=5):
        return WebDriverWait (self.driver, timeout=timeout).until(EC.presence_of_element_located(locator))