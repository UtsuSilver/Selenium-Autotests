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
        self.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[1]').click()

        name_elements = self.driver.find_elements(By.CSS_SELECTOR, '.inventory_item_name')

        for name_element in name_elements:
            name_text = name_element.text
            print(f"Item Name: {name_text}")

        names = [name_element.text for name_element in name_elements]

        is_sorted = all(names[i] <= names[i + 1] for i in range(len(names) - 1))

        self.assertTrue(is_sorted)


if __name__ == '__main__':
    unittest.main()
