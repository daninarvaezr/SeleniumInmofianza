import selenium
from functions.Functions import Functions as Selenium
import unittest
from classes.login import EventLoginInmofianza  as EventLogin

class TratamientoDatos(Selenium,unittest.TestCase): 

    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.get_json_file(self,"TratamientoDatos")
        self.driver.maximize_window()
                   
    def testTerminosCondiciones(self):
        EventLogin.Logueo(self,1013699960,1013699960)              
        Selenium.esperar(self, 2)                
        Selenium.assert_text(self, 'Titulo_1', 'DATOS PERSONALES Y ENROLAMIENTO FACIAL')
        Selenium.esperar(self, 2)
        
                                      
                                                                       
                 
    if __name__ == '__main__':
        unittest.main()
