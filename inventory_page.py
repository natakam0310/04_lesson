from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_item_by_id(self, item_id):
        btn = (By.ID, f"add-to-cart-{item_id}")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(btn)).click()

    def go_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_link)).click()
