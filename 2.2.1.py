from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    A = browser.find_element(By.ID, "num1")
    NUM1 = A.text
    B = browser.find_element(By.ID, "num2")
    NUM2 = B.text
    print("Значение " + NUM1)
    print("Значение " + NUM2)
    Y = int(NUM1) + int(NUM2)
    print(Y)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(str(Y))

    but = browser.find_element(By.CSS_SELECTOR, "button.btn")
    but.click()

finally:
    time.sleep(10)
    browser.quit()

