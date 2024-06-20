import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from math_formula import formula_to_math

browser = webdriver.Chrome()
try:
    url = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(url)
    magic_btn = browser.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
    magic_btn.click()
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.XPATH, "//span[contains(@id, 'input_value')]")
    x = float(x_element.text)
    y = formula_to_math(x)
    input_field = browser.find_element(By.XPATH, "//input[contains(@id, 'answer')]")
    input_field.send_keys(str(y))

    submit_btn = browser.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
    submit_btn.click()
finally:
    time.sleep(5)
    browser.quit()