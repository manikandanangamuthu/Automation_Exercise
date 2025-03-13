from selenium.webdriver.common.by import By


class logout:


    #Locators
    btn_logout_xpath = "//a[normalize-space()='Logout']"

    #Constructors
    def __init__(self,driver):
        self.driver=driver

    #Methods

    def clickLogoutButton(self):
        self.driver.find_element(By.XPATH, self.btn_logout_xpath).click()



