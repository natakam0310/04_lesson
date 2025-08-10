
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_purchase_flow(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_item_by_id("sauce-labs-backpack")
    inventory.add_item_by_id("sauce-labs-bolt-t-shirt")
    inventory.add_item_by_id("sauce-labs-onesie")
    inventory.go_to_cart()

    # Ждём появления alert и принимаем его
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
    except TimeoutException:
        # Если алерта нет — продолжить или логировать
        print("Alert did not appear")

    cart = CartPage(driver)
    assert cart.is_item_in_cart("Sauce Labs Backpack")
    assert cart.is_item_in_cart("Sauce Labs Bolt T-Shirt")
    assert cart.is_item_in_cart("Sauce Labs Onesie")
    cart.checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_info("Имя", "Фамилия", "12345")
    total = checkout.get_total_amount()
    assert total == "$58.29"
