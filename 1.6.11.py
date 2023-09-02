from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.first_class > input[type="text"][class="form-control first"][placeholder="Input your name"][maxlength="32"][required]')
    input1.send_keys("NAME")
    input2 = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.third_class > input[type="text"][class="form-control third"][placeholder="Input your email"][maxlength="32"][required]')
    input2.send_keys("you@mail.ru")
    input3 = browser.find_element(By.CSS_SELECTOR, 'div.second_block > div.form-group.first_class > input[type="text"][class="form-control first"][placeholder="Input your phone"][maxlength="32"]')
    input3.send_keys("+77778886655")
    input4 = browser.find_element(By.CSS_SELECTOR, 'div.second_block > div.form-group.third_class > input[type="text"][class="form-control second"][placeholder="Input your address"][maxlength="32"]')
    input4.send_keys("KAZ")


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()