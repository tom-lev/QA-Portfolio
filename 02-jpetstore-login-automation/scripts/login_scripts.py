from pages.login_page import LoginPage
from pages.home_page import HomePage
from selenium.common.exceptions import TimeoutException

# the error message we expect for every failed login
ERROR_MESSAGE = "Invalid username or password. Signon failed."

class LoginScripts:
    """Login test scenarios"""

    def __init__(self, driver, wait):
        self.__driver = driver
        self.__wait = wait
        self.__login_page = LoginPage(self.__driver, self.__wait)
        self.__home_page = HomePage(self.__driver, self.__wait)
        self.__test_num = 0

    # shared login steps for all tests
    def _login(self, username, password):
        self.__login_page.nav_to()
        self.__login_page.enter_username(username)
        self.__login_page.enter_password(password)
        self.__login_page.click_login_button()

    def login_expect_success(self, description, username, password, expected):
        self.__test_num += 1
        print(f"TEST {self.__test_num}: valid login - {description} | expected = '{expected}'")
        print("=" * 60)
        actual_message = None

        # assert checks the text; both excepts print FAILED instead of crashing:
        # AssertionError = wrong text, TimeoutException = a step timed out
        try:
            self._login(username, password)
            actual_message = self.__home_page.get_welcome_message()
            assert actual_message == expected
            print(f"Passed - got '{actual_message}'")
        except AssertionError:
            print(f"FAILED (wrong text) - expected '{expected}', got '{actual_message}'")
        except TimeoutException:
            print(f"FAILED (timeout) - a step timed out, see the last STEP above")
        print()

        # a successful login leaves a cookie; clear it so the next test starts logged out
        self.__driver.delete_all_cookies()

    def login_expect_error(self, description, username, password):
        self.__test_num += 1
        print(f"TEST {self.__test_num}: invalid login - {description} | expected = '{ERROR_MESSAGE}'")
        print("=" * 60)
        actual_message = None

        # assert checks the text; both excepts print FAILED instead of crashing:
        # AssertionError = wrong text, TimeoutException = a step timed out
        try:
            self._login(username, password)
            actual_message = self.__login_page.get_error_message()
            assert actual_message == ERROR_MESSAGE
            print(f"Passed - got '{actual_message}'")
        except AssertionError:
            print(f"FAILED (wrong text) - expected '{ERROR_MESSAGE}', got '{actual_message}'")
        except TimeoutException:
            print(f"FAILED (timeout) - a step timed out, see the last STEP above")
        print()