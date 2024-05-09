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
          self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
          self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
          self.driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]').click()
          element_not_present = EC.invisibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/a/div'))
          wait.until(element_not_present)
          self.assertTrue(element_not_present(self.driver))

          self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/button[1]').click()

          self.driver.find_element(By.NAME,
                                   'add-to-cart-sauce-labs-backpack').click()

          self.driver.find_element(By.NAME, 'remove-sauce-labs-backpack').click()

          element_not_present = EC.invisibility_of_element_located(
              (By.NAME, 'remove-sauce-labs-backpack'))
          self.assertTrue(element_not_present(self.driver))


def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()



