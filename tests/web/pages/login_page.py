from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://www.saucedemo.com"

    locators = {
        "username": (By.ID, "user-name"),
        "password": (By.ID, "password"),
    }