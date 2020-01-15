from selenium import webdriver
import time
import math
import pyperclip

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

# Нажимаем на кнопку
browser.find_element_by_css_selector("body > form > div > div > button").click()
confirm = browser.switch_to.alert
confirm.accept()


# Вычисление требуемое на странице link
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)

# Вводим вычесленное значение в поле.
browser.find_element_by_css_selector("#answer").send_keys(y)
browser.find_element_by_css_selector("body > form > div > div > button").click()

# Ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(3)

# Копирования числа из Аллерта
alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)

# Закрываем браузер после всех манипуляций
browser.quit()
