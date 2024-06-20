import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    url = "http://suninjuly.github.io/find_xpath_form.html"
    browser.get(url)
    f_name = browser.find_element(By.XPATH, "//input[contains(@name, 'first_name')]")
    l_name = browser.find_element(By.XPATH, "//input[contains(@name, 'last_name')]")
    city = browser.find_element(By.XPATH, "//input[contains(@class, 'city')]")
    country = browser.find_element(By.XPATH, "//input[contains(@id, 'country')]")
    submit_btn = browser.find_element(By.XPATH, "//button[contains(@type, 'submit')]")
    f_name.send_keys("Ivan")
    l_name.send_keys("Petrov")
    city.send_keys("Smolensk")
    country.send_keys("Russia")
    submit_btn.click()

finally:
    time.sleep(10)
    browser.quit()
    