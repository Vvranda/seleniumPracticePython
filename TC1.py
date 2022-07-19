import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://parabank.parasoft.com/parabank/register.htm;jsessionid=DAB2BF2C03E893A2B4025A1F1A165EB7")
time.sleep(2)

full_name = driver.find_element(By.XPATH, value="//tbody/tr[1]/td[2]")
full_name.send_keys("Vranda vijay")
time.sleep(2)

email = driver.find_element(By.XPATH, value="//tbody/tr[7]/td[3]/input[1]")
email.send_keys("bestpeers@gmail.com")
time.sleep(2)

password = driver.find_element(By.XPATH, value="//tbody/tr[9]/td[3]/input[1]")
password.send_keys("1234")
time.sleep(2)

repass = driver.find_element(By.XPATH, value="//tbody/tr[11]/td[3]/input[1]")
repass.send_keys("1234")
time.sleep(2)

alt_email = driver.find_element(By.XPATH, value="//tbody/tr[1]/td[3]/input[1]")
alt_email.send_keys("vvj@bestpeers.com")
time.sleep(2)

number = driver.find_element(By.XPATH, value="//input[@id='mobno']")
number.send_keys("3216549870")
time.sleep(2)

# date of birth
day = Select(driver.find_element(By.XPATH, value="//tbody/tr[22]/td[3]/select[1]"))
day.select_by_index('4')
time.sleep(2)

month = Select(driver.find_element(By.XPATH, value="//tbody/tr[22]/td[3]/select[2]"))
month.select_by_value('06')
time.sleep(2)

year = Select(driver.find_element(By.XPATH, value="//tbody/tr[22]/td[3]/select[3]"))
year.select_by_visible_text('2001')
time.sleep(2)

female = driver.find_element(By.XPATH, value="//tbody/tr[24]/td[3]/input[2]")
female.click()
time.sleep(2)

male = driver.find_element(By.XPATH, value="//tbody/tr[24]/td[3]/input[1]")
male.click()
time.sleep(2)

country = Select(driver.find_element(By.XPATH, value="//select[@id='country']"))
country.select_by_value('99')
time.sleep(2)

city = Select(driver.find_element(By.XPATH, value="//tbody/tr[1]/td[3]/select[1]"))
city.select_by_visible_text('Agra')
time.sleep(2)
driver.close()
