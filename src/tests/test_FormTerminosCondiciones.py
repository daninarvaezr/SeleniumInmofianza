import selenium
from functions.Functions import Functions as Selenium
import unittest
from classes.FormTerminosCondiciones import EventTerminosCondiciones as EventTC

class TratamientoDatos(Selenium,unittest.TestCase): 

    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.get_json_file(self,"Login")
        Selenium.get_json_file(self,"TerminosCondicion")
        self.driver.maximize_window()

    def testTerminosCondiciones(self):
        EventTC.AceptarTratamientoDatos(self)
        Selenium.esperar(self, 2)
        Selenium.assert_text(self, 'AsersionTituloAprobacionDoc','VISUALIZACIÓN Y APROBACIÓN DE DOCUMENTOS')

    if __name__ == '__main__':
        unittest.main()
