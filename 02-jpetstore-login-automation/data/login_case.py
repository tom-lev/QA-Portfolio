class LoginCase:
    """Holds the data for one login test."""

    def __init__(self, description, username, password, welcome_message=None):
        self.description = description
        self.username = username
        self.password = password
        self.welcome_message = welcome_message
