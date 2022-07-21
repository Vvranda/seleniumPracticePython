import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://petstore.octoperf.com/actions/Account.action?newAccountForm=")
driver.maximize_window()

#user information
user_id = driver.find_element(By.XPATH, value="//body[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[1]/td[2]/input[1]")
user_id.send_keys('vvj')
time.sleep(2)

new_pass = driver.find_element(By.XPATH, value="//body[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[2]/td[2]/input[1]")
new_pass.send_keys('123')
time.sleep(2)

re_pass = driver.find_element(By.XPATH, value="//body[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[3]/td[2]/input[1]")
re_pass.send_keys('123')
time.sleep(2)

#Account information
first_name = driver.find_element(By.XPATH, value="//body[1]/div[2]/div[1]/form[1]/table[2]/tbody[1]/tr[1]/td[2]/input[1]")
first_name.send_keys('V')
time.sleep(2)

last_name = driver.find_element(By.XPATH, value="//body[1]/div[2]/div[1]/form[1]/table[2]/tbody[1]/tr[2]/td[2]/input[1]")
last_name.send_keys('Vvj')
time.sleep(2)

email = driver.find_element(By.XPATH, value="//body[1]/div[2]/div[1]/form[1]/table[2]/tbody[1]/tr[3]/td[2]/input[1]")
email.send_keys('vvj@bestpeers.com')
time.sleep(2)

phone = driver.find_element(By.XPATH, value="//body[1]/div[2]/div[1]/form[1]/table[2]/tbody[1]/tr[4]/td[2]/input[1]")
phone.send_keys('0123654987')
time.sleep(2)

add_1 = driver.find_element(By.XPATH, value="//tbody/tr[5]/td[2]/input[1]")
add_1.send_keys('Bestpeers')
time.sleep(2)

add_2 = driver.find_element(By.XPATH, value="//tbody/tr[6]/td[2]/input[1]")
add_2.send_keys('electronic complex')
time.sleep(2)

city = driver.find_element(By.XPATH, value="//tbody/tr[7]/td[2]/input[1]")
city.send_keys('indore')

state = driver.find_element(By.XPATH, value="//tbody/tr[8]/td[2]/input[1]")
state.send_keys('Madhya pradesh')
time.sleep(2)

zip_code = driver.find_element(By.XPATH, value="//tbody/tr[9]/td[2]/input[1]")
zip_code.send_keys('452001')

# country = driver.find_element(By.XPATH, value="")
# country.send_keys('India')
# time.sleep(2)

driver.close()