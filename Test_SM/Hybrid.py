from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.keys import Keys

# Переменные
link = "https://sbermarketing.ru/budget/execution"
login = "adilgereev05@ya.ru"
password = "Ifhfgenlby1993!!"
timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%d.%m.%y / %H:%M:%S')
project_name = "Автотест " + timestamp
сomment_budget = "Перевод деняк " + timestamp

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get(link)

# Авторазиция в системе
browser.find_element_by_id("email").send_keys(login)
browser.find_element_by_id("password").send_keys(password)
browser.find_element_by_css_selector("button.button__auth").click()

# Создание проекта в бюджетировании
browser.find_element_by_css_selector("div.frontend__budget-page__budget-execution__topLine > div:nth-child(1) > a").click()
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

# Сохранение проекта
browser.find_element_by_css_selector("div.ui-components__components__responsive-layout__rightSidebar > div > div > div > div").click()


# Смена сортировки по ID Исполнения
browser.find_element_by_css_selector("div.frontend__budget-page__budget-execution__topLine > div:nth-child(1) > div:nth-child(10) > svg").click()
browser.find_element_by_css_selector("div:nth-child(3) > div > div > div.frontend__cell-types__header-dropdown-cell__title > div").click()
browser.find_element_by_css_selector("div:nth-child(2) > div.ui-components__components__checkbox-group-filter__text").click()
browser.find_element_by_css_selector("#modal-root > div").click()

# Добавление бабла из внешнего источника
browser.find_element_by_css_selector("div:nth-child(1) > div.frontend__budget-page__budget-execution__transferBudgetButton > svg").click()
browser.find_element_by_css_selector("div.frontend__budget-execution__budget-transfer-menu__transferSwitch > div > div:nth-child(3)").click()
browser.find_element_by_css_selector("div:nth-child(1) > div > div.frontend__table__line__cells > div:nth-child(22) > div > div > div").click()
browser.find_element_by_css_selector("div.frontend__budget-transfer-menu__transfer-input__input > div > input").send_keys("200000")
browser.find_element_by_css_selector("div.Select-input > input").send_keys("1", Keys.ENTER)
browser.find_element_by_css_selector("div.ui-components__components__custom-scrollbar__view > textarea").send_keys(сomment_budget)
browser.find_element_by_css_selector("div.frontend__budget-execution__budget-transfer-menu__buttons > div:nth-child(1) > div").click()

# Перевод деняк с Января в Апрель
browser.find_element_by_css_selector("div.frontend__budget-execution__budget-transfer-menu__transferSwitch > div > div:nth-child(1)").click()
browser.find_element_by_css_selector("div:nth-child(1) > div > div.frontend__table__line__cells > div:nth-child(22) > div > div > div").click()
browser.find_element_by_css_selector("div:nth-child(1) > div > div.frontend__table__line__cells > div:nth-child(33) > div > div > div").click()
browser.find_element_by_css_selector("div.frontend__budget-transfer-menu__transfer-input__input > div > input").send_keys("100000")
browser.find_element_by_css_selector("div.frontend__budget-execution__budget-transfer-menu__buttons > div:nth-child(1) > div").click()

time.sleep(3)
# Закрываем браузер после всех манипуляций
browser.quit()
