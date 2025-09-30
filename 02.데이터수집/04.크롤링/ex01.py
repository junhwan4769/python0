from selenium import webdriver
from selenium.webdriver.common.by import By

import time

browser = webdriver.Chrome()
browser.get('http://naver.com')

btn = browser.find_element(By.CLASS_NAME, 'MyView-module__link_login___HpHMW')

btn.click()
time.sleep(3)

browser.back()
browser.forward()
browser.refresh()

time.sleep(10)