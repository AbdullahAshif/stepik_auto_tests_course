import pytest
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://stepik.org/lesson/236895/step/1"


@pytest.fixture(scope="session")
def load_config():
    with open("config.json", 'r') as f:
        config = json.load(f)
        return config


@pytest.fixture(scope="session")
def wait(browser):
    return WebDriverWait(browser, 10)


def test_authorization(browser, wait, load_config):
    login = load_config['STEPIK_USERNAME']
    password = load_config['STEPIK_PASSWORD']
    browser.get(url)
    browser.implicitly_wait(5)

    login_button = browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login")
    login_button.click()

    wait.until(EC.presence_of_element_located((By.ID, 'id_login_email')))

    username_input = browser.find_element(By.ID, 'id_login_email')
    password_input = browser.find_element(By.ID, "id_login_password")

    username_input.send_keys(login)
    password_input.send_keys(password)

    password_input.send_keys(Keys.RETURN)

    wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, ".modal-dialog")), "Element wasn't visible")

    print("Login successful and pop-up disappeared.")
