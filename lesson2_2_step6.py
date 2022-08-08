from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element_by_css_selector('#input_value')
    x = x.text
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(calc(x))

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    option1 = browser.find_element_by_id('robotCheckbox').click()
    option2 = browser.find_element_by_id('robotsRule').click()
    button = browser.find_element_by_css_selector("button.btn").click()

finally:

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
