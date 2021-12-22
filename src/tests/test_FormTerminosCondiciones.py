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
        EventLogin.Loguin(self,1013665963,1013665963) #pendiente cambiar documento
        EventTC.RechazarTratamientoDatos(self)
        Selenium.esperar(self, 2)
        Selenium.assert_text(self, 'AsersionLogin','Ingreso de Usuario')

    def testRechazarEnrolamiento(self):
        EventLogin.Loguin(self,1013665963,1013665963) #pendiente cambiar documento
        EventTC.AceptarTratamientoDatos(self)
        EventTC.RechazarEnrolamientoFacial(self)
        Selenium.esperar(self, 2)
        Selenium.assert_text(self, 'AsersionLogin','Ingreso de Usuario')

    def testRechazarFirmaElectronica(self):
        EventLogin.Loguin(self,1013665964,1013665964) #pendiente cambiar documento
        #EventTC.AceptarTratamientoDatos(self)
        #EventTC.AceptarEnrolamiento(self)
        Selenium.esperar(self, 2)
        EventTC.RechazarFirmaElectronica(self)
        Selenium.esperar(self, 2)
        #Selenium.assert_text(self, 'AsersionLogin','Ingreso de Usuario')




    if __name__ == '__main__':
        unittest.main()
