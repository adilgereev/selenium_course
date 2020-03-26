from selenium import webdriver
import time
import math
import pytest


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"
                                  ])
def test_many_steps(driver, link):
    answer = math.log(int(time.time()))
    str_answer = str(answer)
    driver.get(link)
    time.sleep(6)
    driver.find_element_by_tag_name("textarea").send_keys(str_answer)
    driver.find_element_by_css_selector("button.submit-submission").click()
    feedback_massage = driver.find_element_by_tag_name("pre").text
    assert feedback_massage == "Correct!", "Feedback not current"
    print(feedback_massage)
