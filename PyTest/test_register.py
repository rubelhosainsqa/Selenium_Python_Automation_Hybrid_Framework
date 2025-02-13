import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")


class TestRegister:

    # Test Case 1 (Positive Test Case)
    def test_register_module_with_required_data(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://tutorialsninja.com/demo/")
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.NAME, "firstname").send_keys("Rubel")
        self.driver.find_element(By.NAME, "lastname").send_keys("Hosain")
        self.driver.find_element(By.NAME, "email").send_keys(self.generate_email_time_stamp())
        self.driver.find_element(By.NAME, "telephone").send_keys("01785255727")
        self.driver.find_element(By.NAME, "password").send_keys("Testman#1")
        self.driver.find_element(By.NAME, "confirm").send_keys("Testman#1")
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        expect_result = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expect_result)

    # Test Case 2 (Positive Test Case)
    def test_register_module_with_all_data(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://tutorialsninja.com/demo/")
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.NAME, "firstname").send_keys("Rubel")
        self.driver.find_element(By.NAME, "lastname").send_keys("Hosain")
        self.driver.find_element(By.NAME, "email").send_keys(self.generate_email_time_stamp())
        self.driver.find_element(By.NAME, "telephone").send_keys("01785255727")
        self.driver.find_element(By.NAME, "password").send_keys("Testman#1")
        self.driver.find_element(By.NAME, "confirm").send_keys("Testman#1")
        self.driver.find_element(By.XPATH,"//label[@class='radio-inline'][1]").click()
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        expect_result = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expect_result)


    # Test Case 3 (Negative Test Case)
    def test_register_module_with_required_data_and_duplicate_email(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://tutorialsninja.com/demo/")
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.NAME, "firstname").send_keys("Rubel")
        self.driver.find_element(By.NAME, "lastname").send_keys("Hosain")
        self.driver.find_element(By.NAME, "email").send_keys("rh.riyo.n.bd@gmail.com")
        self.driver.find_element(By.NAME, "telephone").send_keys("01785255727")
        self.driver.find_element(By.NAME, "password").send_keys("Testman#1")
        self.driver.find_element(By.NAME, "confirm").send_keys("Testman#1")
        self.driver.find_element(By.XPATH,"//label[@class='radio-inline'][1]").click()
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        expect_result = "Warning: E-Mail Address is already registered!"
        assert self.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__contains__(expect_result)


    # Time stamp is used for create gmail generate
    def generate_email_time_stamp(self):
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "rubel"+timestamp+"@gmail.com"