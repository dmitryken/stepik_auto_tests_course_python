from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math

try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button1 = browser.find_element_by_id('book').click()

    x = browser.find_element_by_css_selector('#input_value')
    x = x.text
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(calc(x))

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button = browser.find_element_by_id('solve').click()


finally:

    time.sleep(5)
    browser.quit()

