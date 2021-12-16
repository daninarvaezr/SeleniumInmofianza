import selenium
from functions.Functions import Functions as Selenium
import unittest

class LoginInmofianza(Selenium,unittest.TestCase): 

    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.get_json_file(self,"LoginInmofianza")
        self.driver.maximize_window()
                   
    def testLoginInmofianza(self):
          for row in Selenium.all_rows(self):
             if row[0].value:
                 Selenium.get_elements(self, "Username").send_keys(123)              
                 Selenium.esperar(self, 2)
                 Selenium.get_elements(self, "Password").send_keys(123)                         
                 Selenium.esperar(self, 2)
                 Selenium.get_elements(self, "IniciarSesion").click()   
                 Selenium.esperar(self, 5)                 
                 Selenium.assert_text(self, 'AsersionMensajeErrorUsuario', 'Usuario o contraseña incorrecto')                                                        
                 
    if __name__ == '__main__':
        unittest.main()
