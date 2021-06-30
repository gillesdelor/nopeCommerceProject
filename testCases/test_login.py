import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # Calling logger from LogGen Class
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_home_page_title(self, setup):
        self.logger.info("********************* Test_001_Login ********************* ")
        self.logger.info("********************* Verifying Home Page Title ********************* ")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(10)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.logger.info("********************* Home Page Title Test is passed ********************* ")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_home_page_title.png")
            self.driver.close()
            self.logger.error("********************* Home Page Title Test is failed ********************* ")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("********************* Verifying Login Test ********************* ")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(10)

        # Create an object named self.lp that is an instant of LoginPage class
        self.lp = LoginPage(self.driver)

        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********************* Login Test is passed ********************* ")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("********************* Login Test is failed ********************* ")
            assert False
