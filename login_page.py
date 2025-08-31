from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Адрес интернет страницы"""
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        """Конструктор для класса Страница входа с
        указанными параметрами пользователя, пороля и кнопки входа"""
        self.driver = driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self):
        """Открывает страницу по указанному URL"""
        self.driver.get(self.URL)

    def login(self, user, pwd):
        """Заполняет поле имени пользователя и пароля,
        после чего нажимает кнопку входа"""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username)).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_button).click()
