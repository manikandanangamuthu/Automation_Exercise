
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignUp:

    #Locators
     txt_name_xpath="//input[@name='name']"
     txt_email_xpath="//input[@data-qa='signup-email']"
     btn_sinup_xpath="//button[@data-qa='signup-button']"
     btn_title_xpath="//input[@id='id_gender1']"
     txt_password_xpath="//input[@id='password']"
     dropdown_day_xpath="//select[@id='days']"
     dropdown_month_xpath="//select[@id='months']"
     dropdown_year_xpath="//select[@id='years']"
     txt_firstname_xpath="//input[@id='first_name']"
     txt_lastname_xpath="//input[@id='last_name']"
     txt_company_xpath="//input[@id='company']"
     txt_address1_xpath="//input[@id='address1']"
     txt_address2_xpath="//input[@id='address2']"
     dropdown_country_xpath="//select[@id='country']"
     txt_state_xpath="//input[@id='state']"
     txt_city_xpath="//input[@id='city']"
     txt_zipcode_xpath="//input[@id='zipcode']"
     txt_phoneNumber_xpath="//input[@id='mobile_number']"
     btn_createAccount_xpath="//button[normalize-space()='Create Account']"
     confm_message="//b[normalize-space()='Account Created!']"

    #Constructors
     def __init__(self,driver):
         self.driver=driver

    #Methods
     def setUserName(self,name):
         username=self.driver.find_element(By.XPATH,self.txt_name_xpath)
         username.clear()
         username.send_keys(name)

     def setEmailId(self,email):
         useremail=self.driver.find_element(By.XPATH,self.txt_email_xpath)
         useremail.clear()
         useremail.send_keys(email)

     def clickSignUpButton(self):
         self.driver.find_element(By.XPATH,self.btn_sinup_xpath).click()


     def select_Title(self):
         self.driver.find_element(By.XPATH,self.btn_title_xpath).click()

     def setPassword(self,password):
         userPassword=self.driver.find_element(By.XPATH,self.txt_password_xpath)
         userPassword.clear()
         userPassword.send_keys(password)

     def select_date_of_birth(self,day,month,year):
         day_dropdown=Select(self.driver.find_element(By.XPATH,self.dropdown_day_xpath))
         month_dropdown=Select(self.driver.find_element(By.XPATH,self.dropdown_month_xpath))
         year_dropdown=Select(self.driver.find_element(By.XPATH,self.dropdown_year_xpath))

         day_dropdown.select_by_visible_text(str(day))
         month_dropdown.select_by_visible_text(month)
         year_dropdown.select_by_visible_text(str(year))

     def setFirstName(self,firstname):
         FirstName=self.driver.find_element(By.XPATH,self.txt_firstname_xpath)
         FirstName.clear()
         FirstName.send_keys(firstname)

     def setLastName(self,lastname):
         LastName=self.driver.find_element(By.XPATH,self.txt_lastname_xpath)
         LastName.clear()
         LastName.send_keys(lastname)

     def setCompany(self,company):
         CompanyName=self.driver.find_element(By.XPATH,self.txt_company_xpath)
         CompanyName.clear()
         CompanyName.send_keys(company)

     def setAddress1(self,address):
         Address1=self.driver.find_element(By.XPATH,self.txt_address1_xpath)
         Address1.clear()
         Address1.send_keys(address)

     def setAddress2(self,address2):
         Address2=self.driver.find_element(By.XPATH,self.txt_address2_xpath)
         Address2.clear()
         Address2.send_keys(address2)

     def selectCountry(self,county):
         Country=Select(self.driver.find_element(By.XPATH,self.dropdown_country_xpath))
         Country.select_by_visible_text(county)

     def setState(self,state):
         State=self.driver.find_element(By.XPATH,self.txt_state_xpath)
         State.clear()
         State.send_keys(state)

     def setCity(self,city):
         City=self.driver.find_element(By.XPATH,self.txt_city_xpath)
         City.clear()
         City.send_keys(city)

     def setZipcode(self,zipcode):
         Zipcode=self.driver.find_element(By.XPATH,self.txt_zipcode_xpath)
         Zipcode.clear()
         Zipcode.send_keys(zipcode)

     def setMobilenumber(self,mobilenumber):
         MobileNumber=self.driver.find_element(By.XPATH,self.txt_phoneNumber_xpath)
         MobileNumber.clear()
         MobileNumber.send_keys(mobilenumber)

     def clickCreateAccountButton(self):
          CreateAccountBuuton=self.driver.find_element(By.XPATH,self.btn_createAccount_xpath)
          CreateAccountBuuton.click()

     def getconfirm_Message(self):
         try:
             msg_element=WebDriverWait(self.driver, 5).until(
                 EC.visibility_of_element_located((By.XPATH,self.confm_message))
             )
             message=msg_element.text
             return message
         except:
             return ""



