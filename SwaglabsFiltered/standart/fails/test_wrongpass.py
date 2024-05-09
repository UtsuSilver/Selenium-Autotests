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
        self.driver.find_element(By.ID, 'password').send_keys('222')
        self.driver.find_element(By.ID, 'login-button').click()
        text = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3').text
        print(text)
        self.assertEqual(text, 'Epic sadface: Username and password do not match any user in this service')

if __name__ == '__main__':
    unittest.main()


