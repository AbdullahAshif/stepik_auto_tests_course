from .base_page import BasePage
from configuration import BASE_URL

class MainPage(BasePage):
    URL = BASE_URL

    def __init__(self, browser):
        super().__init__(browser, self.URL)

    def go_to_basket(self):
        from .basket_page import BasketPage  # Lazy import to avoid circular import
        basket_link = self.find_element(*self.BASKET_LINK)
        if basket_link:
            basket_link.click()
            return BasketPage(self.browser, self.browser.current_url)
        else:
            return None

    def go_to_login_page(self):
        from .login_page import LoginPage  # Lazy import to avoid circular import
        login_link = self.find_element(*self.LOGIN_LINK)
        login_link.click()
        return LoginPage(self.browser, self.browser.current_url)
