from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

# Заполнение текстовых полей
browser.find_element_by_css_selector("body > div > form > div > input:nth-child(2)").send_keys("Шарап")
browser.find_element_by_css_selector("body > div > form > div > input:nth-child(4)").send_keys("Адильгереев")
browser.find_element_by_css_selector("body > div > form > div > input:nth-child(6)").send_keys("sh@mail.ru")

# Загрузка файла

current_dir = os.path.abspath(r"C:\Users\admin\selenium_course")
# Верхнуюю строчку можно заменить на current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
element = browser.find_element_by_css_selector("#file")
element.send_keys(file_path)

# Клик по кнопке Submit
browser.find_element_by_css_selector("body > div > form > button").click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()
