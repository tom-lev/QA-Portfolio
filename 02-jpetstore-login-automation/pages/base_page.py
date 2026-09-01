from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Base class with shared helpers inherited by all page objects."""
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # --- helpers ---

    # Helper function to type into a field.
    def _type(self, locator, value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    # Helper function to click a button.
    def _click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    # Helper function to get text from an element.
    def _get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    # Helper to print each step
    def _log_step(self, action):
        print(f"  STEP: {action}")

