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
        self.driver.find_element(By.ID, 'user-name').send_keys('locked_out_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()
        error_message = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3').text
        self.assertEqual(error_message, 'Epic sadface: Sorry, this user has been locked out.')


if __name__ == '__main__':
    unittest.main()


