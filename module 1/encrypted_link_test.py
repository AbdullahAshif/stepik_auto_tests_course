import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    url = "http://suninjuly.github.io/find_link_text.html"
    browser.get(url)
    Math = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    partial_link = browser.find_element(By.PARTIAL_LINK_TEXT, Math)
    partial_link.click()
    input1 = browser.find_element(By.TAG_NAME, "input")  # Assuming the tag name is 'input'
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")  # Replace 'last_name' with the actual name attribute
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")  # Replace with the actual class name
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
