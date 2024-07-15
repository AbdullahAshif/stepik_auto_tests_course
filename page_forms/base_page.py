from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.math_utils import click_real_url
from utils.constants import DEFAULT_TIMEOUT, MIN_TIMEOUT


class BasePage():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//a[contains(text(), 'View basket')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

    def __init__(self, browser, url, timeout=DEFAULT_TIMEOUT):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def find_element(self, how, what):
        try:
            return self.browser.find_element(how, what)
        except NoSuchElementException:
            print(f"Element {what} not found on page")
            return None

    def find_elements(self, how, what):
        try:
            return self.browser.find_elements(how, what)
        except NoSuchElementException:
            print(f"No elements found matching {what}")
            return []

    def get_element_text(self, how, what):
        element = self.find_element(how, what)
        if element:
            return element.text
        return ""

    def click_element(self, how, what):
        element = self.find_element(how, what)
        if element:
            element.click()

    def enter_text(self, how, what, text):
        element = self.find_element(how, what)
        if element:
            element.clear()
            element.send_keys(text)

    def handle_alert(self, timeout=DEFAULT_TIMEOUT):
        try:
            WebDriverWait(self.browser, timeout).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            alert.accept()
            print(f"\nAlert Text: {alert_text}")
            return alert_text
        except TimeoutException:
            print("No alert present after form submission.")
            return None

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_authorized_user(self):
        assert self.is_element_present(*self.USER_ICON), "User icon is not presented," \
                                                         " probably unauthorised user"

    def go_to_login_page(self):
        login_link = self.find_element(*self.LOGIN_LINK)
        login_link.click()

    def go_to_basket(self):
        login_link = self.find_element(*self.BASKET_LINK)
        login_link.click()

    def login_link_is_present(self):
        assert self.is_element_present(*self.LOGIN_LINK), "Login link should be present"

    def is_not_element_present(self, how, what, timeout=MIN_TIMEOUT):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            print('TimeoutException == 4 sec')
            return True
        return False

    def is_disappeared(self, how, what, timeout=MIN_TIMEOUT):
        try:
            (WebDriverWait(self.browser, timeout, 1, (TimeoutException,)).until_not
             (EC.presence_of_element_located((how, what))))
        except TimeoutException:
            return False
        return True

    def do_math_to_click_real_url(self):
        math = click_real_url()
        self.find_element(By.PARTIAL_LINK_TEXT, math).click()
