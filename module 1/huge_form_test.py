import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    url = "http://suninjuly.github.io/huge_form.html"
    browser.get(url)
    elements = browser.find_elements(By.XPATH, "//input[contains(@type, 'text')]")
    for element in elements:
        element.send_keys("abc")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
