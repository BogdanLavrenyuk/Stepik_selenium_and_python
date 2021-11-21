from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    element= int(browser.find_element_by_id("treasure").get_attribute("valuex"))
    print(element)
    input4 = browser.find_element_by_id("answer")
    # answer =abs(12math.sin(element))
    # print(answer)
    input4.send_keys(str(math.log(abs(12*math.sin(int(element))))))
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
   print("ff")

# не забываем оставить пустую строку в конце файла