from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import datetime
from selenium.webdriver.common.keys import Keys

# Переменные
login = "adilgereev05@ya.ru"
password = "Ifhfgenlby1993!"
timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S')
project_name = "Автотест пробежал тут в " + timestamp

link = "https://demomrm.sbermarketing.ru/budget/execution"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

# Авторазиция в системе
browser.find_element_by_css_selector("#email").send_keys(login)
browser.find_element_by_css_selector("#password").send_keys(password)
browser.find_element_by_css_selector("button.button__auth").click()

time.sleep(5)

# Создание проекта в бюджетировании
browser.find_element_by_css_selector("#pageContent > div > div > div > div > div > div.frontend__budget-page__budget-execution__topLine > div:nth-child(1) > a").click()
browser.find_elements_by_css_selector(НЕ МОГУ НАЙТИ СИЭСЭС СЕЛЕКТОР!).send_keys("Автотест")

# Закрываем браузер после всех манипуляций
# browser.quit()
