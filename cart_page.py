from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        """Конструктор для класса Корзина"""
        self.driver = driver
        self.checkout_btn = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")

    def is_item_in_cart(self, partial_name):
        """Проверяет есть ли указанный товар в корзине"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.cart_items))
        items = [el.text for el in self.driver.find_elements(*self.cart_items)]
        return any(partial_name in text for text in items)

    def checkout(self):
        """Ожидает чтоб кнопка оформления была кликабельнаи
          и выполняет по ней клик """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_btn)).click()
