from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    url = "http://suninjuly.github.io/wait1.html"
    browser.implicitly_wait(5)
    browser.get(url)
    
    button = browser.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
    button.click()
    message = browser.find_element(By.XPATH, "//div[contains(@id, 'verify_message')]")
    assert "successful" in message.text, "Message wasn't successful"

finally:
    browser.quit()
