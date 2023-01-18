from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = '/drivers/chromedriver/chromedriver'

driver = Chrome(service=Service(path))
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://store.ababahalamaha.com.ua/')

new_arrivals = driver.find_element(By.XPATH, '//header/section[2]/ul/li/a')
new_arrivals.screenshot('locator_arrivals_xpath.png')

header = driver.find_element(By.XPATH, '//header')
header.screenshot('locator_header_xpath.png')

telephone_number = driver.find_element(By.XPATH, "//span[@class='header-telephones']")
telephone_number.screenshot('locator_tel_xpath.png')

badge = driver.find_element(By.XPATH, "//li/div[@class='badge']")
badge.screenshot('locator_badge_xpath.png')
#
search_field = driver.find_element(By.XPATH, "descendant::header//input[@class='ant-input']")
search_field.screenshot('locator_search_field_xpath.png')
#
books_collection = driver.find_element(By.XPATH, "//header/section[2]/div/a/ul[@class='nav']")
books_collection.screenshot('locator_collection_xpath.png')
#
# driver.quit()

