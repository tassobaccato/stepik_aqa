from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# заполняются только обязательные поля

browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
    input1.send_keys("Ivan")
    # изменен атрибут "placeholder='Input your name'"
    time.sleep(2)
    input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    input2.send_keys("Petrov")
    # отсутствует поле "last name"
    input3 = browser.find_element(By.CLASS_NAME, "form-control.third")
    input3.send_keys("ivan@mail.ru")

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
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
