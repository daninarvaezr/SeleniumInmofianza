import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from functions.Functions import Functions as Selenium
from classes.FormLogin import EventLogin
from classes.FormTerminosCondiciones import EventTerminosCondiciones as EventTC


class EventAprobarDocumentos(unittest.TestCase):
    def AprobacionDocumento(self):                
        EventTC.AceptarTratamientoDatos(self)
        Selenium.get_json_file(self,"AprobacionDocumentos")
        Selenium.esperar(self,2)                
        Selenium.get_elements(self, "Seleccionar").click() 
        
        
        Selenium.esperar(self,2)

