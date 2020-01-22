from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.keys import Keys

# Переменные
link = "https://demomrm.sbermarketing.ru/budget/execution"
login = "adilgereev05@ya.ru"
password = "Ifhfgenlby1993!"
timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%d.%m.%y / %H:%M:%S')
project_name = "Автотест " + timestamp

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

# Авторазиция в системе
browser.find_element_by_id("email").send_keys(login)
browser.find_element_by_id("password").send_keys(password)
browser.find_element_by_css_selector("button.button__auth").click()

time.sleep(4)

# Создание проекта в бюджетировании
browser.find_element_by_css_selector("#pageContent > div > div > div > div > div > div.frontend__budget-page__budget-execution__topLine > div:nth-child(1) > a").click()
time.sleep(2)
browser.find_element_by_css_selector("input.ui-components__components__input-redesign__briefPageTheme").send_keys(project_name)
browser.find_element_by_css_selector("#react-select-2--value > div.Select-input > input").send_keys("Спонсор", Keys.ENTER)
browser.find_element_by_css_selector("#react-select-3--value > div.Select-input > input").send_keys("Розничный", Keys.ENTER)
browser.find_element_by_css_selector("#react-select-4--value > div.Select-input > input").send_keys("Платежи", Keys.ENTER)
browser.find_element_by_css_selector("#react-select-5--value > div.Select-input > input").send_keys("Шарап Магомедович", Keys.ENTER)
browser.find_element_by_css_selector("#react-select-6--value > div.Select-input > input").send_keys("Массовый", Keys.ENTER)
browser.find_element_by_css_selector("#react-select-7--value > div.Select-input > input").send_keys("Сбербанк", Keys.ENTER)
browser.find_element_by_css_selector("#react-select-8--value > div.Select-input > input").send_keys("ЦА", Keys.ENTER)
browser.find_element_by_css_selector("#react-select-9--value > div.Select-input > input").send_keys("Московский", Keys.ENTER)

# Скролл
scroll1 = browser.find_element_by_css_selector('div.ui-components__date-pickers-redesign__date-picker__icon_normal > svg')
browser.execute_script('arguments[0].scrollIntoView(true);', scroll1)

# Заполнение строки
browser.find_element_by_css_selector("div.frontend__budget-list__budget-card__form > div > div > div > div:nth-child(1) > div > label > div > div > input").send_keys("Проект №1")
browser.find_element_by_css_selector("#react-select-10--value > div.Select-input > input").send_keys("Медиа", Keys.ENTER)
browser.find_element_by_css_selector("#react-select-11--value > div.Select-input > input").send_keys("Реклама", Keys.ENTER)

# Добавление строки
browser.find_element_by_css_selector("div.frontend__edit-execution-budget-page__budget-list__createButton > div").click()
browser.find_element_by_css_selector("div.frontend__edit-execution-budget-page__budget-list__budgetCard.section.budget1 > div > div > div > div > div > div.frontend__budget-list__budget-card__form > div > div > div > div:nth-child(1) > div > label > div > div > input").send_keys("Проект №2")
browser.find_element_by_css_selector("#react-select-14--value > div.Select-input > input").send_keys("Медиа", Keys.ENTER)
browser.find_element_by_css_selector("#react-select-15--value > div.Select-input > input").send_keys("Реклама", Keys.ENTER)

scroll2 = browser.find_element_by_css_selector('div.frontend__edit-execution-budget-page__budget-list__createButton > div')
browser.execute_script('arguments[0].scrollIntoView(true);', scroll2)

# Сохранение проекта
browser.find_element_by_css_selector("div.ui-components__components__responsive-layout__rightSidebar > div > div > div > div").click()

time.sleep(3)
# Закрываем браузер после всех манипуляций
browser.quit()
