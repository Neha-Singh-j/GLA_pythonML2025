# pip install selenium
from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "https://www.amazon.com"

driver.get(url)

time.sleep(10)