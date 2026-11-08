"""Shared fixtures for the notification service tests.

The SMS and email clients are external services, so both are replaced with
Mock objects. The service writes its log to pytest's tmp_path, so every test
gets a clean, empty log directory.

Bugs found:
BUG-01: when SMS raises ConnectionError, notify raises instead of
        falling back to email (catches TimeoutError).
        Found by: test_sms_connection_error_falls_back_to_email
BUG-02: notify doesn't handle quiet hours that cross midnight.
        Found by: test_only_email_in_quiet_hours, ids:
        1. 22-7-at-22-email
        2. 22-7-at-23-email
        3. 22-7-at-0-email
        4. 22-7-at-6-email
"""

import pytest
from notifier import NotificationService
from unittest.mock import Mock


@pytest.fixture
def sms_client():
    return Mock()


@pytest.fixture
def email_client():
    return Mock()


@pytest.fixture
def service(sms_client, email_client, tmp_path):
    return NotificationService(sms_client, email_client, tmp_path)
