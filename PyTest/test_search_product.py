import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")

class TestSearchProduct:

   # Test Case 1 (Positive Test Case)
   def test_search_with_valid_product(self):
      self.driver = webdriver.Chrome()
      self.driver.maximize_window()
      self.driver.get("https://tutorialsninja.com/demo/")
      self.driver.find_element(By.XPATH,"//input[contains(@class,'form-control input-lg')]").send_keys("HP")
      self.driver.find_element(By.XPATH,"//button[contains(@class,'btn btn-default btn-lg')]").click()
      assert self.driver.find_element(By.XPATH,"//div[contains(@class,'product-layout product-grid col-lg-3 col-md-3 col-sm-6 col-xs-12')]").is_displayed()


   # Test Case 2 (Negative Test Case)
   def test_search_with_invalid_product(self):
      self.driver = webdriver.Chrome()
      self.driver.maximize_window()
      self.driver.get("https://tutorialsninja.com/demo/")
      self.driver.find_element(By.XPATH,"//input[contains(@class,'form-control input-lg')]").send_keys("Tiger")
      self.driver.find_element(By.XPATH,"//button[contains(@class,'btn btn-default btn-lg')]").click()
      expected_result = "There is no product that matches the search criteria."
      assert self.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expected_result)


   # Test Case 3 (Negative Test Case)
   def test_search_with_blank_product(self):
      self.driver = webdriver.Chrome()
      self.driver.maximize_window()
      self.driver.get("https://tutorialsninja.com/demo/")
      self.driver.find_element(By.XPATH,"//input[contains(@class,'form-control input-lg')]").send_keys()
      self.driver.find_element(By.XPATH,"//button[contains(@class,'btn btn-default btn-lg')]").click()
      expected_result = "There is no product that matches the search criteria."
      assert self.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expected_result)