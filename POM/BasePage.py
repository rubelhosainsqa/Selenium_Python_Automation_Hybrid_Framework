from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self,driver):
        self.driver = driver

    # This method is used for input data into an element
    def type_into_element(self,text,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    # This method is used for clicking an element
    def element_click(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()

    # This method is used for check the display status of an element
    def check_display_status_of_element(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        return element.is_displayed()

    # This method is used for retrieve text
    def retrieve_element_text(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        return element.text

    # This method is used for driver find element
    def get_element(self,locator_name,locator_value):
        element = None
        if locator_name.endswith("_id"):
            element = self.driver.find_element(By.ID,locator_value)
        elif locator_name.endswith("_name"):
            element = self.driver.find_element(By.NAME,locator_value)
        elif locator_name.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME,locator_value)
        elif locator_name.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT,locator_value)
        elif locator_name.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH,locator_value)
        elif locator_name.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR,locator_value)
        return element
