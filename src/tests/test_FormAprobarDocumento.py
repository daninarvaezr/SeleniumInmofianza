import selenium
from functions.Functions import Functions as Selenium
import unittest
from classes.FormLogin import EventLogin
from classes.FormTerminosCondiciones import EventTerminosCondiciones as EventTC
from classes.FormAprobacionDocumentos import EventAprobarDocumentos as EventAD

class AprobacionDocumento(Selenium,unittest.TestCase): 

    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.get_json_file(self,"AprobacionDocumentos")
        self.driver.maximize_window()

    def testAprobarDocumento(self):
        EventLogin.Loguin(self,1013665963,1013665963)
        EventTC.AceptarTratamientoDatos(self)
        EventAD.AprobacionDocumento(self)
        Selenium.esperar(self, 2)

    if __name__ == '__main__':
        unittest.main()
