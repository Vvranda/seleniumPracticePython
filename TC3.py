import time

import By as By
import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()

first_name = driver.find_element(By.XPATH, value="//body/section[@id='section']/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]")
first_name.send_keys('V')
time.sleep(2)

last_name = driver.find_element(By.XPATH, value="//body/section[@id='section']/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/input[1]")\
last_name.send_keys('Vvj')
time.sleep(2)
driver.close()