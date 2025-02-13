import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")

class TestLogin:
    # Test Case 1 (Positive Test Case)
    def test_login_with_valid_email_and_valid_password(self):
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.NAME, "email").send_keys("rh.riyo.n.bd@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("Allahproctectme#1")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        assert self.driver.find_element(By.LINK_TEXT, "Change your password").is_displayed()


    # Test Case 2 (Negative Test Case)
    def test_login_with_invalid_email_and_valid_password(self):
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.NAME, "email").send_keys("111@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("Allahproctectme#1")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_value = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text.__contains__(expected_value)


    # Test Case 3 (Negative Test Case)
    def test_login_with_valid_email_and_invalid_password(self):
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.NAME, "email").send_keys("rh.riyo.n.bd@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("#1")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_value = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text.__contains__(expected_value)


    # Test Case 4 (Negative Test Case)
    def test_login_with_invalid_email_and_invalid_password(self):
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.NAME, "email").send_keys("")
        self.driver.find_element(By.NAME, "password").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_value = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text.__contains__(expected_value)