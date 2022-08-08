from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element_by_css_selector("img").get_attribute("valuex")
    browser.find_element_by_id('answer').send_keys(calc(x))

    option1 = browser.find_element_by_id('robotCheckbox').click()
    option2 = browser.find_element_by_id('robotsRule').click()
    button = browser.find_element_by_css_selector("button.btn").click()

finally:

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла