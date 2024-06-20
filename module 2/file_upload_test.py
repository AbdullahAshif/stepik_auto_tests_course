import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    url = "https://suninjuly.github.io/file_input.html"
    browser.get(url)

    __first_name = "Abdullah-Al-"
    __last_name = "Moinur Rashid Ashif"
    __email = "imotemph@gmail.com"

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'bio.txt')

    first_name = browser.find_element(By.XPATH, "//input[contains(@name, 'firstname')]")
    first_name.send_keys(__first_name)

    last_name = browser.find_element(By.XPATH, "//input[contains(@name, 'lastname')]")
    last_name.send_keys(__last_name)

    email = browser.find_element(By.XPATH, "//input[contains(@name, 'email')]")
    email.send_keys(__email)

    choose_file = browser.find_element(By.XPATH, "//input[contains(@id, 'file')]")
    choose_file.send_keys(file_path)

    button = browser.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
