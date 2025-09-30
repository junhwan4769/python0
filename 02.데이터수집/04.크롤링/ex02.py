from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import keys
import time

browser = webdriver.Chrome()
browser.get('http://naver.com')

btn = browser.find_element(By.CLASS_NAME, 'MyView-module__link_login___HpHMW')

btn.click()
time.sleep(2)

id = browser.find_element(By.ID, 'id')
id.send_keys('bjl4769')
pw = browser.find.element(By.ID, 'pw')
pw.send_keys('')
time.sleep(2)

login = browser.find_element(By.ID, 'log.login')
login.click()
time.sleep(100)
