
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage
import allure

@allure.feature("Покупка товаров")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Тест процесса покупки товаров")
@allure.description("Тест проверяет полный процесс покупки от " \
"логина до проверки итоговой суммы")

def test_purchase_flow(driver):
    """Тест проверяет процесс покупки"""
    with allure.step("Открытие страницы логина и вход под пользователем"):
     login = LoginPage(driver)
     login.open()
     login.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину и переход в корзину"):
     inventory = InventoryPage(driver)
     inventory.add_item_by_id("sauce-labs-backpack")
     inventory.add_item_by_id("sauce-labs-bolt-t-shirt")
     inventory.add_item_by_id("sauce-labs-onesie")
     inventory.go_to_cart()

    cart = CartPage(driver)
    with allure.step("Проверка наличия товаров в корзине" \
    " и переход к оформлению"):
     assert cart.is_item_in_cart("Sauce Labs Backpack")
     assert cart.is_item_in_cart("Sauce Labs Bolt T-Shirt")
     assert cart.is_item_in_cart("Sauce Labs Onesie")
     cart.checkout()

    checkout = CheckoutPage(driver)
    with allure.step("Заполнение информации для оформления" \
    " и проверка итоговой суммы"):
     checkout.fill_info("Имя", "Фамилия", "12345")
     total = checkout.get_total_amount()
     assert total == "$58.29"
