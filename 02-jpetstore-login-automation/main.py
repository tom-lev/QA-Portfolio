import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from scripts.login_scripts import LoginScripts
from data.login_case import LoginCase

load_dotenv()

# create a Chrome driver with settings that turn off the password popup
def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--password-store=basic")
    options.add_experimental_option("prefs", {
        "profile.password_manager_leak_detection": False
    })
    return webdriver.Chrome(options=options)


def main():
    driver = create_driver()
    wait = WebDriverWait(driver, 5)

    scripts = LoginScripts(driver, wait)

    valid_dataset = [
        LoginCase("Correct username, correct password",
                  os.getenv("TOMER2_USERNAME"), os.getenv("TOMER2_PASSWORD"), "Welcome tomer2!"),
        LoginCase("Correct username, correct password",
                  os.getenv("TOMER_USERNAME"), os.getenv("TOMER_PASSWORD"), "Welcome tomer!"),
    ]

    invalid_dataset = [
        LoginCase("Invalid user, real password", "wronguser", "j2ee"),
        LoginCase("Invalid user, real password", "wronguser", os.getenv("TOMER_PASSWORD")),
        LoginCase("Valid user, wrong password", os.getenv("TOMER2_USERNAME"), "wrongpassword"),
        LoginCase("Valid user, wrong password", os.getenv("TOMER_USERNAME"), "wrongpassword"),
        LoginCase("Invalid user, Invalid password", "wronguser", "wrongpassword"),
        LoginCase("Invalid user, Invalid password", "baduser", "badpassword"),
    ]

    try:
        # run the valid login test for each valid data set
        for data in valid_dataset:
            scripts.login_expect_success(data.description, data.username, data.password, data.welcome_message)
        # run the invalid login test for each invalid data set
        for data in invalid_dataset:
            scripts.login_expect_error(data.description, data.username, data.password)
    finally:
        # always close the browser, crash or not
        driver.quit()


if __name__ == "__main__":
    main()
