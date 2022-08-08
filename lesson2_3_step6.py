from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/cats.html"

try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get(link)

    press_troll = browser.find_element_by_css_selector('[class="trollface btn btn-primary"]')
    button = browser.find_element_by_css_selector("button.btn").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_css_selector('#input_value')
    x = x.text
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(calc(x))

    button = browser.find_element_by_css_selector("button.btn").click()

finally:

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
