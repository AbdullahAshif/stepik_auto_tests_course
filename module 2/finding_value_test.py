import time
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
try:
    url = "http://suninjuly.github.io/math.html"
    browser.get(url)
    people_rdo_btn = browser.find_element(By.ID, "peopleRule")
    people_checked = people_rdo_btn.get_attribute("checked")
    print("Value of people radio: ", people_checked)
    assert people_checked == "true", "People radio is not selected by default"

finally:
    time.sleep(5)
    browser.quit()
