import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class BaseTest:
    # Time stamp is used for create gmail generate
    def generate_email_time_stamp(self):
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "rubel" + timestamp + "@gmail.com"

