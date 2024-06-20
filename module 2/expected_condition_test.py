import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from math_formula import formula_to_math


browser = webdriver.Chrome()
try:
    url = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(url)

    # Wait until the price drops to $100
    WebDriverWait(browser, 12).until(
        ec.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Click the book button
    button = browser.find_element(By.ID, "book")
    button.click()

    # Wait for the input field to be present before proceeding
    WebDriverWait(browser, 5).until(
        ec.presence_of_element_located((By.ID, "input_value"))
    )

    x_element = browser.find_element(By.ID, "input_value")
    x = float(x_element.text)
    y = formula_to_math(x)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(str(y))

    # Ensure the submit button is clickable before clicking
    submit_btn = WebDriverWait(browser, 5).until(
        ec.element_to_be_clickable((By.ID, "solve"))
    )
    submit_btn.click()

finally:
    # Wait to observe the result (optional)
    time.sleep(5)
    browser.quit()
