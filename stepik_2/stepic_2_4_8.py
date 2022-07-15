from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
try:
    button = browser.find_element(By.ID, "book")
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)

    def calc(x):
        return str(math.log(abs(12 * math.sin(x))))
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "solve").click()
    time.sleep(5)

finally:
    browser.quit()
