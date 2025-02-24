from selenium.webdriver.common.by import By
from POM.AccountSuccessPage import AccountSuccessPage
from POM.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)


    # For the First Name input field
    first_name_input_filed_lct_name = "firstname"
    # For the Last Name input field
    last_name_input_filed_lct_name = "lastname"
    # For the Email Address input field
    email_address_input_filed_lct_name = "email"
    # For the Telephone number input field
    telephone_input_filed_lct_name = "telephone"
    # For the Password input field
    password_input_filed_lct_name = "password"
    # For the Confirm Password input field
    confirm_password_input_filed_lct_name = "confirm"
    # For the Privacy Policy check box
    privacy_filed_lct_xpath = "//input[@type='checkbox']"
    # For the Continue button
    continue_button_filed_lct_xpath = "//input[@type='submit']"
    # For the Radio button
    radio_button_filed_lct_xpath = "//label[@class='radio-inline'][1]"
    # For the Warning Message
    warning_message_filed_lct_xpath = "//div[@id='account-register']/div[1]"







    # For the First Name input field
    def enter_first_name(self,first_name):
        self.type_into_element(first_name,"first_name_input_filed_lct_name",self.first_name_input_filed_lct_name) # Used "type_into_element" method of BasePage

    # For the Last Name input field
    def enter_last_name(self, last_name):
        self.type_into_element(last_name,"last_name_input_filed_lct_name",self.last_name_input_filed_lct_name) # Used "type_into_element" method of BasePage

    # For the Email Address input field
    def enter_email_address(self, email_address):
        self.type_into_element(email_address,"email_address_input_filed_lct_name",self.email_address_input_filed_lct_name) # Used "type_into_element" method of BasePage

    # For the Telephone number input field
    def enter_telephone_number(self, telephone):
        self.type_into_element(telephone,"telephone_input_filed_lct_name",self.telephone_input_filed_lct_name) # Used "type_into_element" method of BasePage

    # For the Password input field
    def enter_password(self, password):
        self.type_into_element(password,"password_input_filed_lct_name",self.password_input_filed_lct_name) # Used "type_into_element" method of BasePage

    # For the Confirm Password input field
    def enter_confirm_password(self, confirm_password):
        self.type_into_element(confirm_password,"confirm_password_input_filed_lct_name",self.confirm_password_input_filed_lct_name) # Used "type_into_element" method of BasePage

    # For the Privacy Policy check box
    def check_privacy_policy(self):
        self.element_click("privacy_filed_lct_xpath",self.privacy_filed_lct_xpath) # Used "element_click" method of BasePage

    # For the Continue button
    def click_on_the_continue_button(self):
        self.element_click("continue_button_filed_lct_xpath",self.continue_button_filed_lct_xpath) # Used "element_click" method of BasePage
        return AccountSuccessPage(self.driver) #Return the POM>>AccountSuccessPage.py file as an object

    # For the Radio button
    def click_on_the_radio_button(self):
        self.element_click("radio_button_filed_lct_xpath",self.radio_button_filed_lct_xpath) # Used "element_click" method of BasePage


    # For create an account
    def register_an_account(self,first_name,last_name,email_address,telephone,password,confirm_password,privacy_policy,yes_or_no):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email_address(email_address)
        self.enter_telephone_number(telephone)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        if privacy_policy.__eq__("select"):
            self.check_privacy_policy()
        if yes_or_no.__eq__("yes"):
            self.click_on_the_radio_button()
        return self.click_on_the_continue_button()

    # For the Warning Message
    def retrieve_waring_message(self):
        self.retrieve_element_text("warning_message_filed_lct_xpath",self.warning_message_filed_lct_xpath) # Used "retrieve_element_text" method of BasePage
