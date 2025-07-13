from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


chrome_options = Options()
chrome_options.add_argument("--incognito")


driver = webdriver.Chrome(service=Service(), options=chrome_options)

url = 'https://www.saucedemo.com/'
driver.get(url)

element = driver.find_element(By.ID,'user-name')
element.send_keys('problem_user')

element = driver.find_element(By.ID,'password')
element.send_keys('secret_sauce')

time.sleep(3)
element = driver.find_element(By.NAME,'login-button')
element.click()

time.sleep(5)
driver.quit()