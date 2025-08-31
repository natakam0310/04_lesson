import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """Фикстура для инициализации и
     завершения работы драйвера"""
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
