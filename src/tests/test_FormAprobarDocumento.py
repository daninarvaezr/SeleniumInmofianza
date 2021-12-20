import selenium
from functions.Functions import Functions as Selenium
import unittest
from classes.FormAprobacionDocumentos import EventAprobarDocumentos as EventAD
from classes.FormLogin import  EventLogin
from classes.FormTerminosCondiciones import EventTerminosCondiciones as EventTC
class AprobacionDocumento(Selenium,unittest.TestCase): 

    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.get_json_file(self,"AprobacionDocumentos")
        self.driver.maximize_window()

    def testAprobarbDocumento(self):
        EventLogin.Loguin(self,1013665963,1013665963)
        EventTC.AceptarTratamientoDatos(self)
        EventAD.VerificarDocumento(self)
        Selenium.esperar(self, 2)
        EventAD.AceptarDocumento(self)
        Selenium.esperar(self, 2)

    if __name__ == '__main__':
        unittest.main()
