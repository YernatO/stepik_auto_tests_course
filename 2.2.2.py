from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print(x)
    where = browser.find_element(By.ID, "answer")
    y = calc(x)
    print(y)
    where.send_keys(y)

    
    opt1 = browser.find_element(By.ID, "robotCheckbox")
    opt1.click()

    browser.execute_script("window.scrollBy(0, 200);")

    option1 = browser.find_element(By.ID, "robotsRule")
    option1.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()



finally:
    time.sleep(10)
    browser.quit()