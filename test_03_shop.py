import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_validation(driver):
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    # Ожидание загрузки страницы с товарами
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

    # Добавление товаров в корзину
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # Проверка, что в корзине 3 товара
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "3", "В корзине должно быть 3 товара"

    # Переход в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Ожидание загрузки страницы корзины
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
    )

    # Нажатие Checkout
    driver.find_element(By.ID, "checkout").click()

    # Ожидание загрузки формы checkout
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )

    # Заполнение формы
    driver.find_element(By.ID, "first-name").send_keys("Natalya")
    driver.find_element(By.ID, "last-name").send_keys("Podkovyrova")
    driver.find_element(By.ID, "postal-code").send_keys("684093")
    driver.find_element(By.ID, "continue").click()

    # Ожидание загрузки страницы Overview
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_info"))
    )

    # Чтение итоговой стоимости
    total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_element.text
    total_value = float(total_text.split("$")[1])

    # Проверка итоговой суммы
    expected_total = 58.29
    assert abs(total_value - expected_total) < 0.01, (
        f"Итоговая сумма составляет ${total_value:.2f}, "
        f"ожидалось ${expected_total:.2f}"
    )
