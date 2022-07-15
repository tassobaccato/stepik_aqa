from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/math.html")
    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    print(y)
    input_y = browser.find_element(By.ID, "answer")
    input_y.send_keys(y)
    time.sleep(2)
    robot_check_box = browser.find_element(By.ID, "robotCheckbox")
    robot_check_box.click()
    time.sleep(2)
    radio_robots_rule = browser.find_element(By.ID, "robotsRule")
    radio_robots_rule.click()
    time.sleep(2)
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    time.sleep(10)

finally:
    browser.quit()
