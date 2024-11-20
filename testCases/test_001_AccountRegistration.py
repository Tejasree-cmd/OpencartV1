import pytest

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountregistrationPage
import time
from utilities import randomString
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen  # For Logging

class Test_001_Accountreg:
    baseurl = ReadConfig.getApplicationURL()
    baseurl = baseurl.encode('ascii', 'ignore').decode('unicode_escape')
    pwd = ReadConfig.getPassword()
    print(baseurl,pwd)
    baseurl1 = "https://demo.opencart.com/en-gb?route=account/register"
    logger=LogGen.loggen()  # For Logging
    @pytest.mark.sanity
    def test_account_registration(self, setup):
        self.logger.info("**** Test 001 Account Registration Started *****")
        self.driver = setup
        time.sleep(3)
        print("inside function",self.baseurl)
        self.logger.info(" Launching Application ")
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        time.sleep(2)

        # self.hp = HomePage(self.driver)
        # time.sleep(3)
        # self.hp.clickMyAccount()
        # time.sleep(5)
        # self.hp.clickRegister()

        self.regpage=AccountregistrationPage(self.driver)
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")
        self.email=randomString.random_string_generator()+'@gmail.com'
        self.regpage.setEmail(self.email)
        self.regpage.setpassword(self.pwd)
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg = self.regpage.getconfirmationmsg()

        if self.confmsg == "Your Account Has Been Created!":
            self.logger.info("Account Registration Passed")
            self.driver.close()

            assert True
        else:
            self.loc1=os.path.abspath(os.curdir)
            print(self.loc1)
            self.loc2=os.path.join(self.loc1,"screenshots")
            self.loc=os.path.join(self.loc2,"test_account_reg.png")
            print(self.loc)
            self.driver.save_screenshot(self.loc)
            self.logger.error("Account registration failed")
            self.driver.close()
            assert False
        self.logger.info("**** Test 001 Account Registration Ended  *****")


