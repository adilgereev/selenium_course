from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Переменные
link = "https://sbermarketing.ru/budget/execution"
login = "adilgereev05@ya.ru"
password = "Ifhfgenlby1993!!"
timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%d.%m.%y / %H:%M:%S')
project_name = "Автотест " + timestamp
сomment_budget = "Перевод деняк " + timestamp

def zapusk():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(10)
    browser.get(link)

    def clickOnElement(selector):

        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
        ).click()

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
    browser.find_element_by_css_selector("#react-select-12--value > div.Select-input > input").send_keys("1", Keys.ENTER)
    browser.find_element_by_css_selector("#react-select-13--value > div.Select-input > input").send_keys("1", Keys.ENTER)
    # browser.find_element_by_css_selector("div:nth-child(6) > div > label > div > div > input").send_keys("Тестовое примечание!", Keys.ENTER)

    # Сохранение проекта
    browser.find_element_by_css_selector("div.ui-components__components__responsive-layout__rightSidebar > div > div > div > div").click()

    # Смена сортировки по ID Исполнения
    browser.find_element_by_css_selector('div.frontend__budget-page__budget-execution__resetViewSettingsButton.frontend__budget-page__budget-execution__strokeIcon').click()
    browser.find_element_by_css_selector('div.frontend__budget-page__budget-execution__topLine > div:nth-child(1) > div:nth-child(12)').click()
    browser.find_element_by_css_selector("div:nth-child(3) > div > div > div.frontend__cell-types__header-dropdown-cell__title > div").click()
    browser.find_element_by_css_selector("div:nth-child(2) > div.ui-components__components__checkbox-group-filter__text").click()
    browser.find_element_by_css_selector("#modal-root > div").click()

    # Добавление бабла из внешнего источника
    clickOnElement("div:nth-child(1) > div.frontend__budget-page__budget-execution__transferBudgetButton > svg")
    clickOnElement("div.frontend__budget-execution__budget-transfer-menu__transferSwitch > div > div:nth-child(3)")
    clickOnElement("div.frontend__budget-execution__table__tableBody > div > div.wrapper > div > div > div > div > div:nth-child(1) > div > div.frontend__table__line__cells > div:nth-child(25) > div > div")
    browser.find_element_by_css_selector("div.frontend__budget-transfer-menu__transfer-input__input > div > input").send_keys("200000")
    browser.find_element_by_css_selector("div.Select-input > input").send_keys("1", Keys.ENTER)
    browser.find_element_by_css_selector("div.ui-components__components__custom-scrollbar__view > textarea").send_keys(сomment_budget)
    clickOnElement("div.frontend__budget-execution__budget-transfer-menu__buttons > div:nth-child(1) > div")
    time.sleep(3)

    # Скролл к апрелю
    scroll2 = browser.find_element_by_css_selector('div:first-child > div > div.frontend__table__line__cells > div:nth-child(36) > div > div')
    browser.execute_script('arguments[0].scrollIntoViewIfNeeded(true);', scroll2)

    # Перевод деняк с Января в Апрель
    clickOnElement("div.frontend__budget-execution__budget-transfer-menu__transferSwitch > div > div:nth-child(1)")
    clickOnElement("div:nth-child(1) > div > div.frontend__table__line__cells > div:nth-child(25) > div > div")
    clickOnElement("div:first-child > div > div.frontend__table__line__cells > div:nth-child(36) > div > div")
    browser.find_element_by_css_selector("div.frontend__budget-transfer-menu__transfer-input__input > div > input").send_keys("100000")
    clickOnElement("div.frontend__budget-execution__budget-transfer-menu__buttons > div:nth-child(1) > div")
    time.sleep(3)
    clickOnElement("div.frontend__budget-execution__budget-transfer-menu__buttons > div:nth-child(2) > div")

    # Резервируем 50000 в Марте
    clickOnElement("div:nth-child(1) > div > div.frontend__table__line__cells > div:nth-child(32) > div")
    browser.find_element_by_css_selector("div:nth-child(1) > div > div.frontend__table__line__cells > div:nth-child(32) > div > div > div > input").send_keys("50000")
    clickOnElement("div.frontend__budget-page__budget-execution__topLineGroup.frontend__budget-page__budget-execution__rightColumn > div > div")
    time.sleep(3)

    # Вносим Факт 50000 в Февраль
    clickOnElement("div:nth-child(1) > div > div.frontend__table__line__cells > div:nth-child(30) > div")
    browser.find_element_by_css_selector("div:nth-child(1) > div > div.frontend__table__line__cells > div:nth-child(30) > div > div > div > input").send_keys("50000")
    clickOnElement("div.frontend__budget-page__budget-execution__topLineGroup.frontend__budget-page__budget-execution__rightColumn > div > div")
    time.sleep(4)

    # Скролл к ячейке ИФКВ
    clickOnElement("div:nth-child(1) > div > div.frontend__table__line__cells > div:nth-child(78) > div")

    clickOnElement("div:nth-child(1) > div > div.frontend__table__line__cells > div:nth-child(72) > div")
    clickOnElement("div.frontend__budget-execution__table__dropdownCellWrapper > div > div > div > div > div > div > div:nth-child(1)")
    clickOnElement("div.frontend__budget-page__budget-execution__topLineGroup.frontend__budget-page__budget-execution__rightColumn > div > div")
    time.sleep(4)

    # Меняем ячейку Порядок использования ресурсов
    clickOnElement("div:nth-child(1) > div > div.frontend__table__line__cells > div:nth-child(73) > div")
    clickOnElement("div.frontend__budget-execution__table__dropdownCellWrapper > div > div > div.wrapper > div > div > div > div:nth-child(3)")
    clickOnElement("div.frontend__budget-page__budget-execution__topLineGroup.frontend__budget-page__budget-execution__rightColumn > div > div")
    time.sleep(4)

    # Меняем ячейку Направление затрат
    clickOnElement("div:nth-child(1) > div > div.frontend__table__line__cells > div:nth-child(74) > div")
    clickOnElement("div.frontend__budget-execution__table__dropdownCellWrapper > div > div > div > div > div > div > div:nth-child(2)")
    clickOnElement("div.frontend__budget-page__budget-execution__topLineGroup.frontend__budget-page__budget-execution__rightColumn > div > div")
    time.sleep(4)

    # Меняем ячейку Подкатегория
    clickOnElement("div:nth-child(1) > div > div.frontend__table__line__cells > div:nth-child(75) > div")
    clickOnElement("div.frontend__budget-execution__table__dropdownCellWrapper > div > div > div > div > div > div > div:nth-child(1)")
    clickOnElement("div.frontend__budget-page__budget-execution__topLineGroup.frontend__budget-page__budget-execution__rightColumn > div > div")
    time.sleep(4)

    # Меняем ячейку Задача
    clickOnElement("div:nth-child(1) > div > div.frontend__table__line__cells > div:nth-child(76) > div")
    clickOnElement("div.frontend__budget-execution__table__dropdownCellWrapper > div > div > div.wrapper > div > div > div > div:nth-child(2)")
    clickOnElement("div.frontend__budget-page__budget-execution__topLineGroup.frontend__budget-page__budget-execution__rightColumn > div > div")
    time.sleep(4)

    # Вводим данные в ячейку Номер ЗНС из САП
    clickOnElement("div:nth-child(1) > div > div.frontend__table__line__cells > div:nth-child(77) > div")
    browser.find_element_by_css_selector("div.frontend__table__line__cells > div:nth-child(77) > div > div > div > input").send_keys("1234567890, 0123456789")
    clickOnElement("div.frontend__budget-page__budget-execution__topLineGroup.frontend__budget-page__budget-execution__rightColumn > div > div")
    time.sleep(4)

    scroll3 = browser.find_element_by_css_selector('div:nth-child(1) > div > div.frontend__table__line__cells > div:nth-child(79) > div')
    browser.execute_script('arguments[0].scrollIntoViewIfNeeded(true);', scroll3)

    # Вводим данные в ячейку Номер корректировки из САП
    clickOnElement("div:nth-child(1) > div > div.frontend__table__line__cells > div:nth-child(78) > div")
    browser.find_element_by_css_selector("div.frontend__table__line__cells > div:nth-child(78) > div > div > div > input").send_keys("1234567890, 0123456789")
    clickOnElement("div.frontend__budget-page__budget-execution__topLineGroup.frontend__budget-page__budget-execution__rightColumn > div > div")
    time.sleep(4)

    # Вводим данные в ячейку В примечания
    clickOnElement("div:nth-child(1) > div > div.frontend__table__line__cells > div:nth-child(79) > div")
    browser.find_element_by_css_selector("div.frontend__table__line__cells > div:nth-child(79) > div > div > div > input").send_keys('Очень большой текст, с числами 0123456789 и различными символами !@№;%:?*()_+')
    clickOnElement("div.frontend__budget-page__budget-execution__topLineGroup.frontend__budget-page__budget-execution__rightColumn > div > div")

    time.sleep(3)
    # Закрываем браузер после всех манипуляций
    browser.quit()


while True:
    zapusk()