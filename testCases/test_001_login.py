import pytest
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
import time
from utilities import randomString
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen  # For Logging

class Test_Login:
    logger = LogGen.loggen()
    baseurl = "https://demo.opencart.com/en-gb?route=account/login"
    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    print(user , password)
    time.sleep(3)
    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("***** Starting test_002_login *******")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.hp = LoginPage(self.driver)
        self.hp.setEmail(self.user)
        self.hp.setPassword(self.password)
        self.hp.clickLogin()

        self.targgetpage= self.hp.isMyAccountPageExists()
        if self.targgetpage == True:
            assert True

        else:
            self.loc1 = os.path.abspath(os.curdir)
            print(self.loc1)
            self.loc2 = os.path.join(self.loc1, "screenshots")
            self.loc = os.path.join(self.loc2, "test_account_Login.png")
            print(self.loc)
            self.driver.save_screenshot(self.loc)

            assert False
        self.driver.close()
        self.logger.info("**** Test 002 Account Login Ended  *****")

