from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://uitestingplayground.com/classattr")

button = driver.find_element(By.CSS_SELECTOR, "button.btn.class1").click


sleep(5)
