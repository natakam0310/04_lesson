
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_purchase_flow(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_item_by_id("sauce-labs-backpack")
    inventory.add_item_by_id("sauce-labs-bolt-t-shirt")
    inventory.add_item_by_id("sauce-labs-onesie")
    inventory.go_to_cart()

    cart = CartPage(driver)
    assert cart.is_item_in_cart("Sauce Labs Backpack")
    assert cart.is_item_in_cart("Sauce Labs Bolt T-Shirt")
    assert cart.is_item_in_cart("Sauce Labs Onesie")
    cart.checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_info("Имя", "Фамилия", "12345")
    total = checkout.get_total_amount()
    assert total == "$58.29"
