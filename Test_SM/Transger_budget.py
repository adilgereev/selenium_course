from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.keys import Keys

# Переменные
link = "https://demomrm.sbermarketing.ru/budget/execution"
login = "adilgereev05@ya.ru"
password = "Ifhfgenlby1993!"
timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%d.%m.%y / %H:%M:%S')
сomment_budget = "Перевод деняк " + timestamp

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

# Авторазиция в системе
browser.find_element_by_id("email").send_keys(login)
browser.find_element_by_id("password").send_keys(password)
browser.find_element_by_css_selector("button.button__auth").click()

time.sleep(5)

# Смена сортировки по ID Исполнения
browser.find_element_by_css_selector("div.frontend__budget-page__budget-execution__topLine > div:nth-child(1) > div:nth-child(10) > svg").click()
browser.find_element_by_css_selector("div:nth-child(3) > div > div > div.frontend__cell-types__header-dropdown-cell__title > div").click()
browser.find_element_by_css_selector("div:nth-child(2) > div.ui-components__components__checkbox-group-filter__text").click()
browser.find_element_by_css_selector("#modal-root > div").click()

# Добавление бабла
browser.find_element_by_css_selector("#pageContent > div > div > div > div > div > div.frontend__budget-page__budget-execution__topLine > div:nth-child(1) > div.frontend__budget-page__budget-execution__transferBudgetButton > svg").click()
browser.find_element_by_css_selector("div.frontend__budget-execution__budget-transfer-menu__transferSwitch > div > div:nth-child(3)").click()
browser.find_element_by_css_selector("div:nth-child(1) > div > div.frontend__table__line__cells > div:nth-child(22) > div > div > div").click()
browser.find_element_by_css_selector("div.frontend__budget-transfer-menu__transfer-input__input > div > input").send_keys("100000")
browser.find_element_by_css_selector("div.Select-input > input").send_keys("1", Keys.ENTER)
browser.find_element_by_css_selector("div.ui-components__components__custom-scrollbar__view > textarea").send_keys(сomment_budget)
browser.find_element_by_css_selector("div.frontend__budget-execution__budget-transfer-menu__buttons > div:nth-child(1) > div").click()

time.sleep(3)
# Закрываем браузер после всех манипуляций
browser.quit()
