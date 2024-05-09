from selenium import webdriver
from selenium.webdriver.common.by import  By
import time

driver=webdriver.Chrome()

driver.get('https://www.saucedemo.com/')

driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
driver.find_element(By.ID, 'login-button').click()

driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()

time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("check")
driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('chekist')
driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('666/777')
driver.find_element(By.XPATH, '//*[@id="continue"]').click()

driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("check")
driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('chekist')
driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('666/777')
driver.find_element(By.XPATH, '//*[@id="continue"]').click()
driver.find_element(By.XPATH, '//*[@id="finish"]').click()

time.sleep(5)