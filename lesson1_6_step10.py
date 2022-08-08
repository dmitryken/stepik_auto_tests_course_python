from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector("div.first_block > div.form-group.first_class > input")
    input1.send_keys("Dmitrii")
    input2 = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input")
    input2.send_keys("Khokhlov")
    input3 = browser.find_element_by_css_selector("div.first_block > div.form-group.third_class > input")
    input3.send_keys("d@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # xpath = "//label[contains(text(), '*')]/following-sibling::input"
    # input_list = browser.find_elements_by_xpath(xpath)
    # output_list = ['first_name', 'Last_name', 'email']
    # submit = browser.find_element_by_tag_name('button')
    #
    # for element, data in zip(input_list, output_list):
    #     element.send_keys(data)
    # submit.click()

    # css селектор: input.first:required
    # xpath селектор //input[@class ='form-control first' and @ required]
    # xpath селектор через contains // input[contains(@class , "first") and @ required]
