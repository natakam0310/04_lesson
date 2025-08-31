from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Адрес страницы калькулятора"""
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        """Конструктор класса Калькулятор"""
        self.driver = driver

    def open(self):
        """Открывает страницу калькулятора"""
        self.driver.get(self.URL)

    def enter_delay(self, value):
        """Устанавливает задержку для выполнения
         операции на калькуляторе"""
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(value))

    def click_element(self):
        """Показывает список кнопок на которые нужно нажать"""
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    def expectation(self):
        """Ожидаем появления результата на экране"""
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, ".screen"), "15")
        )

    def get_result(self):
        """Показывает текущий результат на экране"""
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
