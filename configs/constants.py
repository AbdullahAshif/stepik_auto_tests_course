from enum import Enum


class Browser(Enum):
    CHROME = "chrome"
    FIREFOX = "firefox"


class AlertMessages(Enum):
    BASKET_EMPTY = "Your basket is empty. Continue shopping"


DEFAULT_TIMEOUT = 10
MIN_TIMEOUT = 4
