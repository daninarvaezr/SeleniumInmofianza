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
        self.driver = webdriver.Chrome(executable_path=r"C:\\Users\\danie\\OneDrive\\Documentos\\Selenium\\Inmofianza\\Selenium_Inmofianza\\chromedriver.exe",chrome_options=options)

        
    def test_page(self):
        driver = self.driver
        driver.get('https://seguroqa.thomasgreg.com/Omnicanalidad/Login?id=MQAzADkAMQA5AA==')
        self.assertIn("OMNICANALIDAD",driver.title)        
        for i  in  [1,2,3]:
        print('input#verificarFlujo'+str(i))  
        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input#btnAceptar')))\
            .click()
        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input#verificarFlujo'+str(i))))\
            .click()

        
        time.sleep(15)
        assert "No se encontro elemento: " not in driver.page_source
        
    def tearDown(self):
        self.driver.close()

if __name__ =='__main__':
    unittest.main()
        
        
        

    