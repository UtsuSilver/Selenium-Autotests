from selenium import webdriver
from selenium.webdriver.common.by import  By
import time

driver=webdriver.Chrome()

driver.get('https://www.saucedemo.com/')

driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
driver.find_element(By.ID, 'login-button').click()

driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select').click()
driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[1]').click()

name_elements = driver.find_elements(By.CSS_SELECTOR, '.inventory_item_name')

for name_element in name_elements:
    name_text = name_element.text
    print(f"Item Name: {name_text}")

names = [name_element.text for name_element in name_elements]

# Check if the list of names is sorted
is_sorted = all(names[i] <= names[i + 1] for i in range(len(names) - 1))

# Print the result
if is_sorted:
    print("The list of names is sorted from A to Z.")
else:
    print("The list of names is not sorted from A to Z.")

time.sleep(0)