from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Calc import CalculatorPage


def test_calculator():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    page = CalculatorPage(driver)
    page.open()
    page.enter_delay(45)
    page.click_element()
    page.expectation()
    result = page.get_result()
    assert result == "15"
    driver.quit()
