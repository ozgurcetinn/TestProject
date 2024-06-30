import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestPython(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_pypi(self):
        driver = self.driver
        driver.get("https://pypi.org")
        search_bar = driver.find_element(By.NAME, "q")
        search_bar.send_keys("selenium")
        search_bar.send_keys(Keys.ENTER)

        assert "There were no result for" not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
