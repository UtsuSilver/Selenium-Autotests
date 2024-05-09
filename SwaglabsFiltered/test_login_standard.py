import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        time.sleep(2)

    def test_case(self):
          self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
          self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input').send_keys("secret_sauce")
          self.driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[1]/div/div/form/input').click()
          current_url = self.driver.current_url
          self.assertEqual(current_url, "https://www.saucedemo.com/inventory.html")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

