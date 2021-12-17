import selenium
from functions.Functions import Functions as Selenium
import unittest
class EventLogin():

    def Loguin(self,UserName,Password):
        #   for row in Selenium.all_rows(self):
        #      if row[0].value:}
        Selenium.get_json_file(self,"Login")
        Selenium.get_elements(self, "User").send_keys(UserName)
        Selenium.esperar(self, 2)
        Selenium.get_elements(self, "Password").send_keys(Password)
        Selenium.esperar(self, 2)
        Selenium.get_elements(self, "IniciarSesion").click()
        Selenium.esperar(self, 5)
