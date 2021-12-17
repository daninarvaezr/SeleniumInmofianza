import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from functions.Functions import Functions as Selenium
from classes.FormLogin import EventLogin
from classes.FormTerminosCondiciones import EventTerminosCondiciones as EventTC
class EventAprobarDocumentos(unittest.TestCase):
    def AprobacionDocumento(self):
        EventLogin.Loguin(self,1013665963,1013665963)
        EventTC.AceptarTratamientoDatos(self)
        Selenium.get_json_file(self,"AprobacionDocumentos")
        Selenium.esperar(self,2)
        # Selenium.get_elements(self,"Seleccionar").isSelected()
        Selenium.esperar(self,10000)

