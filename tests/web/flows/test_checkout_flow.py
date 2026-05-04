from tests.web.pages.login_page import LoginPage
from tests.web.pages.inventory_page import InventoryPage
from tests.web.pages.cart_page import CartPage
from tests.web.pages.checkout_page import CheckoutStepOnePage, CheckoutStepTwoPage, CheckoutCompletePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USUARIO = "standard_user"
SENHA = "secret_sauce"


def test_login_com_sucesso(driver):
    LoginPage(driver).open().login(USUARIO, SENHA)
    assert "inventory" in driver.current_url


def test_login_invalido(driver):
    page = LoginPage(driver).open()
    page.login("usuario_errado", "senha_errada")
    assert "Username and password do not match" in page.get_error_message()


def test_login_usuario_bloqueado(driver):
    page = LoginPage(driver).open()
    page.login("locked_out_user", "secret_sauce")
    assert "Sorry, this user has been locked out" in page.get_error_message()


def test_fluxo_completo_checkout(driver):
    LoginPage(driver).open().login(USUARIO, SENHA)

    inventory = InventoryPage(driver)
    assert inventory.get_title() == "Products"
    inventory.add_first_item_to_cart()
    assert inventory.get_cart_count() == "1"
    inventory.go_to_cart()

    cart = CartPage(driver)
    assert cart.get_title() == "Your Cart"
    assert cart.get_items_count() == 1
    cart.proceed_to_checkout()

    CheckoutStepOnePage(driver).fill_info("Joao", "Silva", "12345")

    step_two = CheckoutStepTwoPage(driver)
    assert "Total:" in step_two.get_total()
    step_two.finish_order()

    assert CheckoutCompletePage(driver).get_confirmation_text() == "Thank you for your order!"


def test_checkout_sem_preencher_campos(driver):
    LoginPage(driver).open().login(USUARIO, SENHA)
    InventoryPage(driver).add_first_item_to_cart()
    InventoryPage(driver).go_to_cart()
    CartPage(driver).proceed_to_checkout()

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "continue"))
    ).click()

    error = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )
    assert "First Name is required" in error.text