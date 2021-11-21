from selenium import webdriver
import math
import time
import os

from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1=browser.find_element_by_name("firstname")
    input1.send_keys("Artem")
    input1 = browser.find_element_by_name("lastname")
    input1.send_keys("Artem")
    input1 = browser.find_element_by_name("email")
    input1.send_keys("Artem")

    element=browser.find_element_by_name("file")
    current_dir = os.path.abspath(os.path.dirname("D:\text"))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'f.txt')  # добавляем к этому пути имя файла
    print(file_path)
    element.send_keys(file_path)
    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
   print("ff")

# не забываем оставить пустую строку в конце фа