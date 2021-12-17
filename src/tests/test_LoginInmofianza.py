import selenium
from functions.Functions import Functions as Selenium
from classes.login import EventLoginInmofianza  as EventLogin
import unittest

class LoginInmofianza(Selenium,unittest.TestCase): 

    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.get_json_file(self,"LoginInmofianza")
        Selenium.get_json_file(self,"TerminosCondicion")
        self.driver.maximize_window()
                   
    def testLoginInmofianza_AccesoDenegado(self):
        EventLogin.Logueo(self,1013699960,1013699960)
    def testLoginInmofianza_AccesoCorrecto(self):
        EventLogin.Logueo(self,1013665960,1013665960)        
        Selenium.assert_text(self, 'Titulo_1', 'DATOS PERSONALES Y ENROLAMIENTO FACIAL')                                                                                 
                 
    if __name__ == '__main__':
        unittest.main()
