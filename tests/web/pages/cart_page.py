from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    LOCATORS = {
        "title":        (By.CLASS_NAME, "title"),
        "cart_items":   (By.CLASS_NAME, "cart_item"),
        "checkout_btn": (By.ID, "checkout"),
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LOCATORS["title"])
        ).text

    def get_items_count(self):
        return len(self.driver.find_elements(*self.LOCATORS["cart_items"]))

    def proceed_to_checkout(self):
        self.driver.find_element(*self.LOCATORS["checkout_btn"]).click()