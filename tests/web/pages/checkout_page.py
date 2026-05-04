from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutStepOnePage:
    LOCATORS = {
        "first_name":   (By.ID, "first-name"),
        "last_name":    (By.ID, "last-name"),
        "postal_code":  (By.ID, "postal-code"),
        "continue_btn": (By.ID, "continue"),
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def fill_info(self, first_name, last_name, postal_code):
        self.wait.until(EC.element_to_be_clickable(self.LOCATORS["first_name"])).send_keys(first_name)
        self.wait.until(EC.element_to_be_clickable(self.LOCATORS["last_name"])).send_keys(last_name)
        self.wait.until(EC.element_to_be_clickable(self.LOCATORS["postal_code"])).send_keys(postal_code)
        self.wait.until(EC.element_to_be_clickable(self.LOCATORS["continue_btn"])).click()


class CheckoutStepTwoPage:
    LOCATORS = {
        "summary_total": (By.CLASS_NAME, "summary_total_label"),
        "finish_btn":    (By.ID, "finish"),
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def get_total(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LOCATORS["summary_total"])
        ).text

    def finish_order(self):
        self.wait.until(EC.element_to_be_clickable(self.LOCATORS["finish_btn"])).click()


class CheckoutCompletePage:
    LOCATORS = {
        "confirmation": (By.CLASS_NAME, "complete-header"),
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def get_confirmation_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LOCATORS["confirmation"])
        ).text