import selenium
from functions.Functions import Functions as Selenium
import unittest

class EventLoginInmofianza():

    def Logueo(self,Username,Password):
          for row in Selenium.all_rows(self):
             if row[0].value:
                 Selenium.get_elements(self, "Username").send_keys(Username)              
                 Selenium.esperar(self, 2)
                 Selenium.get_elements(self, "Password").send_keys(Password)                         
                 Selenium.esperar(self, 2)
                 Selenium.get_elements(self, "IniciarSesion").click()   
                 Selenium.esperar(self, 5)            
                 
                 
                 