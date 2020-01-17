from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)


# Вычисление требуемое на странице link
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element_by_css_selector("#treasure")
x = x_element.get_attribute("valuex")
y = calc(x)


# Ввод вычесленного значения в input
input = browser.find_element_by_css_selector("#answer")
input.send_keys(y)
checkbox = browser.find_element_by_css_selector("#robotCheckbox")
checkbox.click()
radiobutton = browser.find_element_by_css_selector("#robotsRule")
radiobutton.click()

button = browser.find_element_by_css_selector("body > div > form > div > div > button")
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
