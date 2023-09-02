from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    First_name = browser.find_element(By.NAME, "firstname")
    First_name.send_keys("Скуби")
    Last_name = browser.find_element(By.NAME, "lastname")
    Last_name.send_keys("Ду")
    Email = browser.find_element(By.NAME, "email")
    Email.send_keys("123@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.c, "[type='file']")
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()