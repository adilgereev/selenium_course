# Руководство по Selenium
# Шапка для начала работы с selenium:
from selenium import webdriver<br>
from selenium.webdriver.common.keys import Keys<br>
import time<br>
import math<br>

link = "http://suninjuly.github.io/file_input.html"<br>
browser = webdriver.Chrome()<br>
browser.maximize_window()<br>
browser.implicitly_wait(5)<br>
browser.get(link)<br>


# Методы поиска элементов по странице:
browser.find_element_by_css_selector();<br>
browser.find_element_by_css_id();<br>
browser.find_element_by_xpath();<br>
browser.find_element_by_name();<br>
browser.find_element_by_tag_name();<br>
browser.find_element_by_class_name();<br>
browser.find_element_by_link_text();<br>
browser.find_element_by_partial_link_text();<br>

<h4>Взять значение атрибута:</h4>
browser.get_attribute();

<h4>Получить содержимое тэга:</h4>
"метод поиска элкментра по странице" + .text


# Пример метода загрузки файла:
current_dir = os.path.abspath(r"C:\Users\admin\selenium_course")<br>
file_path = os.path.join(current_dir, 'file.txt')<br>
element = browser.find_element_by_css_selector("#file")<br>
element.send_keys(file_path)<br>
Строку №1 можно заменить на (если используем текущую директорию): current_dir = os.path.abspath(os.path.dirname(__file__))<br>


# Аллерты
<h4>Методы для работы с Аллертом:</h4>
alert = browser.switch_to.alert<br>
alert.accept()

<h4>Получение текста из Аллерта:</h4>
alert = browser.switch_to.alert<br>
alert_text = alert.text

<h4>Методы для работы с Конферм:</h4>
confirm = browser.switch_to.alert<br>
confirm.accept() или confirm.dismiss() - Принять или Отменить

<h4>Методы для работы с Промпт:</h4>
prompt = browser.switch_to.alert<br>
prompt.send_keys("My answer") - Ввод сообщения<br>
prompt.accept()

<h4>Копировать текст из Аллерта (конкретно для аллертов из степик):</h4>
alert = browser.switch_to.alert<br>
alert_text = alert.text<br>
addToClipBoard = alert_text.split(': ')[-1]<br>
pyperclip.copy(addToClipBoard)


# Переход на новую вкладку браузера:
browser.switch_to.window("window name")

<h4>Возвращает массив имён всех вкладок:</h4>
window_handles<br>
first_window = browser.window_handles[0] - первая вкладка<br>
new_window = browser.window_handles[1] - новая вкладка

# Библиотека expected_conditions
<h4>Данная библиотека работает после импорта:</h4>

from selenium.webdriver.common.by import By<br>
from selenium.webdriver.support.ui import WebDriverWait<br>
from selenium.webdriver.support import expected_conditions as EC


<h4>Говорим selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной:</h4>
button = WebDriverWait(browser, 5).until(<br>
    EC.element_to_be_clickable((By.ID, "verify"))<br>
)

<h4>Говорим selenium проверять в течение 12 секунд, пока цена дома не станет $100 (пример из конкретного задания).</h4>
house_price = WebDriverWait(browser, 12).until(<br>
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")<br>
)


# Полезные ссылки к первому и второму модулям:
Общее<br>
https://selenium-python.com/<br>
http://selenium-python.readthedocs.io<br>
http://chromedriver.chromium.org/getting-started﻿<br>
﻿https://www.guru99.com/selenium-tutorial.html - ﻿Туториал на английском, ориентирован на Java.﻿<br>
https://www.guru99.com/live-selenium-project.html - ﻿Можно попробовать писать автотесты для демо-сайта ﻿банка. Тоже Java.<br>
http://barancev.github.io/good-locators/ - что такое хорошие селекторы<br>
http://barancev.github.io/what-is-path-env-var/ - что за PATH переменная?<br>


Ожидания в Selenium WebDriver<br>
https://docs.seleniumhq.org/docs/04_webdriver_advanced.jsp<br>
https://selenium-python.readthedocs.io/waits.html﻿<br>
https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_condition...﻿<br>
https://stackoverflow.com/questions/15122864/selenium-wait-until-document-is-ready<br>
https://blog.codeship.com/get-selenium-to-wait-for-page-load/<br>