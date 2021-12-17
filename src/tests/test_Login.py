import selenium
from functions.Functions import Functions as Selenium
from classes.FormLogin import EventLogin as EventLogin
import unittest

class LoginInmofianza(Selenium,unittest.TestCase): 

    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.get_json_file(self,"LoginInmofianza")
        #Selenium.get_json_file(self,"TerminosCondicion")
        self.driver.maximize_window()
                   
    def testLoginInmofianza_AccesoDenegado(self):
        EventLogin.Logueo(self,1013699,10136999)
        Selenium.assert_text(self, 'AsersionMensajeErrorUsuario', 'Usuario o contraseña incorrecto')
    def testLoginInmofianza_AccesoCorrecto(self):
        EventLogin.Logueo(self,1013665960,1013665960)
        Selenium.esperar(self, 10)        
        Selenium.assert_text(self, 'Asersion_TituloTerminosCondiciones', 'TRATAMIENTO DE DATOS PERSONALES')                                                                                         
                 
    if __name__ == '__main__':
        unittest.main() 
