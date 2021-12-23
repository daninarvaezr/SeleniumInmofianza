import selenium
from functions.Functions import Functions as Selenium
import unittest
from classes.FormLogin import EventLogin
from classes.FormTerminosCondiciones import EventTerminosCondiciones as EventTC

class TratamientoDatos(Selenium,unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.get_json_file(self,"TerminosCondicion")
        self.driver.maximize_window()

    def testTerminosCondiciones(self):
        EventLogin.Loguin(self,1013665963,1013665963)
        EventTC.AceptarTratamientoDatos(self)
        EventTC.AceptarEnrolamiento(self)
        EventTC.AceptarFirmaElectronica(self)
        Selenium.esperar(self, 2)
        Selenium.assert_text(self, 'AsersionTituloAprobacionDoc','VISUALIZACIÓN Y APROBACIÓN DE DOCUMENTOS')

    def testRechazarTratamientoDatos(self):
        EventLogin.Loguin(self,101366451,101366451)
        EventTC.RechazarTratamientoDatos(self)
        EventLogin.Loguin(self,101366451,101366451)
        Selenium.esperar(self, 2)


    def testRechazarEnrolamiento(self):
        EventLogin.Loguin(self,101366453,101366453)
        EventTC.RechazarEnrolamientoFacial(self)
        EventLogin.Loguin(self,101366453,101366453) # pte realizar las funciones en el login ( bloqueo)
        Selenium.esperar(self, 2)

    def testRechazarFirmaElectronica(self):
        EventLogin.Loguin(self,101366450,101366450)
        EventTC.RechazarFirmaElectronica(self)
        EventLogin.Loguin(self,101366450,101366450)
        Selenium.esperar(self, 2)
        
    if __name__ == '__main__':
        unittest.main()
