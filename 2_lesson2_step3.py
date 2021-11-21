from selenium import webdriver
import math
import time

from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    element1=int(browser.find_element_by_id("num1").text)
    element2 =int(browser.find_element_by_id("num2").text)
    answer=element1+element2

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(answer))

    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
   print("ff")

# не забываем оставить пустую строку в конце файла