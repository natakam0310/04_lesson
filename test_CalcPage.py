import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_calculator(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    wait = WebDriverWait(driver, 60)

    # Установить задержку выполнения калькулятора
    delay_input = wait.until(
        EC.presence_of_element_located((By.ID, "delay")))
    delay_input.clear()
    delay_input.send_keys("45")

    def click_button(label):
        xpath = f"//span[text()='{label}']"
        btn = wait.until(EC.element_to_be_clickable((
            By.XPATH, xpath)))
        btn.click()

    click_button("7")
    click_button("+")
    click_button("8")
    click_button("=")


def get_result(self):
    result = self.driver.find_element(By.CSS_SELECTOR, ".screen")
    return result.text  # вот здесь добавляем .text
    assert result == "15"
