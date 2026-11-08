"""Notification service module (system under test).

Specification:

User(name, email, phone=None)
    Every user has an email. A phone number is optional.

NotificationService(sms_client, email_client, log_dir)
    sms_client and email_client are external services (an SMS gateway and a
    mail server). Both have a send(to, message) method.
    log_dir is a directory (Path) where the log file is written.

notify(user, message)
    1. If the user has a phone and it is not quiet hours: sends an SMS with
       sms_client.send(phone, message).
    2. If the user has no phone, or it is quiet hours: sends an email with
       email_client.send(email, message).
    3. If sending the SMS fails with ConnectionError: sends an email instead.
       The exception is not raised to the caller.
    4. Appends a line to notifications.log inside log_dir, in the format
       <channel>|<user name>|<message> followed by a newline.
       For example: sms|Dana|Your order shipped
    5. Prints "sent via sms" or "sent via email".
    6. Returns the channel the message was sent through: "sms" or "email".

is_quiet_hours()
    - Reads the QUIET_HOURS environment variable in the format "start-end",
      whole hours 0-23. For example "22-7".
    - If the variable is not set: there are no quiet hours.
    - The current hour comes from get_current_hour() (in clock.py).
    - The start hour is inside the range, the end hour is outside it.
      With "22-7": 22:00 to 6:59 is quiet, 7:00 is not.
    - A range can cross midnight ("22-7") or not ("13-15").
"""

import os
from dataclasses import dataclass

from clock import get_current_hour


@dataclass
class User:
    name: str
    email: str
    phone: str = None


class NotificationService:
    def __init__(self, sms_client, email_client, log_dir):
        self.sms_client = sms_client
        self.email_client = email_client
        self.log_dir = log_dir

    def is_quiet_hours(self):
        quiet = os.environ.get("QUIET_HOURS")
        if not quiet:
            return False
        start, end = quiet.split("-")
        start, end = int(start), int(end)
        hour = get_current_hour()
        return start <= hour < end

    def notify(self, user, message):
        channel = "email"
        if user.phone and not self.is_quiet_hours():
            try:
                self.sms_client.send(user.phone, message)
                channel = "sms"
            except TimeoutError:
                pass

        if channel == "email":
            self.email_client.send(user.email, message)

        log_file = self.log_dir / "notifications.log"
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"{channel}|{user.name}|{message}\n")

        print(f"sent via {channel}")
        return channel
