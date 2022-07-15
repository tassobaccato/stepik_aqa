from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/get_attribute.html")
    treasure = browser.find_element(By.ID, "treasure")
    treasure_valuex = treasure.get_attribute("valuex")
    x = treasure_valuex
    print(x)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    print(y)
    time.sleep(2)
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
