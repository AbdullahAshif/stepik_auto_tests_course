from selenium.webdriver.common.by import By
from page_forms.base_page import BasePage


class EncryptedLink(BasePage):
    FIRST_NAME = (By.XPATH, "//*[contains(@name, 'first_name')]")
    LAST_NAME = (By.XPATH, "//*[contains(@name, 'last_name')]")
    CITY_NAME = (By.XPATH, "//*[contains(@class, 'form-control city')]")
    COUNTRY_NAME = (By.XPATH, "//*[contains(@id, 'country')]")
    SUBMIT_BUTTON = (By.XPATH, "//*[contains(@class, 'btn btn-default')]")

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def fill_form(self):
        self.enter_text(*self.FIRST_NAME, "Ivan")
        self.enter_text(*self.LAST_NAME, "Petrov")
        self.enter_text(*self.CITY_NAME, "Smolensk")
        self.enter_text(*self.COUNTRY_NAME, "Russia")
        self.click_element(*self.SUBMIT_BUTTON)
