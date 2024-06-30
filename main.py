from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Chrome()
driver.maximize_window()
'''
driver.get("https://www.google.com")
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "q")))

search_bar = driver.find_element(By.NAME, "q")

# search_bar_class = driver.find_element(By.CLASS_NAME, "gLFyf")

search_bar.send_keys("Godzilla")
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "btnK")))

search_button = driver.find_element(By.NAME, "btnK")
search_button.click()
'''
driver.get("https://atilsamancioglu.com")

WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div[1]/div[3]/nav/div/ul/li[3]/a")))
blog_page = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div[3]/nav/div/ul/li[3]/a")
blog_page.click()

WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "button")))

read_button = driver.find_element(By.CLASS_NAME, "button")
read_button.click()

WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/aside[4]")))
archive = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/aside[4]")
print(len(archive.text.splitlines()))

while True:
    continue


