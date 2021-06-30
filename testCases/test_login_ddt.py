import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils
import time


class Test_002_DDT_Login:
    baseUrl = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"

    # Calling logger from LogGen Class
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("********************* Test_002_DDT_Login *********************")
        self.logger.info("********************* Verifying Login DDT Test ********************* ")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(10)

        # Create an object named self.lp that is an instant of LoginPage class
        self.lp = LoginPage(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, "Sheet1")
        print("Number of Rows in the Excel is:", self.rows)

        list_status = []  # Empty variable

        # Data Driven
        for r in range(2, self.rows + 1):
            self.username = ExcelUtils.readData(self.path, "Sheet1", r, 1)
            self.password = ExcelUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = ExcelUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            # Validation of combination of actual title and exp title conditions
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("***** Passed *******")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                elif self.exp == "Fail":
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_loginDDT.png")
                    self.logger.info("***** Failed *******")
                    self.lp.clickLogout()
                    list_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_loginDDT.png")
                    self.logger.info("***** Failed *******")
                    list_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("***** Passed *******")
                    list_status.append("Pass")

        # List Status validation
        if "Fail" not in list_status:
            self.logger.info("****** Login DDT test passed *****")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_loginDDT.png")
            self.driver.close()
            self.logger.error("****** Login DDT test failed *****")
            assert False

        self.logger.info("************************ End Of Login DDT Test ******************")
        self.logger.info("************************ Completed TC_LoginDDT_002 ******************")
