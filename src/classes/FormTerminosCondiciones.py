import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from functions.Functions import Functions as Selenium


class EventTerminosCondiciones(unittest.TestCase):

    def AceptarTratamientoDatos(self):
        Selenium.get_json_file(self,"TerminosCondicion")
        Selenium.assert_text(self,'TratamientoDatosPersonales','TRATAMIENTO DE DATOS PERSONALES')
        Selenium.esperar(self,2)
        Selenium.get_elements(self, "btnAceptar").click()
        Selenium.esperar(self,2)
        Selenium.get_elements(self, "GuardarFlujo1").click()
        Selenium.esperar(self,2)
        Selenium.assert_text(self, 'EnrolamientoFacial','DATOS PERSONALES Y ENROLAMIENTO FACIAL')
        Selenium.esperar(self,2)

    def AceptarEnrolamiento(self):
        Selenium.get_json_file(self,"TerminosCondicion")
        Selenium.assert_text(self, 'EnrolamientoFacial','DATOS PERSONALES Y ENROLAMIENTO FACIAL')
        Selenium.get_elements(self, "btnAceptar").click()
        Selenium.esperar(self,2)
        Selenium.get_elements(self, "GuardarFlujo2").click()
        Selenium.esperar(self,2)
        Selenium.assert_text(self, 'HabeasData','ACUERDO DE FIRMA ELECTRÓNICA')
        Selenium.esperar(self,2)

    def AceptarFirmaElectronica(self):
        Selenium.get_json_file(self,"TerminosCondicion")
        Selenium.assert_text(self, 'HabeasData','ACUERDO DE FIRMA ELECTRÓNICA')
        Selenium.get_elements(self, "btnAceptar").click()
        Selenium.esperar(self,2)
        Selenium.get_elements(self, "GuardarFlujo3").click()
        Selenium.esperar(self,2)

    def RechazarTratamientoDatos(self):
        Selenium.get_json_file(self,"TerminosCondicion")
        Selenium.esperar(self,2)
        Selenium.get_elements(self, "btnRechazar").click()
        Selenium.esperar(self,2)
        Selenium.get_elements(self,"btnAceptarModal").click()
        Selenium.esperar(self,2)
        Selenium.get_elements(self,"btnVolverModal").click()
        Selenium.esperar(self,2)
        Selenium.get_json_file(self,"Login")
        Selenium.assert_text(self, 'AsersionLogin','Ingreso de Usuario')
        Selenium.esperar(self,2)

    def RechazarEnrolamientoFacial(self):
        EventTerminosCondiciones.AceptarTratamientoDatos(self)
        Selenium.get_json_file(self,"TerminosCondicion")
        Selenium.esperar(self,2)
        Selenium.get_elements(self, "btnRechazar").click()
        Selenium.esperar(self,2)
        Selenium.get_elements(self,"btnAceptarModal").click()
        Selenium.esperar(self,2)
        Selenium.get_elements(self,"btnVolverModal").click()
        Selenium.esperar(self,2)
        Selenium.get_json_file(self,"Login")
        Selenium.assert_text(self, 'AsersionLogin','Ingreso de Usuario')
        Selenium.esperar(self,2)

    def RechazarFirmaElectronica(self):
        EventTerminosCondiciones.AceptarTratamientoDatos(self)
        EventTerminosCondiciones.AceptarEnrolamiento(self)
        Selenium.get_json_file(self,"TerminosCondicion")
        Selenium.get_elements(self, "btnRechazar").click()
        Selenium.esperar(self,2)
        Selenium.get_elements(self,"btnAceptarModal").click()
        Selenium.esperar(self,2)
        Selenium.get_elements(self,"btnVolverModal").click()
        Selenium.esperar(self,2)
        Selenium.get_json_file(self,"Login")
        Selenium.assert_text(self, 'AsersionLogin','Ingreso de Usuario')
        Selenium.esperar(self,2)
