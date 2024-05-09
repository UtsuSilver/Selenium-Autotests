from selenium import webdriver
from selenium.webdriver.common.by import  By
import time

driver=webdriver.Chrome()

driver.get('https://www.saucedemo.com/')

driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
driver.find_element(By.ID, 'login-button').click()

driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select').click()
driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[4]').click()

price_elements = driver.find_elements(By.CSS_SELECTOR,'.inventory_item_price')

for i in range(len(price_elements) - 1):
    price_text1 = price_elements[i].text
    price_text2 = price_elements[i + 1].text

    price1 = float(price_text1.replace('$', '').replace(',', ''))
    price2 = float(price_text2.replace('$', '').replace(',', ''))

    print(f"Price {i + 1}: {price_text1}")
    print(f"Price {i + 2}: {price_text2}")

    if price1 > price2:
        print(f"Price {i + 1} is greater than Price {i + 2}")
    elif price1 < price2:
        print(f"Price {i + 1} is less than Price {i + 2}")
    else:
        print(f"Price {i + 1} is equal to Price {i + 2}")

