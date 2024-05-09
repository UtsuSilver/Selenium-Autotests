import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.timeout = 10

    def test_case(self):
          wait = WebDriverWait(self.driver,self.timeout)
          wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input')))
          self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
          self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
          self.driver.find_element(By.ID, 'login-button').click()
          self.driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
          element = '//*[@id="logout_sidebar_link"]'
          wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]')))
          self.driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
          element = '/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input'
          wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input')))
          self.assertTrue(self.driver.find_element(By.XPATH, element).is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
        unittest.main