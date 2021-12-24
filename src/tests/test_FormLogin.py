import selenium
from functions.Functions import Functions as Selenium
from classes.FormLogin import EventLogin
import unittest

class LoginInmofianza(Selenium,unittest.TestCase): 

    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.get_json_file(self,"Login")        
        self.driver.maximize_window()
                   
    def testLogin_AccesoDenegado(self):
        Cedula=Selenium.leer_celda(self, 'K1')
        EventLogin.Loguin(self,Cedula,Cedula)
        Selenium.assert_text(self, 'AsersionMensajeErrorUsuario', 'Usuario o contraseña incorrecto')
    def testLogin_AccesoCorrecto(self):
        Cedula=Selenium.leer_celda(self, 'K2')
        EventLogin.Loguin(self,Cedula,Cedula)
        Selenium.esperar(self, 10)        
        Selenium.assert_text(self, 'AsersionTituloTerminosCondiciones', 'TRATAMIENTO DE DATOS PERSONALES')                                                                                         
                 
if __name__ == '__main__':
    unittest.main() 
