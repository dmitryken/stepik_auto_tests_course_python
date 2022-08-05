from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("div.form-group > input:nth-child(2)")
    input1.send_keys("Dmitrii")
    input2 = browser.find_element_by_css_selector("div.form-group > input:nth-child(4)")
    input2.send_keys("Khokhlov")
    input3 = browser.find_element_by_css_selector("div.form-group > input:nth-child(6)")
    input3.send_keys("d@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "lesson2.2_step8.py"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    # case 2
    # element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    # element.send_keys("/Users/dkhokhlov/selenium_course/lesson2.2_step8.py")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:

    time.sleep(10)
    browser.quit()