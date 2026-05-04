from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    LOCATORS = {
        "title":       (By.CLASS_NAME, "title"),
        "add_to_cart": (By.CSS_SELECTOR, ".inventory_item:first-child button"),
        "cart_badge":  (By.CLASS_NAME, "shopping_cart_badge"),
        "cart_icon":   (By.CLASS_NAME, "shopping_cart_link"),
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LOCATORS["title"])
        ).text

    def add_first_item_to_cart(self):
        self.driver.find_element(*self.LOCATORS["add_to_cart"]).click()

    def get_cart_count(self):
        return self.driver.find_element(*self.LOCATORS["cart_badge"]).text

    def go_to_cart(self):
        self.driver.find_element(*self.LOCATORS["cart_icon"]).click()