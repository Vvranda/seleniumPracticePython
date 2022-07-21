import time

import By as By
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()

user_id = driver.find_element(By.XPATH, value="//body[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[1]/td[2]/input[1]")
user_id.send_keys('vvj')
time.sleep(2)

new_pass = driver.find_element(By.XPATH, value="//body[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[2]/td[2]/input[1]")
new_pass.send_keys('123')
time.sleep(2)

first_name = driver.find_element(By.XPATH, value="//body/section[@id='section']/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]")
first_name.send_keys('V')
time.sleep(2)

last_name = driver.find_element(By.XPATH, value="//body/section[@id='section']/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/input[1]")
last_name.send_keys('Vvj')
time.sleep(2)

driver.close()