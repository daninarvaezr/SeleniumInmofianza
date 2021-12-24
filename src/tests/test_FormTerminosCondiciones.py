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

    def testTerminosCondiciones_Aceptar(self):
        Cedula=Selenium.leer_celda(self, 'K3')
        EventLogin.Loguin(self,Cedula,Cedula)
        EventTC.AceptarTratamientoDatos(self)
        EventTC.AceptarEnrolamiento(self)
        EventTC.AceptarFirmaElectronica(self)
        Selenium.esperar(self, 2)
        Selenium.assert_text(self, 'AsersionTituloAprobacionDoc','VISUALIZACIÓN Y APROBACIÓN DE DOCUMENTOS')

    def testTratamientoDatos_Rechazado(self):
        Cedula=Selenium.leer_celda(self, 'K4')
        EventLogin.Loguin(self,Cedula,Cedula)
        EventTC.RechazarTratamientoDatos(self)
        
        Selenium.esperar(self, 2)


    def testEnrolamiento_Rechazado(self):
        Cedula=Selenium.leer_celda(self, 'K5')
        EventLogin.Loguin(self,Cedula,Cedula)
        Selenium.esperar(self, 2)
        EventTC.AceptarTratamientoDatos(self)
        Selenium.esperar(self, 2)
        EventTC.RechazarEnrolamientoFacial(self)
        Selenium.esperar(self, 2)

    def testFirmaElectronica_Rechazado(self):
        Cedula=Selenium.leer_celda(self, 'K6')
        EventLogin.Loguin(self,Cedula,Cedula)
        Selenium.esperar(self, 2)
        EventTC.AceptarTratamientoDatos(self)
        Selenium.esperar(self, 2)
        EventTC.AceptarEnrolamiento(self)
        Selenium.esperar(self, 2)
        EventTC.RechazarFirmaElectronica(self)
        Selenium.esperar(self, 2)
        
if __name__ == '__main__':
    unittest.main()