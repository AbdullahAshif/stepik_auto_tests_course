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

    def fill_form(self, first_name, last_name, city, country):
        self.enter_text(*self.FIRST_NAME, first_name)
        self.enter_text(*self.LAST_NAME, last_name)
        self.enter_text(*self.CITY_NAME, city)
        self.enter_text(*self.COUNTRY_NAME, country)
        self.click_element(*self.SUBMIT_BUTTON)
