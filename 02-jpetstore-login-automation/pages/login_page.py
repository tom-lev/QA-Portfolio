from selenium.webdriver.common.by import By
from pages.base_page import BasePage

LOGIN_URL = "https://petstore.octoperf.com/actions/Account.action?signonForm="

class LoginPage(BasePage):
    """Login page: enters credentials and reads sign-on errors."""

    # --- locators ---

    USERNAME_FIELD = (By.NAME, "username")  # find the field by its name
    PASSWORD_FIELD = (By.NAME, "password")  # find the field by its name
    LOGIN_BUTTON = (By.NAME, "signon")   # find the button by its name
    ERROR_MESSAGE = (By.CLASS_NAME, "messages")  # find the error message by its class

    # --- actions ---

    def nav_to(self):
        self._log_step("navigate to login page")
        self.driver.get(LOGIN_URL)

    def enter_username(self, value):
        self._log_step(f"enter username '{value}'")
        self._type(self.USERNAME_FIELD, value)

    def enter_password(self, value):
        self._log_step(f"enter password '{value}'")
        self._type(self.PASSWORD_FIELD, value)

    def click_login_button(self):
        self._log_step("click login button")
        self._click(self.LOGIN_BUTTON)

    def get_error_message(self):
        self._log_step("get error message")
        return self._get_text(self.ERROR_MESSAGE)
