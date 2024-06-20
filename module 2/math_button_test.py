import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from math_formula import formula_to_math


browser = webdriver.Chrome()
try:
    url = "http://suninjuly.github.io/math.html"
    browser.get(url)

    x_element = browser.find_element(By.XPATH, "//span[contains(@id, 'input_value')]")
    x = float(x_element.text)  # Convert x to a float
    y = formula_to_math(x)

    input_field = browser.find_element(By.XPATH, "//input[contains(@id, 'answer')]")
    input_field.send_keys(str(y))  # Send the computed y value

    robot_checkbox = browser.find_element(By.XPATH, "//input[contains(@id, 'robotCheckbox')]")
    robot_checkbox.click()

    robot_rdo_btn = browser.find_element(By.XPATH, "//input[contains(@id, 'robotsRule')]")
    robot_rdo_btn.click()

    submit_btn = browser.find_element(By.XPATH, "//button[contains(@class, 'btn-default')]")
    submit_btn.click()

finally:
    time.sleep(30)
    browser.quit()
