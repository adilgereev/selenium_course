from selenium import webdriver
import time
import math

# link = "http://suninjuly.github.io/find_link_text"
#
# browser = webdriver.Chrome()
# browser.get(link)
#
# formula = str(math.ceil(math.pow(math.pi, math.e)*10000))
# browser.find_element_by_link_text(formula).click()
#
#
#
#
# input1 = browser.find_element_by_tag_name("input")
# input1.send_keys("Ivan")
# input2 = browser.find_element_by_name("last_name")
# input2.send_keys("Petrov")
# input3 = browser.find_element_by_class_name("form-control.city")
# input3.send_keys("Smolensk")
# input4 = browser.find_element_by_id("country")
# input4.send_keys("Russia")
# button = browser.find_element_by_css_selector("button.btn")
# button.click()
#
# # успеваем скопировать код за 30 секунд
# time.sleep(30)
#
# browser.quit()
# # не забываем оставить пустую строку в конце файла

link = "https://stepik.org/lesson/236895/step/1"

answer = math.log(int(time.time()))
stranswer = str(answer)

browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)
browser.find_element_by_tag_name("textarea").send_keys(stranswer)
browser.find_element_by_css_selector("button.submit-submission").click()