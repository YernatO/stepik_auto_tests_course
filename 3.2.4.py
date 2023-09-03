from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestRegistration(unittest.TestCase):
    def test_negative(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

    # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.first_class > input[class="form-control first"][placeholder="Input your first name"][maxlength="32"][required]')
        input1.send_keys("NAME")
        input2 = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.second_class > input[class="form-control second"][placeholder="Input your last name"][maxlength="32"][required]')
        input2.send_keys("LAST")
        input3 = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.third_class > input[class="form-control third"][placeholder="Input your email"][maxlength="32"][required]')
        input3.send_keys("you@mail.ru")
        input4 = browser.find_element(By.CSS_SELECTOR, 'div.second_block > div.form-group.first_class > input[class="form-control first"][placeholder="Input your phone:"][maxlength="32"]')
        input4.send_keys("+77778889944")
        input5 = browser.find_element(By.CSS_SELECTOR, 'div.second_block > div.form-group.second_class > input[class="form-control second"][placeholder="Input your address:"][maxlength="32"]')
        input5.send_keys("KAZ")


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
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        if "Congratulations! You have successfully registered!" == welcome_text:
        #   Congratulations! You have successfully registered!

            print('OK!')
        else:
            print('WRONG!')


    # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        browser.quit()



    def test_pozitiv(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

    # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.first_class > input[class="form-control first"][placeholder="Input your first name"][maxlength="32"][required]')
        input1.send_keys("NAME")
        input2 = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.second_class > input[class="form-control second"][placeholder="Input your last name"][maxlength="32"][required]')
        input2.send_keys("LAST")
        input3 = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.third_class > input[class="form-control third"][placeholder="Input your email"][maxlength="32"][required]')
        input3.send_keys("you@mail.ru")
        input4 = browser.find_element(By.CSS_SELECTOR, 'div.second_block > div.form-group.first_class > input[class="form-control first"][placeholder="Input your phone:"][maxlength="32"]')
        input4.send_keys("+77778889944")
        input5 = browser.find_element(By.CSS_SELECTOR, 'div.second_block > div.form-group.second_class > input[class="form-control second"][placeholder="Input your address:"][maxlength="32"]')
        input5.send_keys("KAZ")


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
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        if "Congratulations! You have successfully registered!" == welcome_text:
        #   Congratulations! You have successfully registered!
            print('OK!')
        else:
            print('WRONG!')


    # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
    
    # закрываем браузер после всех манипуляций
        browser.quit()
    



if __name__ == "__main__": 
    unittest.main()