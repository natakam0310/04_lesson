from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/inputs")

number_input = driver.find_element(By.XPATH, '//input[@type="number"] ')
number_input.send_keys("1000", Keys.RETURN)

number_input.clear()

number_input = driver.find_element(By.XPATH, '//input[@type="number"] ')
number_input.send_keys("800", Keys.RETURN)

driver.quit()
