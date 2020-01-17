from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.keys import Keys

# Переменные
login = "adilgereev05@ya.ru"
password = "Ifhfgenlby1993!"
timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S')
project_name = "Автотест " + timestamp

link = "https://demomrm.sbermarketing.ru/budget/execution"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

# Авторазиция в системе
browser.find_element_by_id("email").send_keys(login)
browser.find_element_by_id("password").send_keys(password)
browser.find_element_by_css_selector("button.button__auth").click()

time.sleep(5)

# Создание проекта в бюджетировании
browser.find_element_by_css_selector("#pageContent > div > div > div > div > div > div.frontend__budget-page__budget-execution__topLine > div:nth-child(1) > a").click()
time.sleep(2)
browser.find_element_by_css_selector("input.ui-components__components__input-redesign__briefPageTheme").send_keys(project_name)
browser.find_element_by_css_selector("#react-select-2--value > div.Select-input > input").send_keys("Промо", Keys.ENTER)
browser.find_element_by_css_selector("#react-select-3--value > div.Select-input > input").send_keys("КИБ", Keys.ENTER)
browser.find_element_by_css_selector("#react-select-4--value > div.Select-input > input").send_keys("Депозитарий", Keys.ENTER)
browser.find_element_by_css_selector("#react-select-5--value > div.Select-input > input").send_keys("Шарап Магомедович", Keys.ENTER)
browser.find_element_by_css_selector("#react-select-6--value > div.Select-input > input").send_keys("Частные", Keys.ENTER)
browser.find_element_by_css_selector("#react-select-7--value > div.Select-input > input").send_keys("Сбербанк", Keys.ENTER)
browser.find_element_by_css_selector("#react-select-8--value > div.Select-input > input").send_keys("ЦА", Keys.ENTER)
browser.find_element_by_css_selector("#react-select-9--value > div.Select-input > input").send_keys("Московский", Keys.ENTER)
browser.execute_script("window.scrollBy(0, 100);") # НЕ МОГУ ВЫПОЛНИТЬ СКРОЛ!!!
browser.find_element_by_css_selector("#pageContent > div.frontend__common__router__component > div > div > div > div > div > div.ui-components__components__responsive-layout__centralContent > div > div.frontend__budget__edit-execution-budget-page__activityCard.section.activity > div > div > div > div > div > div.frontend__edit-execution-budget-page__activity-budget-card__form > div > div > div > div:nth-child(10) > div > label > div.ui-components__components__labeled-input__inputWrapper > div > div.ui-components__date-pickers-redesign__date-picker__calendarIcon > div > div.ui-components__date-pickers-redesign__date-picker__icon_normal > svg").click()

# browser.find_element_by_css_selector("").send_keys("", Keys.ENTER)

time.sleep(2)
# Закрываем браузер после всех манипуляций
browser.quit()
