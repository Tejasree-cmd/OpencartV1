from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class HomePage:
      lnk_myaccount_xpath = "//span[normalize-space()='My Account']"
      lnk_register_lnktxt = "Register"
      lnk_login_lnktxt = "Login"

      def __init__(self,driver):
          self.driver = driver

      def clickMyAccount(self):
          print("My Account")
         # self.ele = self.driver.find_element(By.XPATH, self.lnk_myaccount_xpath)
          #self.action = ActionChains(self.driver)
          self.driver.find_element(By.XPATH,self.lnk_myaccount_xpath).click()

          #self.action.move_to_element(self.ele).click().perform()
          print("After My account")

      def clickRegister(self):
          print("Click register")
          self.driver.find_element(By.LINK_TEXT,self.lnk_register_lnktxt).click()

      def clickLogin(self):
          self.driver.find_element(By.LINK_TEXT,self.lnk_login_lnktxt).click()
