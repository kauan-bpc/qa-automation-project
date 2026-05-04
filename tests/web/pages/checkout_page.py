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
        self.wait = WebDriverWait(driver, 10)

    def fill_info(self, first_name, last_name, postal_code):
        first_name_field = self.wait.until(
            EC.element_to_be_clickable(self.LOCATORS["first_name"])
        )
        first_name_field.clear()
        first_name_field.send_keys(first_name)

        last_name_field = self.wait.until(
            EC.element_to_be_clickable(self.LOCATORS["last_name"])
        )
        last_name_field.clear()
        last_name_field.send_keys(last_name)

        postal_field = self.wait.until(
            EC.element_to_be_clickable(self.LOCATORS["postal_code"])
        )
        postal_field.clear()
        postal_field.send_keys(postal_code)

        self.driver.find_element(*self.LOCATORS["continue_btn"]).click()


class CheckoutStepTwoPage:
    LOCATORS = {
        "summary_total": (By.CLASS_NAME, "summary_total_label"),
        "finish_btn":    (By.ID, "finish"),
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_total(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LOCATORS["summary_total"])
        ).text

    def finish_order(self):
        self.driver.find_element(*self.LOCATORS["finish_btn"]).click()


class CheckoutCompletePage:
    LOCATORS = {
        "confirmation": (By.CLASS_NAME, "complete-header"),
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_confirmation_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LOCATORS["confirmation"])
        ).text