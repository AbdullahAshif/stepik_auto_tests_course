from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.ID, "id_registration-email")
    PASSWORD1 = (By.ID, "id_registration-password1")
    PASSWORD2 = (By.ID, "id_registration-password2")
    BUTTON_SUBMIT = (By.NAME, "registration_submit")

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def login_page_is_present(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' should be in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*self.LOGIN_FORM), "Login form should be not present"

    def should_be_register_form(self):
        assert self.is_element_present(*self.REGISTRATION_FORM), "Register form should be present"

    def register_new_user(self, email, password):
        self.enter_text(*self.EMAIL, email)
        self.enter_text(*self.PASSWORD1, password)
        self.enter_text(*self.PASSWORD2, password)
        self.click_element(*self.BUTTON_SUBMIT)
