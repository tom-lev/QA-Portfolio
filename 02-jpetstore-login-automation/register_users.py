import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

users = [
    (os.getenv("TOMER_USERNAME"), os.getenv("TOMER_PASSWORD"), "tomer"),
    (os.getenv("TOMER2_USERNAME"), os.getenv("TOMER2_PASSWORD"), "tomer2"),
]
required_fields = [
    "account.lastName",
    "account.email",
    "account.phone",
    "account.address1",
    "account.address2",
    "account.city",
    "account.state",
    "account.zip",
    "account.country",
]

def fill(name,value):
    field = wait.until(EC.visibility_of_element_located((By.NAME, name)))
    field.send_keys(value)

for username, password, firstname in users:
    driver.get("https://petstore.octoperf.com/actions/Account.action?newAccountForm=")
    fill("username", username)
    fill("password", password)
    fill("repeatedPassword", password)
    fill("account.firstName", firstname)

    for field in required_fields:
        fill(field, "ABC")
    button = wait.until(EC.element_to_be_clickable((By.NAME, "newAccount")))
    button.click()

    time.sleep(5)
driver.quit()
