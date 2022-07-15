from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Выбирая селектор с классом ".second" для автотеста для первой формы, вы можете попасть в
    # следующую ситуацию: обязательное поле "Last name:" вдруг пропадёт при изменениях в продукте,
    # как это произошло во второй версии формы, и данные будут введены во второстепенное поле с
    # тем же классом. В этом случае тест пройдёт успешно, и мы не будем знать о возникшей проблеме.
    # Уникальный селектор может спасти нас в этой ситуации — тест упадёт именно в тот момент,
    # когда не обнаружит нужный элемент на странице.
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, '//input[contains(@class, "first") and @required]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '//input[contains(@class, "second") and @required]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '//input[contains(@class, "third") and @required]')
    input3.send_keys("pepik@stepik.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, "btn-default")
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
