from selenium import webdriver
import time
import math
import pyperclip

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

# Клик по кнопке
browser.find_element_by_css_selector("body > form > div > div > button").click()

# Переход на новую вкладку
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

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
time.sleep(5)

# Копирования числа из Аллерта
alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)

# Закрываем браузер после всех манипуляций
browser.quit()
