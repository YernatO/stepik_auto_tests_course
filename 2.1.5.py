from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    print(x)
    y = calc(x)
    print("Значение " + x)
    print("Значение " + y)
    where = browser.find_element(By.ID, "answer")
    where.send_keys(y)



    opt1 = browser.find_element(By.ID, "robotCheckbox")
    opt1.click()

    option1 = browser.find_element(By.ID, "robotsRule")
    option1.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()




finally:
    time.sleep(10)
    browser.quit()