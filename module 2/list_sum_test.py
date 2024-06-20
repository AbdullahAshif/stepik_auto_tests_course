import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    url = "https://suninjuly.github.io/selects1.html"
    browser.get(url)

    num1_element = browser.find_element(By.ID, 'num1')
    num2_element = browser.find_element(By.ID, 'num2')
    num1 = int(num1_element.text)
    num2 = int(num2_element.text)

    sum_result = num1 + num2

    dropdown = Select(browser.find_element(By.ID, 'dropdown'))
    dropdown.select_by_value(str(sum_result))

    submit_button = browser.find_element(By.XPATH, "//button[contains(@type, 'submit')]")
    submit_button.click()

    time.sleep(5)

finally:
    browser.quit()
