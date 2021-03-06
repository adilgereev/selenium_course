from selenium import webdriver
import time
import unittest


class TestLink(unittest.TestCase):

    def test_link1(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link1)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(
            "body > div > form > div.first_block > div.form-group.first_class > input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(
            "body > div > form > div.first_block > div.form-group.second_class > input")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(
            "body > div > form > div.first_block > div.form-group.third_class > input")
        input3.send_keys("example@stepik.org")
        input4 = browser.find_element_by_css_selector(
            "body > div > form > div.second_block > div.form-group.first_class > input")
        input4.send_keys("+79261231212")
        input5 = browser.find_element_by_css_selector(
            "body > div > form > div.second_block > div.form-group.second_class > input")
        input5.send_keys("г. Москва")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_link2(self):
        link2 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link2)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(
            "body > div > form > div.first_block > div.form-group.first_class > input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(
            "body > div > form > div.first_block > div.form-group.second_class > input")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(
            "body > div > form > div.first_block > div.form-group.third_class > input")
        input3.send_keys("example@stepik.org")
        input4 = browser.find_element_by_css_selector(
            "body > div > form > div.second_block > div.form-group.first_class > input")
        input4.send_keys("+79261231212")
        input5 = browser.find_element_by_css_selector(
            "body > div > form > div.second_block > div.form-group.second_class > input")
        input5.send_keys("г. Москва")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()