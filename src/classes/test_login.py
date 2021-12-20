import unittest 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time 

class Login(unittest.TestCase): 


    def setUp(self): 
                # Opciones de navegación
        
        options =  webdriver.ChromeOptions() 
        options.add_argument('--start-maximized')         
        options.add_argument('--disable-extensions') 
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\daniela.narvaez\QA\INMOFIANZA_SELENIUM\Selenium_Inmofianza\chromedriver.exe",chrome_options=options)


    def test_inicio(self):
        driver = self.driver
        driver.get('https://seguroqa.thomasgreg.com/Omnicanalidad/Login?id=MQAzADkAMQA5AA==')
        self.assertIn("OMNICANALIDAD",driver.title)
        inputUsuario = driver.find_element_by_id("txtUsuario") 
        inputClave = driver.find_element_by_name("txtPwd") 
        ButtonIniciar = driver.find_element_by_css_selector("button#btnnLogin") 
        inputUsuario.send_keys('123') 
        inputClave.send_keys('123') 
        ButtonIniciar.send_keys(Keys.ENTER) 
        time.sleep(15) 
        assert "No se encontro elemento: " not in driver.page_source

        
    def tearDown(self):
        self.driver.close()

if __name__ =='__main__':
    unittest.main()
        
        
        

    