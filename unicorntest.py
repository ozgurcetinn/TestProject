import unittest
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_unicorn(self):
        driver = self.driver
        driver.get("http://unicornitems.com/my-account/")
        username = driver.find_element(By.NAME, "username")
        username.send_keys("111")

        password = driver.find_element(By.NAME, "password")
        password.send_keys("111")

        login_button = driver.find_element(By.NAME, "login")
        login_button.click()

        assert "ERROR" in driver.page_source



if __name__ == '__main__':
    unittest.main()
