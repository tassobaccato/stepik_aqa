from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/file_input.html")
    browser.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys("Maria")
    browser.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys("Ivanova")
    browser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("maria@mail.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'stepik_2_2_8.txt')   # добавляем к этому пути имя файла
    browser.find_element(By.ID, "file").send_keys(file_path)
    browser.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(5)


finally:
    browser.quit()
