from selenium import webdriver
import time
import math
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")


# Вычисление требуемое на странице link
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# говорим Selenium проверять в течение 12 секунд, пока цена дома не станет $100
house_price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
browser.find_element_by_id("book").click()

# Ввод вычисленного значения
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_id("solve").click()

# Ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(3)

# Копирования числа из Аллерта
alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)

# Закрываем браузер после всех манипуляций
browser.quit()
