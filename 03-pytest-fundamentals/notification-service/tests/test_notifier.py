import pytest
import notifier
from notifier import User


@pytest.mark.regression
def test_with_phone_gets_sms_not_email(service, sms_client, email_client):
    user = User("tomer", "tomer@gmail.com", "0506843971")
    service.notify(user, "hello world")
    sms_client.send.assert_called_once_with(user.phone, "hello world")
    email_client.send.assert_not_called()


@pytest.mark.smoke
def test_no_phone_gets_email(service, sms_client, email_client):
    user = User("tomer", "tomer@gmail.com")
    service.notify(user, "hello world")
    email_client.send.assert_called_once_with(user.email, "hello world")
    sms_client.send.assert_not_called()


@pytest.mark.regression
@pytest.mark.xfail(
    reason="BUG-01: notify catches TimeoutError instead of ConnectionError", strict=True
)
def test_sms_connection_error_falls_back_to_email(service, sms_client, email_client):
    user = User("tomer", "tomer@gmail.com", "0506843971")
    sms_client.send.side_effect = ConnectionError
    service.notify(user, "hello world")
    email_client.send.assert_called_once_with(user.email, "hello world")


@pytest.mark.smoke
def test_notify_appends_line_to_log_sms(service, tmp_path):
    user = User("tomer", "tomer@gmail.com", "0506843971")
    expected_log_file = tmp_path / "notifications.log"
    service.notify(user, "hello world")
    service.notify(user, "hello world2")
    assert (
        expected_log_file.read_text(encoding="utf-8")
        == "sms|tomer|hello world\nsms|tomer|hello world2\n"
    )


@pytest.mark.smoke
def test_notify_appends_line_to_log_email(service, tmp_path):
    user = User(
        "tomer",
        "tomer@gmail.com",
    )
    expected_log_file = tmp_path / "notifications.log"
    service.notify(user, "hello world")
    service.notify(user, "hello world2")
    assert (
        expected_log_file.read_text(encoding="utf-8")
        == "email|tomer|hello world\nemail|tomer|hello world2\n"
    )


@pytest.mark.regression
def test_sent_via_sms(service, capsys):
    user = User("tomer", "tomer@gmail.com", "0506843971")
    service.notify(user, "hello world")
    captured = capsys.readouterr()
    assert captured.out == "sent via sms\n"


@pytest.mark.regression
def test_sent_via_email(service, capsys):
    user = User("tomer", "tomer@gmail.com")
    service.notify(user, "hello world")
    captured = capsys.readouterr()
    assert captured.out == "sent via email\n"


midnight_bug = pytest.mark.xfail(
    reason="BUG-02: quiet hours that cross midnight are not detected", strict=True
)


@pytest.mark.regression
@pytest.mark.parametrize(
    "time, expected_channel, quiet_hours",
    [
        pytest.param(21, "sms", "22-7", id="22-7-at-21-sms"),
        pytest.param(22, "email", "22-7", id="22-7-at-22-email", marks=midnight_bug),
        pytest.param(
            23,
            "email",
            "22-7",
            id="22-7-at-23-email",
            marks=midnight_bug,
        ),
        pytest.param(0, "email", "22-7", id="22-7-at-0-email", marks=midnight_bug),
        pytest.param(6, "email", "22-7", id="22-7-at-6-email", marks=midnight_bug),
        pytest.param(7, "sms", "22-7", id="22-7-at-7-sms"),
        pytest.param(12, "sms", "13-15", id="13-15-at-12-sms"),
        pytest.param(13, "email", "13-15", id="13-15-at-13-email"),
        pytest.param(14, "email", "13-15", id="13-15-at-14-email"),
        pytest.param(15, "sms", "13-15", id="13-15-at-15-sms"),
    ],
)
def test_only_email_in_quiet_hours(
    service, monkeypatch, time, expected_channel, quiet_hours
):
    user = User("tomer", "tomer@gmail.com", "0506843971")
    monkeypatch.setenv("QUIET_HOURS", quiet_hours)

    def fake_get_current_hour():
        return time

    monkeypatch.setattr(notifier, "get_current_hour", fake_get_current_hour)
    result_channel = service.notify(user, "hello world")
    assert result_channel == expected_channel
