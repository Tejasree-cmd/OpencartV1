import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class LoginPage:
    txt_email_xpath = "//input[@id='input-email']"
    txt_password_Xpath = "//input[@id='input-password']"
    btn_login_xpath = "//*[@id='form-login']/div[3]/button"
    msg_myaccount_xpath = "//h2[normalize-space()='My Account']"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txt_password_Xpath).send_keys(password)

    def clickLogin(self):
        if self.driver.find_element(By.XPATH,self.btn_login_xpath).is_enabled():
            try:
                text= self.driver.find_element(By.XPATH, self.btn_login_xpath).text
                print(text)
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.btn_login_xpath).click()
                self.driver.find_element(By.XPATH, self.btn_login_xpath).click()
                self.driver.find_element(By.XPATH, self.btn_login_xpath).click()
                self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

            except:
                print( " button not clickable ")



        time.sleep(3)


    def isMyAccountPageExists(self):
        try:
            return self.driver.find_element(By.XPATH,self.msg_myaccount_xpath).is_displayed()
        except:
            return False
