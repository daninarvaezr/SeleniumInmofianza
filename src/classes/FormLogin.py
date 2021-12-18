import selenium
from functions.Functions import Functions as Selenium
import unittest

class EventLogin():

    def Loguin(self,UserName,Password):
        #self.driver = webdriver.Chrome(executable_path=r"C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe")
        #driver = self.driver
        #driver.find_element_by_name('gv_Docs$ctl02$chk_sel').click()       
        Selenium.get_json_file(self,"Login")
        Selenium.get_elements(self, "User").send_keys(UserName)
        Selenium.esperar(self, 2)
        Selenium.get_elements(self, "Password").send_keys(Password)
        Selenium.esperar(self, 2)
        Selenium.get_elements(self, "IniciarSesion").click()
        
