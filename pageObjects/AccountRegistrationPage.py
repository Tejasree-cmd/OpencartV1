from selenium.webdriver.common.by import By
import time
class AccountregistrationPage:
    txt_firstname_name="firstname"
    txt_lastname_name="lastname"
    txt_email_name="email"
    txt_password_name="password"
    chk_policy_name="agree"
    btn_cont_xpath="//button[@class='btn btn-primary']"
    txt_msg_conf_path="//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self,driver):
        self.driver = driver

    def setFirstName(self,fname):
        self.driver.find_element(By.NAME,self.txt_firstname_name).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.NAME,self.txt_lastname_name).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.NAME,self.txt_email_name).send_keys(email)

    def setpassword(self,pwd):
       self.driver.find_element(By.NAME,self.txt_password_name).send_keys(pwd)
       time.sleep(3)

    def setPrivacyPolicy(self):
        self.ele1=self.driver.find_element(By.NAME,self.chk_policy_name)
        self.driver.execute_script("arguments[0].click();", self.ele1)
        #self.ele1.click()
        time.sleep(3)

    def clickContinue(self):
        self.ele2=self.driver.find_element(By.XPATH,self.btn_cont_xpath)
        self.driver.execute_script("arguments[0].click();", self.ele2)
        time.sleep(5)


    def getconfirmationmsg(self):
        try:
            return self.driver.find_element(By.XPATH,self.txt_msg_conf_path).text

        except:
            None
