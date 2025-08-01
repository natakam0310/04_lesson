import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    #Прописать путь до драйвера
    edge_service = EdgeService(r"C:\Users\Андрей\Desktop\дз5\edgedriver_win64\msedgedriver.exe")
    driver = webdriver.Edge(service=edge_service)
    driver.maximize_window()
    yield driver
    driver.quit()
    
@pytest.mark.usefixtures("driver")
def test_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 16)
    
    first_name_input = wait.until(EC.visibility_of_element_located((By.NAME, "first-name")))
    first_name_input.send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")
    

    button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].click();", button)
    
   
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".overlay-class")))

    

    # Проверка подсветки поля Zip code
    pole_z = driver.find_element(By.ID, "zip-code").get_attribute("class")
    assert pole_z == "alert py-2 alert-danger"

    # Проверка подсветки остальных полей
    poles = ["#first-name", "#last-name", "#address", "#city", "#country", "#e-mail", "#phone", "#company"]
    for pole in poles:
        pole_class = driver.find_element(By.CSS_SELECTOR, pole).get_attribute("class")
        assert pole_class == "alert py-2 alert-success"

        