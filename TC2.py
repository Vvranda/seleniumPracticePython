import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://parabank.parasoft.com/parabank/register.htm;jsessionid=DAB2BF2C03E893A2B4025A1F1A165EB7")
driver.maximize_window()

first_name = driver.find_element(By.XPATH, value="//input[@id='customer.firstName']")
first_name.send_keys('vranda')
time.sleep(2)

last_name = driver.find_element(By.XPATH, value="//input[@id='customer.lastName']")
last_name.send_keys('vvj')
time.sleep(2)

address = driver.find_element(By.XPATH, value="//input[@id='customer.address.street']")
address.send_keys('geetabhawan')
time.sleep(2)

city = driver.find_element(By.XPATH, value="//input[@id='customer.address.city']")
city.send_keys('indore')
time.sleep(2)

state = driver.find_element(By.XPATH, value="//input[@id='customer.address.state']")
state.send_keys('Madhya Pradesh')
time.sleep(2)

zip_code = driver.find_element(By.XPATH, value="//input[@id='customer.address.zipCode']")
zip_code.send_keys('452001')
time.sleep(2)

phone= driver.find_element(By.XPATH, value="//input[@id='customer.phoneNumber']")
phone.send_keys('0123654987')
time.sleep(2)

ssn = driver.find_element(By.XPATH, value="//input[@id='customer.ssn']")
ssn.send_keys('vvj123')
time.sleep(2)

user_name = driver.find_element(By.XPATH, value="//input[@id='customer.username']")
user_name.send_keys('vvj')
time.sleep(2)

password = driver.find_element(By.XPATH, value="//input[@id='customer.password']")
password.send_keys('1233')
time.sleep(2)

confirm = driver.find_element(By.XPATH, value="//input[@id='repeatedPassword']")
confirm.send_keys('1233')
time.sleep(2)
driver.close()