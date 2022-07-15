from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/selects1.html")
    #browser.get("http://suninjuly.github.io/selects2.html")
    num1_element = browser.find_element(By.ID, 'num1')
    num2_element = browser.find_element(By.ID, 'num2')
    num1 = int(num1_element.text)
    num2 = int(num2_element.text)

    sum_num = str(num1 + num2)

    select = Select(browser.find_element(By.CLASS_NAME, 'custom-select'))
    select.select_by_value(sum_num)
    browser.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(5)

finally:
    browser.quit()
