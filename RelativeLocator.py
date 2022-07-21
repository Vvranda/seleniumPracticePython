import time

from selenium import webdriver
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(2)
email = driver.find_element(By.ID, value="email")
email.send_keys("111123")
time.sleep(2)
password = driver.find_element(locate_with(By.TAG_NAME, "input").below(email))
password.send_keys("gdygdrdfjikref")

driver.quit()
