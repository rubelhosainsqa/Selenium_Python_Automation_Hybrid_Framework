import pytest
from openpyxl.reader.excel import ExcelReader
from selenium import webdriver
from selenium.webdriver.common.by import By
from POM.AccountSuccessPage import AccountSuccessPage
from POM.BasePage import BasePage
from POM.HomePage import HomePage
from POM.RegisterPage import RegisterPage
from PyTest.BaseTest import BaseTest
from utilities import ExcelUtilis


class TestRegister(BaseTest):

    # Test Case 1 (Positive Test Case)
    def test_register_module_with_required_data(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account(
            ExcelUtilis.get_cell_data("ExcelFiles/TutorialsNinja.xlsx","RegisterTest",2,1),
            ExcelUtilis.get_cell_data("ExcelFiles/TutorialsNinja.xlsx","RegisterTest",2,2),
            self.generate_email_time_stamp(),"01785255727","Testman#1","Testman#1","select","no")

        expect_result = "Your Account Has Been Created!"
        assert account_success_page.retrieve_successfully_account_creation_message().__eq__(expect_result)


    # Test Case 2 (Positive Test Case)
    def test_register_module_with_all_data(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account("Rubel","Hosain",self.generate_email_time_stamp(),"01785255727","Testman#1","Testman#1","select","yes")
        expect_result = "Your Account Has Been Created!"
        assert account_success_page.retrieve_successfully_account_creation_message().__eq__(expect_result)


    # Test Case 3 (Negative Test Case)
    def test_register_module_with_required_data_and_duplicate_email(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("Rubel","Hosain","rh.riyon.bd@gmail.com","01785255727","Testman#1","Testman#1","select","no")
        expect_result = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_waring_message().__eq__(expect_result)

