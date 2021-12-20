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
        Selenium.get_elements(self,"Revisar").click()        
        #Selenium.close_windows_name(self,'ViewDocPDF')               
        Selenium.switch_to_windows_name(self,'OMNICANALIDAD')
        Selenium.esperar(self,3)                   
        Selenium.get_elements(self,"Seleccionar").click()                            
        Selenium.capturar_pantalla(self)
        Selenium.get_elements(self,"Siguiente").click()
        Selenium.get_elements(self,"BtnAceptar").click()
        Selenium.esperar(self,3000000)
    def RechazarDocumento(self):        
        EventTC.AceptarTratamientoDatos(self)
        Selenium.get_json_file(self,"AprobacionDocumentos")
        Selenium.get_elements(self,"Revisar").click()        
        #Selenium.close_windows_name(self,'ViewDocPDF')               
        Selenium.switch_to_windows_name(self,'OMNICANALIDAD')
        Selenium.esperar(self,3)                   
        Selenium.get_elements(self,"Seleccionar").click()                            
        Selenium.capturar_pantalla(self)
        Selenium.get_elements(self,"Siguiente").click()
        Selenium.get_elements(self,"BtnAceptar").click()
        Selenium.esperar(self,3000000)        
        
        #Selenium.esperar(self,1000000)

