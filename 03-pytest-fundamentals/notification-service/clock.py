from datetime import datetime


def get_current_hour():
    """The current hour on this machine, 0-23."""
    return datetime.now().hour
