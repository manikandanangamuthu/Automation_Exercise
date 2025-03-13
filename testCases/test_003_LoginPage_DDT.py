# import os
#
# from pageObjects.HomePage import homepage
# from pageObjects.LoginPage import loginpage
# from pageObjects.LogoutPage import logout
# from utilities.customLogger import LogGen
# from utilities.readproperties import ReadConfig
# from utilities import XLUtilis
#
# class Test_003_loginpage_DDT():
#
#     baseURL = ReadConfig.getApplicationURL()
#     logger = LogGen.loggen()
#     path = os.path.abspath(os.curdir) + "\\testData\\loginData.xlsx"
#
#
#     def test_003_loginpage_DDT(self,setup):
#
#         rows=XLUtilis.getRowsCount(self.path,'Sheet1')
#
#
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         self.driver.maximize_window()
#
#
#         hp=homepage(self.driver)
#         lp = loginpage(self.driver)
#         logoutpage=logout(self.driver)
#
#         for r in range(2, rows+1):
#
#             hp.click_Signup_login_button()
#
#             email=XLUtilis.readData(self.path,'Sheet1',r,1)
#             password=XLUtilis.readData(self.path,'Sheet1',r,2)
#             Expected_Status=XLUtilis.readData(self.path,'Sheet1',r,3)
#             success_message=lp.get_Loginpage_success_Message()
#             fail_login_message=lp.get_Loginpage_fail_Message()
#             lp.setEmail(email)
#             lp.setPassword(password)
#
#
#
#                 if Expected_Status=="Valid":
#
#                     if success_message=="Full-Fledged practice website for Automation Engineers":
#                         XLUtilis.writeData(self.path,'Sheet1',r,4,"Pass")
#                         logoutpage.clickLogoutButton()
#                     else:
#                         XLUtilis.writeData(self.path,'Sheet1',r,4,"fail")
#                 elif Expected_Status=="Invalid":
#                     if fail_login_message=="Your email or password is incorrect!":
#                        XLUtilis.writeData(self.path,'Sheet1',r,4,"pass")
#                     else:
#                        XLUtilis.writeData(self.path, 'Sheet1', r, 4, "fail")
#
#             self.driver.close()
#


import os
from pageObjects.HomePage import homepage
from pageObjects.LoginPage import loginpage
from pageObjects.LogoutPage import logout
from utilities.customLogger import LogGen
from utilities.readproperties import ReadConfig
from utilities import XLUtilis
from selenium.common.exceptions import NoSuchElementException  # ✅ Handle login failures

class Test_003_loginpage_DDT:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path = os.path.join(os.getcwd(), "testData", "loginData.xlsx")  # ✅ Use correct Excel path

    def test_003_loginpage_DDT(self, setup):
        self.logger.info("***** Loginpage DDT Started *****")
        rows = XLUtilis.getRowsCount(self.path, 'Sheet1')  # ✅ Get row count
        self.driver = setup
        self.driver.get(self.baseURL)  # ✅ Load correct URL
        self.driver.maximize_window()

        hp = homepage(self.driver)
        lp = loginpage(self.driver)
        logoutpage = logout(self.driver)

        for r in range(2, rows + 1):  # ✅ Loop through Excel data
            self.logger.info(f"🔹 Running Test: Row {r}")

            # ✅ Click Signup/Login button
            hp.click_Signup_login_button()

            # ✅ Read credentials from Excel
            email = XLUtilis.readData(self.path, "Sheet1", r, 1)
            password = XLUtilis.readData(self.path, "Sheet1", r, 2)
            expected_status = XLUtilis.readData(self.path, "Sheet1", r, 3)  # ✅ Read Expected Result (Valid/Invalid)

            # ✅ Perform Login
            lp.setEmail(email)
            lp.setPassword(password)
            lp.clickLoginButton()
            self.logger.info(f"🔍 Trying to log in with: {email} | {password}")

            # ✅ Read Actual Messages **AFTER LOGIN**
            try:
                actual_success_message = lp.get_Loginpage_success_Message()  # ✅ Read success message
            except NoSuchElementException:
                actual_success_message = ""

            try:
                actual_fail_message = lp.get_Loginpage_fail_Message()  # ✅ Read fail message
            except NoSuchElementException:
                actual_fail_message = ""

            try:
                if expected_status.lower() == "valid":
                    if "Full-Fledged practice website for Automation Engineers" in actual_success_message:
                        self.logger.info(f"✅ Expected Valid Login - Login Successful")
                        logoutpage.clickLogoutButton()  # ✅ Logout only for valid users
                        XLUtilis.writeData(self.path, "Sheet1", r, 4, "PASS")  # ✅ Write result in Excel
                    else:
                        self.logger.error(f"❌ Valid Login Failed")
                        XLUtilis.writeData(self.path, "Sheet1", r, 4, "FAIL")

                else:  # **For Invalid Data**
                    if "Your email or password is incorrect!" in actual_fail_message:
                        self.logger.info(f"✅ Expected Invalid Login - Error Message Verified")
                        XLUtilis.writeData(self.path, "Sheet1", r, 4, "PASS")
                    else:
                        self.logger.error(f"❌ Expected Login Failure but Passed!")
                        XLUtilis.writeData(self.path, "Sheet1", r, 4, "FAIL")

            except NoSuchElementException:
                self.logger.error(f"❌ Element Not Found for {email}")
                XLUtilis.writeData(self.path, "Sheet1", r, 4, "FAIL")

            self.driver.refresh()  # ✅ Refresh browser for next test case

        self.driver.close()  # ✅ Close browser after all tests
        self.logger.info("***** Loginpage DDT Completed *****")

