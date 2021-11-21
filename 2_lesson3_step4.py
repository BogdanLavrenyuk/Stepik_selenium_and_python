from selenium import webdriver
import math
import time
import os

from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("btn")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()

    value=browser.find_element_by_id("input_value").text
    print(value)

    answer = math.log(abs(12 * math.sin(int(value))))

    input=browser.find_element_by_id("answer")
    input.send_keys(str(answer))
    button = browser.find_element_by_class_name("btn")
    button.click()



finally:
   print("ff")

# не забываем оставить пустую строку в конце файла