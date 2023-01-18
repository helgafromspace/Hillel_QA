from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = '/drivers/chromedriver/chromedriver'

driver = Chrome(service=Service(path))
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://store.ababahalamaha.com.ua/')

new_arrivals = driver.find_element(By.LINK_TEXT, 'Нові видання')
new_arrivals.screenshot('locator_arrivals_css.png')

header = driver.find_element(By.TAG_NAME, 'header')
header.screenshot('locator_header_css.png')

telephone_number = driver.find_element(By.CSS_SELECTOR, "header div.widget>span.header-telephones")
telephone_number.screenshot('locator_tel_css.png')

badge = driver.find_element(By.CSS_SELECTOR, 'li>.badge')
badge.screenshot('locator_badge_css.png')

search_field = driver.find_element(By.CSS_SELECTOR, 'header input.ant-input')
search_field.screenshot('locator_search_field_css.png')

books_collection = driver.find_element(By.CSS_SELECTOR, 'a ul.nav')
books_collection.screenshot('locator_collection_css.png')

driver.quit()

