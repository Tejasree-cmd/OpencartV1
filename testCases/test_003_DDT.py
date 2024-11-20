import pytest
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage

import time
from utilities import randomString
import os
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen  # For Logging


class Test_Login:
    logger = LogGen.loggen()
    baseurl = "https://demo.opencart.com/en-gb?route=account/login"
    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    print(user , password)
    time.sleep(3)
    path = ".\\testData\\Opencart_Login.xlsx"
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("***** Starting test_003_ddtlogin *******")
        self.rows= XLUtils.getRowCount(self.path,'Sheet1')
        lst_status=[]
        self.driver = setup


        self.lp = LoginPage(self.driver)
        self.ma = MyAccountPage(self.driver)
        for r in range(2,self.rows+1):
            self.driver.get(self.baseurl)
            self.driver.maximize_window()
            self.email = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password= XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp=XLUtils.readData(self.path,'Sheet1',r,3)
            self.lp.setEmail(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)
            self.targgetpage=self.lp.isMyAccountPageExists()

            if self.exp=='Valid':
                if self.targgetpage==True:
                    lst_status.append('Pass')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Fail')
            elif self.exp=='Invalid':
                if self.targgetpage==True:
                    lst_status.append('Fail')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Pass')


        self.driver.close()

        if "Fail" not in lst_status:
            assert True
        else:
            assert False


        self.logger.info("**** Test 003 Account Login Ended  *****")

