from selenium import webdriver
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

# Находим сумму элементов
x = browser.find_element_by_css_selector("#num1").text
y = browser.find_element_by_css_selector("#num2").text

xy = str(int(x) + int(y))


# Находим дроп даун и элемент дропдауна по сумме "xy"
dropdown1 = browser.find_element_by_tag_name("select").click()
element = browser.find_element_by_css_selector(f"[value='{xy}']").click()
clock = browser.find_element_by_css_selector("body > div > form > button").click()


# Ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()
