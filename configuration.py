import pytest


BASE_URL = "http://selenium1py.pythonanywhere.com"
LOGIN_URL = f"{BASE_URL}/en-gb/accounts/login/"
BASKET_URL = f"{BASE_URL}/en-gb/basket/"
PRODUCT_URL = f"{BASE_URL}/catalogue/coders-at-work_207/"
ENCRYPTED_URL = "http://suninjuly.github.io/find_link_text.html"
LOGIN_TO_PRODUCT_URL = f"{BASE_URL}/en-gb/catalogue/the-city-and-the-stars_95/"
PROMO_URLS = [
    f"{BASE_URL}/catalogue/coders-at-work_207/?promo=offer0",
    f"{BASE_URL}/catalogue/coders-at-work_207/?promo=offer1",
    f"{BASE_URL}/catalogue/coders-at-work_207/?promo=offer2",
    f"{BASE_URL}/catalogue/coders-at-work_207/?promo=offer3",
    f"{BASE_URL}/catalogue/coders-at-work_207/?promo=offer4",
    f"{BASE_URL}/catalogue/coders-at-work_207/?promo=offer5",
    f"{BASE_URL}/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param(f"{BASE_URL}/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
    f"{BASE_URL}/catalogue/coders-at-work_207/?promo=offer8",
    f"{BASE_URL}/catalogue/coders-at-work_207/?promo=offer9",
]
