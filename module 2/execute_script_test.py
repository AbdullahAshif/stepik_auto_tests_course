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
    browser = webdriver.Chrome()
    url = "https://SunInJuly.github.io/execute_script.html"
    browser.get(url)

    x_element = browser.find_element(By.XPATH, "//span[contains(@id, 'input_value')]")
    x = float(x_element.text)
    y = formula_to_math(x)

    button = browser.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    input_field = browser.find_element(By.XPATH, "//input[contains(@id, 'answer')]")
    input_field.send_keys(str(y))

    robot_checkbox = browser.find_element(By.XPATH, "//input[contains(@id, 'robotCheckbox')]")
    robot_checkbox.click()

    robot_rdo_btn = browser.find_element(By.XPATH, "//input[contains(@id, 'robotsRule')]")
    browser.execute_script("arguments[0].click();", robot_rdo_btn)

    time.sleep(1)
    browser.execute_script("arguments[0].click();", button)

finally:
    time.sleep(5)
    browser.quit()
