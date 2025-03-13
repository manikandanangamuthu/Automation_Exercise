import os.path
import time

from selenium.common import NoSuchElementException

from pageObjects.LoginPage import loginpage
from utilities.readproperties import ReadConfig
from pageObjects.HomePage import homepage
from utilities.customLogger import LogGen

class Test_002_loginPage:

    logger=LogGen.loggen()
    baseURL=ReadConfig.getApplicationURL()
    email=ReadConfig.getEmail()
    password=ReadConfig.getPassword()

    def test_loginpage(self,setup):
        self.logger.info("***** Test_002_LoginPage Started *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()


        self.hp=homepage(self.driver)
        self.logger.info("***** User clicked Signup\Login button ***** ")
        self.hp.click_Signup_login_button()


        self.lp = loginpage(self.driver)
        self.logger.info("***** User Entered Email ID ***** ")
        self.lp.setEmail(self.email)
        self.logger.info("***** User Entered Password  ***** ")
        self.lp.setPassword(self.password)
        self.logger.info("***** User clicked Login Button")
        self.lp.clickLoginButton()

            #self.targetpage=self.lp.verifyLoginpageSuccessMessage()

            # Get confirmation message

