import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def formula_to_math(x):
    value = 12 * math.sin(x)
    abs_value = abs(value)
    ln_value = math.log(abs_value)
    return ln_value


try:
    url = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(url)

    x_element = browser.find_element(By.XPATH, "//img[contains( @ id, 'treasure')]")
    x_value = x_element.get_attribute("valuex")
    x = float(x_value)  # Convert x to a float
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
    time.sleep(10)
    browser.quit()
