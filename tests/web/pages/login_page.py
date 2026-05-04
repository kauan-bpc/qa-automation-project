from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://www.saucedemo.com"

    LOCATORS = {
        "username":  (By.ID, "user-name"),
        "password":  (By.ID, "password"),
        "login_btn": (By.ID, "login-button"),
        "error_msg": (By.CSS_SELECTOR, "[data-test='error']"),
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        return self

    def login(self, username, password):
        self.driver.find_element(*self.LOCATORS["username"]).send_keys(username)
        self.driver.find_element(*self.LOCATORS["password"]).send_keys(password)
        self.driver.find_element(*self.LOCATORS["login_btn"]).click()

    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LOCATORS["error_msg"])
        ).text