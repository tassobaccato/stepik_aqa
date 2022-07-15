from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element(By.CLASS_NAME, "btn").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)

    def calc(x):
        return str(math.log(abs(12 * math.sin(x))))
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CLASS_NAME, "btn").click()

    time.sleep(5)
finally:
    browser.quit()
