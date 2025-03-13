from selenium.webdriver.common.by import By




class homepage():

    #Locators
    btn_Signup_Login_xpath="//a[normalize-space()='Signup / Login']"

    # Constructors
    def __init__(self,driver):
        self.driver=driver


    #methods

    def click_Signup_login_button(self):
        self.driver.find_element(By.XPATH, self.btn_Signup_Login_xpath).click()
