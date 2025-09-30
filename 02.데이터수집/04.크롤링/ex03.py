from selenium import webdriver
import time
import os

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True) #브라우저창이 항상 켜져있다
browser = webdriver.Chrome(options=options)

browser.maximize_window()

url = 'https://flight.naver.com'
browser.get(url)

time.sleep(3)

if not os.path.exists('data'):
    os.makedirs('data')

browser.get_screenshot_as_file('data/flight.png') #화면을 캡쳐해서 파일로 저장
browser.quit()