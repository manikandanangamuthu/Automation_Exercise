# import os
# import time
#
# import pytest
#
# from pageObjects.HomePage import homepage
# from pageObjects.SignupPage import SignUp
# from utilities.readproperties import ReadConfig
# from utilities.customLogger import LogGen
#
# class Test_001_signupPage:
#     baseURL=ReadConfig.getApplicationURL()
#     unique_email=ReadConfig.getEmail()
#     Password=ReadConfig.getPassword()
#     logger=LogGen.loggen()
#
#     #baseURL="https://www.automationexercise.com/"
#     Name="Manikandan"
#     #unique_email = f"mani{int(time.time())}@gmail.com"
#     #Password="Q5vcQt4WNXKDQhA"
#     Day="7"
#     Month="May"
#     Year="1997"
#     FirstName="Manikandan"
#     LastName="Angamuthu"
#     Company="NSEIT"
#     Address1="Santosh Nagar"
#     Address2="Santosh Nagar"
#     Country="India"
#     State=" Andhra Pradesh"
#     City="Hyderabad"
#     ZipCode="500079"
#     MobileNumber="9512493470"
#
#
#
#     def test_signupPage(self,setup):
#         self.logger.info("*******test_001_SignupPage Started*********")
#         self.driver=setup
#         self.driver.get(self.baseURL)
#         #self.driver.maximize_window()
#
#         self.hp=homepage(self.driver)
#         self.logger.info("******* User clicked Signup/Login Button *********")
#         self.hp.click_Signup_login_button()
#
#         self.sp=SignUp(self.driver)
#         self.logger.info("******* User Entered Name *********")
#         self.sp.setUserName(self.Name)
#         self.logger.info("******* User Entered EmailId *********")
#         self.sp.setEmailId(self.unique_email)
#         self.logger.info("******* User Clicked SignUp Button  *********")
#         self.sp.clickSignUpButton()
#
#         self.logger.info("******* User Clicked Title Radio Button *********")
#         self.sp.select_Title()
#         self.logger.info("******* User Entered Password *********")
#         self.sp.setPassword(self.Password)
#         self.logger.info("******* User Selected Date Of Birth *********")
#         self.sp.select_date_of_birth(self.Day,self.Month,self.Year)
#         self.logger.info("******* User Entered Firstname *********")
#         self.sp.setFirstName(self.FirstName)
#         self.logger.info("******* User Entered Lastname *********")
#         self.sp.setLastName(self.LastName)
#         self.logger.info("******* User Entered Company name *********")
#         self.sp.setCompany(self.Company)
#         self.logger.info("******* User Entered Address 1 *********")
#         self.sp.setAddress1(self.Address1)
#         self.logger.info("******* User Entered Address 2 *********")
#         self.sp.setAddress2(self.Address2)
#         self.logger.info("******* User Selected Country *********")
#         self.sp.selectCountry(self.Country)
#         self.logger.info("******* User Entered State  *********")
#         self.sp.setState(self.State)
#         self.logger.info("******* User Entered City *********")
#         self.sp.setCity(self.City)
#         self.logger.info("******* User Entered Zipcode *********")
#         self.sp.setZipcode(self.ZipCode)
#         self.logger.info("******* User Entered Mobile Number *********")
#         self.sp.setMobilenumber(self.MobileNumber)
#         self.logger.info("******* User Clicked Account Create Button *********")
#         self.sp.clickCreateAccountButton()
#         self.logger.info("******* Validating Homepage Title *********")
#         self.confmsg=self.sp.getconfirm_Message()
#         print(self.driver.page_source)
#
#         if self.confmsg=="ACCOUNT CREATE!":
#            self.logger("***** Account Created Successfully *****")
#            self.driver.close()
#            assert True
#         else:
#             # self.logger("***** Account Not Created Successfully *****")
#             # timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")  # Format: YYYY-MM-DD_HH-MM-SS
#             # screenshot_filename = f"signupPage_{timestamp}.png"
#             # self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+screenshot_filename)
#             # self.driver.close()
#             screenshot_dir = os.path.join(os.getcwd(), "screenshots")
#             if not os.path.exists(screenshot_dir):
#                 os.makedirs(screenshot_dir)  # ✅ Create folder if missing
#
#             # ✅ Save screenshot
#             screenshot_filename = os.path.join(screenshot_dir, "test_login_failed.png")
#             self.driver.save_screenshot(screenshot_filename)
#             self.logger.info(f"📸 Screenshot saved: {screenshot_filename}")  # ✅ Debugging log
#
#             assert False
#         self.logger.info("***** test_001_SignupPage Completed *****")

#===========================================================================
import os
import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from pageObjects.HomePage import homepage
from pageObjects.SignupPage import SignUp
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_signupPage:
    baseURL = ReadConfig.getApplicationURL()
    unique_email = ReadConfig.getEmail()
    Password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # Test Data
    Name = "Manikandan"
    Day = "7"
    Month = "May"
    Year = "1997"
    FirstName = "Manikandan"
    LastName = "Angamuthu"
    Company = "NSEIT"
    Address1 = "Santosh Nagar"
    Address2 = "Santosh Nagar"
    Country = "India"
    State = "Andhra Pradesh"
    City = "Hyderabad"
    ZipCode = "500079"
    MobileNumber = "9512493470"

    def test_signupPage(self, setup):
        self.logger.info("📌 Test Started: Signup Page")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        try:
            self.hp = homepage(self.driver)
            self.hp.click_Signup_login_button()
            self.logger.info("✅ Clicked Signup/Login")

            self.sp = SignUp(self.driver)
            self.sp.setUserName(self.Name)
            self.sp.setEmailId(self.unique_email)
            self.sp.clickSignUpButton()
            self.sp.select_Title()
            self.sp.setPassword(self.Password)
            self.sp.select_date_of_birth(self.Day, self.Month, self.Year)
            self.sp.setFirstName(self.FirstName)
            self.sp.setLastName(self.LastName)
            self.sp.setCompany(self.Company)
            self.sp.setAddress1(self.Address1)
            self.sp.setAddress2(self.Address2)
            self.sp.selectCountry(self.Country)
            self.sp.setState(self.State)
            self.sp.setCity(self.City)
            self.sp.setZipcode(self.ZipCode)
            self.sp.setMobilenumber(self.MobileNumber)
            self.sp.clickCreateAccountButton()
            self.logger.info("✅ Clicked Create Account")

            # Get confirmation message
            self.confmsg = self.sp.getconfirm_Message()
            if self.confmsg == "ACCOUNT CREATED!":
                self.logger.info("✅ Account Created Successfully")
                assert True
            else:
                self.logger.error("❌ Account Creation Failed")

                # ✅ **DIRECTLY CAPTURE SCREENSHOT HERE**
                screenshot_dir = os.path.join(os.getcwd(), "screenshots")
                os.makedirs(screenshot_dir, exist_ok=True)  # ✅ Ensure folder exists

                timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
                screenshot_path = os.path.join(screenshot_dir, f"AccountCreationFailed_{timestamp}.png")

                self.driver.save_screenshot(screenshot_path)
                self.logger.info(f"📸 Screenshot Saved: {screenshot_path}")  # ✅ Debugging log

                assert False

        except NoSuchElementException as e:
            self.logger.error(f"❌ Element Not Found: {str(e)}")

            # ✅ **CAPTURE SCREENSHOT IF ELEMENT NOT FOUND**
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)  # ✅ Ensure folder exists

            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_path = os.path.join(screenshot_dir, f"NoSuchElement_{timestamp}.png")

            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"📸 Screenshot Saved: {screenshot_path}")

            assert False

        finally:
            self.driver.quit()
            self.logger.info("📌 Test Completed: Signup Page")
