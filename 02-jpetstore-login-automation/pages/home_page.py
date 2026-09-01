from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    """Home page shown after sign-on; reads the welcome message."""

    # --- locators ---

    WELCOME_MESSAGE = (By.ID, "WelcomeContent")  # find the welcome message by its id

    # --- actions ---

    def get_welcome_message(self):
        self._log_step("get welcome message")
        return self._get_text(self.WELCOME_MESSAGE)

