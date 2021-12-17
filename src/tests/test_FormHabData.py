import selenium
from functions.Functions import Functions as Selenium
import unittest

class FormHabeasData(Selenium,unittest.TestCase): 

    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.get_json_file(self,"FormHabeasData")
        self.driver.maximize_window()
                   
    def testFormHabData(self):
          for row in Selenium.all_rows(self):
             if row[0].value:
                 Selenium.get_elements(self, "Aceptar").click()              
                 Selenium.esperar(self, 2)
                 Selenium.get_elements(self, "Guardar").click()                        
                 Selenium.esperar(self, 2)                                
                                                                       
                 
    if __name__ == '__main__':
        unittest.main()
