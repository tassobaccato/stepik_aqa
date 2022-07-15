from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

browser = webdriver.Chrome()
try:
    browser.get("http://SunInJuly.github.io/execute_script.html")
    x_value = browser.find_element(By.ID, "input_value")
    x = x_value.text
    print(x)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)

    input_y = browser.find_element(By.ID, "answer")
    input_y.send_keys(y)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.TAG_NAME, "button").click()

    time.sleep(5)
finally:
    browser.quit()
