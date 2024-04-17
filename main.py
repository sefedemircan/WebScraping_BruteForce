from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/index.html")

input_ = driver.find_element(By.ID, "kod")
button_ = driver.find_element(By.CLASS_NAME, "btn")

numbers = random.sample(range(8540, 8550), 10)

for rnd in numbers:
    driver.execute_script(f"console.log({rnd})")
    input_.send_keys(rnd)
    button_.click()
    time.sleep(1)
    input_.clear()

driver.quit()