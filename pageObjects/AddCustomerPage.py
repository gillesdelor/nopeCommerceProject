import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    # Add Customer page
    linkCustomer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    linkCustomer_menuItem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"

    txtEmail_xpath = "//input[@id='Email']"

    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"

    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"

    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    chboxIsTaxExempt_xpath = "//input[@id='IsTaxExempt']"

    lstNewsletter_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstNewsletter_YourStoreName_xpath = "//li[contains(text(),'Your store name')]"
    lstNewsletter_TestStore2_xpath = "//li[contains(text(),'Test store 2')]"

    txtcustomerRoles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemForumModerators_xpath = "//li[contains(text(),'Forum Moderators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuest_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"

    drpManagerofVendor_xpath = "//*[@id='VendorId']"
    chboxActive_id = "Active"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"

    btnSave_xpath = "//button[@name='save']"
    btnSaveAndContinue_xpath = "//button[@name='save-continue']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu_btn(self):
        self.driver.find_element_by_xpath(self.linkCustomer_menu_xpath).click()

    def clickOnCustomerMenuItem_btn(self):
        self.driver.find_element_by_xpath(self.linkCustomer_menuItem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, firstname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lastname)

    def clickOnGender(self, gender):
        if gender == "Male":
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == "Female":
            self.driver.find_element_by_id(self.rdFemaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setDoB(self, dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, compName):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(compName)

    def clickOnIsTaxExempt(self):
        self.driver.find_element_by_xpath(self.chboxIsTaxExempt_xpath).click()

    def select_Newsletter(self, newsletter):
        self.driver.find_element_by_xpath(self.lstNewsletter_xpath).click()
        time.sleep(3)
        if newsletter == "Your store name":
            self.driver.find_element_by_xpath(self.lstNewsletter_YourStoreName_xpath).click()
        elif newsletter == "Test store 2":
            self.driver.find_element_by_xpath(self.lstNewsletter_TestStore2_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.lstNewsletter_YourStoreName_xpath).click()

    def select_CustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
        time.sleep(3)

        if role == "Administrators":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)

        elif role == "Forum Moderators":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemForumModerators_xpath)

        elif role == "Guests":
            # Here user can be Registered (or ) Guest ,only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li[1]/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuest_xpath)

        elif role == "Registered":
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li[1]/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)

        elif role == "Vendors":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)

        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuest_xpath)
        time.sleep(3)

        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drpManagerofVendor_xpath))
        drp.select_by_visible_text(value)

    def clickOnActiveBtn(self):
        self.driver.find_element_by_id(self.chboxActive_id).click()

    def setAdminComment(self, content):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()

    def clickOnSaveAndContinue(self):
        self.driver.find_element_by_xpath(self.btnSaveAndContinue_xpath).click()
