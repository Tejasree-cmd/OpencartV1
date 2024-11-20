from selenium.webdriver.common.by import By

class MyAccountPage:
    lnk_logout_xpath ="//a[@class='list-group-item'][normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver = driver

    def clickLogout(self):
        self.ele1=self.driver.find_element(By.XPATH,self.lnk_logout_xpath)
        self.driver.execute_script("arguments[0].click();", self.ele1)