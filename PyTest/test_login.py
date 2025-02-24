import pytest
from selenium.webdriver.common.by import By
from POM.AccountPage import AccountPage
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_and_teardown")

class TestLogin:
    # Test Case 1 (Positive Test Case)
    def test_login_with_valid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        account_page = login_page.login_to_application("rh.riyo.n.bd@gmail.com","Allahproctectme#1")
        assert account_page.retrieve_the_text_of_change_your_password()


    # Test Case 2 (Negative Test Case)
    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("rh", "Allahproctectme#1")
        expected_value = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_waring_message().__contains__(expected_value)


    # Test Case 3 (Negative Test Case)
    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("rh.riyo.n.bd@gmail.com", "#1")
        expected_value = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_waring_message().__contains__(expected_value)

    # Test Case 4 (Negative Test Case)
    def test_login_with_invalid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("rh", "#1")
        expected_value = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_waring_message().__contains__(expected_value)
