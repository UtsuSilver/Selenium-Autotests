import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.saucedemo.com/')
        self.timeout = 10

    def tearDown(self):
        self.driver.quit()

    def test_case(self):
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()

        self.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select').click()
        self.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[4]').click()

        price_elements = self.driver.find_elements(By.CSS_SELECTOR, '.inventory_item_price')

        for i in range(len(price_elements) - 1):
            price_text1 = price_elements[i].text
            price_text2 = price_elements[i + 1].text


            price1 = float(price_text1.replace('$', '').replace(',', ''))
            price2 = float(price_text2.replace('$', '').replace(',', ''))

            print(f"Price {i + 1}: {price_text1}")
            print(f"Price {i + 2}: {price_text2}")

            time.sleep(5)

            self.assertGreaterEqual(price1, price2)


if __name__ == '__main__':
    unittest.main()


