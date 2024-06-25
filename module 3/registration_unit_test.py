import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_registration1(self):
        url = "http://suninjuly.github.io/registration1.html"
        self.browser.get(url)
        first_name = self.browser.find_element(By.XPATH, "//input[contains(@class, 'form-control first') "
                                                         "and @placeholder='Input your first name']")
        last_name = self.browser.find_element(By.XPATH, "//input[contains(@class, 'form-control second') "
                                                        "and @placeholder='Input your last name']")
        email = self.browser.find_element(By.XPATH, "//input[contains(@class, 'form-control third') "
                                                    "and @placeholder='Input your email']")
        phone = self.browser.find_element(By.XPATH, "//input[contains(@class, 'form-control first') "
                                                    "and @placeholder='Input your phone:']")
        address = self.browser.find_element(By.XPATH, "//input[contains(@class, 'form-control second') "
                                                      "and @placeholder='Input your address:']")
        button = self.browser.find_element(By.XPATH, "//button[contains(@class, 'btn-default')]")
        first_name.send_keys("Ivan")
        last_name.send_keys("Petrov")
        email.send_keys("ivanpetrov@gmail.com")
        phone.send_keys("+8801601447774")
        address.send_keys("Smolensk")
        button.click()
        time.sleep(1)
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1")
        text = welcome_text.text
        self.assertEqual("Congratulations! You have successfully registered!", text)

    def test_registration2(self):
        url = "http://suninjuly.github.io/registration2.html"
        self.browser.get(url)
        first_name = self.browser.find_element(By.XPATH, "//input[contains(@class, 'form-control first') "
                                                         "and @placeholder='Input your first name']")
        last_name = self.browser.find_element(By.XPATH, "//input[contains(@class, 'form-control second') "
                                                        "and @placeholder='Input your last name']")
        email = self.browser.find_element(By.XPATH, "//input[contains(@class, 'form-control third') "
                                                    "and @placeholder='Input your email']")
        phone = self.browser.find_element(By.XPATH, "//input[contains(@class, 'form-control first') "
                                                    "and @placeholder='Input your phone:']")
        address = self.browser.find_element(By.XPATH, "//input[contains(@class, 'form-control second') "
                                                      "and @placeholder='Input your address:']")
        button = self.browser.find_element(By.XPATH, "//button[contains(@class, 'btn-default')]")
        first_name.send_keys("Ivan")
        last_name.send_keys("Petrov")
        email.send_keys("ivanpetrov@gmail.com")
        phone.send_keys("+8801601447774")
        address.send_keys("Smolensk")
        button.click()
        time.sleep(1)
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1")
        text = welcome_text.text
        self.assertEqual("Congratulations! You have successfully registered!", text)


if __name__ == "__main__":
    unittest.main()
