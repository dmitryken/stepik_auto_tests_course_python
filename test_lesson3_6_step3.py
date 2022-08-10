import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math

class TestMain:

    @pytest.fixture()
    def browser(self):
        browser = webdriver.Chrome()
        yield browser
        browser.quit()

    @pytest.mark.parametrize('page_number', ['236895', '236896', '236897', '236898', '236899',
                             '236903', '236904', '236905'])
    def test_correct_message(self, browser, page_number):
        answer = str(math.log(int(time.time())))
        link = f"https://stepik.org/lesson/{page_number}/step/1"
        browser.get(link)
        browser.implicitly_wait(10)
        browser.find_element_by_tag_name('textarea').send_keys(answer)
        submit_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
            ).click()
        msg = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
        assert "Correct!" == msg, f'msg is not "Correct!", real={msg}'



