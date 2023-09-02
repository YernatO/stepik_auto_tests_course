from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)  


    button = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = driver.find_element(By.ID, "book")
    button.click()

    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text
    print(x)
    where = driver.find_element(By.ID, "answer")
    y = calc(x)
    print(y)
    where.send_keys(y)

    button2 = driver.find_element(By.ID, "solve")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    button2.click()

finally:
    time.sleep(5)
    driver.quit()