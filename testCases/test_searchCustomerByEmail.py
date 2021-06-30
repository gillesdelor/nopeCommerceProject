import pytest
import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.AddCustomerPage import AddCustomer


class Test_004_SearchCustomerByEmail:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # Calling logger from LogGen Class
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("********************* Test_004_ SearchCustomerByEmail********************* ")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # Create an object named self.lp that is an instant of LoginPage class
        self.lp = LoginPage(self.driver)

        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******************* Login successful ***************************** ")

        self.logger.info("******************* Starting Search Customer by Email ***************************** ")

        # Create an object named addCust of AddCustomer class (Page Object Class )
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomerMenu_btn()
        self.addCust.clickOnCustomerMenuItem_btn()

        self.logger.info("************************ Searching Customer by  emailID *********************** ")
        # Create an object named searchCust of SearchCustomer class (Page Object Class )
        searchCust = SearchCustomer(self.driver)
        searchCust.setEmail("victoria_victoria@nopCommerce.com")
        searchCust.clickSearch_btn()
        time.sleep(5)
        status = searchCust.searchCustomerBy_Email("victoria_victoria@nopCommerce.com")
        assert True == status

        self.logger.info("**************************** TC_Search Customer By Email_004 Finished ")
        self.driver.close()
