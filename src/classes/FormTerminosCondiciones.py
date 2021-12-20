import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from functions.Functions import Functions as Selenium

class EventTerminosCondiciones(unittest.TestCase):

    def AceptarTratamientoDatos(self):        
        Selenium.get_json_file(self,"TerminosCondicion")
        #Selenium.assert_text(self,'TratamientoDatosPersonales','TRATAMIENTO DE DATOS PERSONALES')
        #Selenium.esperar(self,2)
        #Selenium.get_elements(self, "btnAceptar").click()
        #Selenium.esperar(self,2)
        #Selenium.get_elements(self, "GuardarFlujo1").click()
        # Selenium.esperar(self,2)
        # Selenium.assert_text(self, 'EnrolamientoFacial','DATOS PERSONALES Y ENROLAMIENTO FACIAL')
        # Selenium.esperar(self,2)
        # Selenium.get_elements(self, "btnAceptar").click()
        # Selenium.esperar(self,2)
        # Selenium.get_elements(self, "GuardarFlujo2").click()
        # Selenium.esperar(self,2)
        # Selenium.assert_text(self, 'HabeasData','ACUERDO DE FIRMA ELECTRÓNICA')
        # Selenium.esperar(self,2)
        # Selenium.get_elements(self, "btnAceptar").click()
        # Selenium.esperar(self,2)
        # Selenium.get_elements(self, "GuardarFlujo3").click()




