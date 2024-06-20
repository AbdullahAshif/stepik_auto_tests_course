import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    url = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(url)
    first_name = browser.find_element(By.XPATH, "//input[contains(@class, 'form-control first') "
                                                "and @placeholder='Input your first name']")
    last_name = browser.find_element(By.XPATH, "//input[contains(@class, 'form-control second') "
                                               "and @placeholder='Input your last name']")
    email = browser.find_element(By.XPATH, "//input[contains(@class, 'form-control third') "
                                           "and @placeholder='Input your email']")
    phone = browser.find_element(By.XPATH, "//input[contains(@class, 'form-control first') "
                                           "and @placeholder='Input your phone:']")
    address = browser.find_element(By.XPATH, "//input[contains(@class, 'form-control second') "
                                             "and @placeholder='Input your address:']")
    button = browser.find_element(By.XPATH, "//button[contains(@class, 'btn-default')]")
    first_name.send_keys("Ivan")
    last_name.send_keys("Petrov")
    email.send_keys("ivanpetrov@gmail.com")
    phone.send_keys("+8801601447774")
    address.send_keys("Smolensk")
    button.click()
    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1")
    text = welcome_text.text

    assert "Congratulations! You have successfully registered!" == text

finally:
    time.sleep(10)
    browser.quit()
