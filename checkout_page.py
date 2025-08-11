from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first = (By.ID, "first-name")
        self.last = (By.ID, "last-name")
        self.postal = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_info(self, first, last, postal_code):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first)).send_keys(first)
        self.driver.find_element(*self.last).send_keys(last)
        self.driver.find_element(*self.postal).send_keys(postal_code)
        self.driver.find_element(*self.continue_btn).click()

    def get_total_amount(self):
        text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_label)).text
        return text.replace("Total: ", "").strip()
