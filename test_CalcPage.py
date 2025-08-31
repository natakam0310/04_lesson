from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Calc import CalculatorPage
import allure


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест корректной работы калькулятора")
@allure.description("Тест проверяет работу калькулятора с вводом " \
"задержки и подсчётом результата")
def test_calculator():
    """Тест проверяет работу калькулятора"""
    with allure.step("Инициализация драйвера и открытие страницы" \
    " калькулятора"):
     service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    page = CalculatorPage(driver)
    page.open()
    with allure.step("Ввод значения задержки"):
     page.enter_delay(45)
     with allure.step("Нажатие на элемент калькулятора"):
      page.click_element()
    with allure.step("Ожидание результата"):
     page.expectation()
    with allure.step("Получение и проверка результата"):
     result = page.get_result()
    assert result == "15"
    with allure.step("Закрытие драйвера"):
     driver.quit()
