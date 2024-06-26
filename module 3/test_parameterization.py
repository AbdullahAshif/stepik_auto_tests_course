import pytest
import json
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

urls = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]


@pytest.fixture(scope="session")
def load_config():
    with open("config.json", 'r') as f:
        config = json.load(f)
        return config


@pytest.fixture(scope="session")
def wait(browser):
    return WebDriverWait(browser, 10)


@pytest.fixture(scope="session", autouse=True)
def login_to_stepik(browser, wait, load_config):
    login = load_config['STEPIK_USERNAME']
    password = load_config['STEPIK_PASSWORD']

    browser.get("https://stepik.org/catalog")

    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".navbar__auth_login")))
    login_button.click()

    wait.until(EC.presence_of_element_located((By.ID, 'id_login_email')))

    username_input = browser.find_element(By.ID, 'id_login_email')
    password_input = browser.find_element(By.ID, 'id_login_password')

    username_input.send_keys(login)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal-dialog")), "Login popup did not disappear")

    # Ensure we are logged in by checking for a logout button or user profile
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar__profile")))


@pytest.fixture(scope="session")
def processed_urls():
    return set()


@pytest.mark.parametrize("url", urls)
def test_stepik_authorization_and_submission(browser, wait, url, processed_urls):
    browser.get(url)
    browser.implicitly_wait(10)

    # Check if this is the first URL being processed
    if url not in processed_urls:
        try:
            reset_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'again-btn')]")))
            reset_button.click()
            print("Reset button clicked to clear previous answer.")
            browser.implicitly_wait(5)
        except Exception as e:
            print(f"No reset button found or could not click: {e}")
        finally:
            processed_urls.add(url)

    # Wait for the answer input field to be clickable and visible
    answer_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".textarea")))

    # Scroll element into view
    browser.execute_script("arguments[0].scrollIntoView(true);", answer_input)

    # Only clear the input field if it contains text
    if answer_input.is_enabled() and answer_input.get_attribute('value'):
        answer_input.clear()

    # Calculate the answer
    answer = math.log(int(time.time() + 3.3))
    print(f"Calculated answer: {answer}")

    answer_input.send_keys(str(answer))

    # Click the "Send" button
    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
    submit_button.click()

    # Wait for feedback
    feedback = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))).text

    # Check if the feedback is "Correct!"
    assert feedback == "Correct!", f"Expected 'Correct!', but got '{feedback}'"

    print("Answer submitted and feedback verified.")
