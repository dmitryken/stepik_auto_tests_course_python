from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

def link_t(link):
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("div.first_block > div.form-group.first_class > input").send_keys("Dmitrii")
    browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input").send_keys("Khokhlov")
    browser.find_element_by_css_selector("div.first_block > div.form-group.third_class > input").send_keys("d@gmail.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)

    return browser.find_element(By.TAG_NAME, "h1").text

class TestUniReg(unittest.TestCase):

    def test_reg1(self):

        self.assertEqual(link_t("http://suninjuly.github.io/registration1.html"),
                         'Congratulations! You have successfully registered!', 'ok')

    def test_reg2(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration2.html"),
                         'Congratulations! You have successfully registered!', 'not ok')

if __name__ == "__main__": unittest.main()
