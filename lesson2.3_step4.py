from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get(link)

    alert = browser.find_element_by_css_selector('[class="btn btn-primary"]')
    button = browser.find_element_by_css_selector("button.btn").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_css_selector('#input_value')
    x = x.text
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(calc(x))

    button = browser.find_element_by_css_selector("button.btn").click()

finally:

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
