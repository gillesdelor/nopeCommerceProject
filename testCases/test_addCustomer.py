import random
import string
import pytest
import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.AddCustomerPage import AddCustomer


class Test_003_AddCustomer:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # Calling logger from LogGen Class
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("********************* Test_003_AddCustomer ********************* ")
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

        self.logger.info("******************* Starting Add Customer test ***************************** ")

        # Create an object named addCust of AddCustomer class (Page Object Class )
        self.addCust = AddCustomer(self.driver)
        self.driver.implicitly_wait(10)

        # Calling Add new Customer action methods
        self.logger.info("************************ Starting research Customer inside Menu *********************** ")
        self.addCust.clickOnCustomerMenu_btn()
        self.addCust.clickOnCustomerMenuItem_btn()

        self.addCust.clickOnAddNew()

        self.logger.info("************************ Providing new customer info *********************** ")
        self.driver.implicitly_wait(10)

        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        self.addCust.setFirstName("Gilles")
        self.addCust.setLastName("Zannou")
        self.addCust.clickOnGender("Male")
        self.addCust.setDoB("6/10/1985")  # Format D / MM / YYYY
        self.addCust.setCompanyName("GilCarQA")
        time.sleep(3)
        self.addCust.clickOnIsTaxExempt()
        self.addCust.select_Newsletter("Your store name")
        self.addCust.select_CustomerRoles("Registered")
        self.addCust.setManagerOfVendor("Vendor 1")
        time.sleep(3)
        self.addCust.setAdminComment("This is nopeCommerce testing")
        self.addCust.clickOnSave()

        self.logger.info("********************* Saving customer info ********************* ")

        self.logger.info("********************* Add customer validation started ********************* ")

        self.msg = self.driver.find_element_by_tag_name("body").text

        if "customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("******************* Add Customer Test Passed ********************* ")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer.png")
            self.logger.error("********************* Add Customer Test Failed ********************* ")
            assert True == False

        self.driver.close()
        self.logger.info("********************* Ending AddCustomer Test ********************* ")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
