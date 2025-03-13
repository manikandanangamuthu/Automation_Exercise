from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class loginpage:


    #Locators

    txt_email_xpath="//input[@data-qa='login-email']"
    txt_password_xpath="//input[@placeholder='Password']"
    btn_login_xpath="//button[normalize-space()='Login']"
    text_loginSuccess_xpath="//div[@class='item active']//h2[contains(text(),'Full-Fledged practice website for Automation Engin')]"
    text_loginFail_message="//p[normalize-space()='Your email or password is incorrect!']"

    #Constructors

    def __init__(self,driver):
        self.driver=driver

    #Methods

    def setEmail(self,email):

        Email=WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.txt_email_xpath))
        )
        #Email=self.driver.find_element(By.XPATH,self.txt_email_xpath)
        Email.clear()
        Email.send_keys(email)

    def setPassword(self,password):
        Password=self.driver.find_element(By.XPATH,self.txt_password_xpath)
        Password.clear()
        Password.send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def get_Loginpage_success_Message(self):
        self.driver.find_element(By.XPATH,self.text_loginSuccess_xpath).text()

        # try:
        #     return self.driver.find_element(By.XPATH,self.text_message_xpath).is_displayed()
        # except:
        #     return False

    def get_Loginpage_fail_Message(self):
        self.driver.find_element(By.XPATH,self.text_loginFail_message).text()


