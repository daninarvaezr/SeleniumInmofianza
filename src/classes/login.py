class LoginFront():

    def login(self, Selenium):
           for row in Selenium.all_rows(self):
             if row[0].value:
                 Selenium.get_elements(self, "Username").send_keys(row[0].value)              
                 Selenium.get_elements(self, "Password").send_keys(row[1].value)                         
                 Selenium.get_elements(self, "IniciarSesion").click() 
                 Selenium.esperar(self, 2)      
                 Selenium.get_elements(self, "SelecCliente").click()                    
                 Selenium.esperar(self, 2)   
                 Selenium.get_elements(self, "BuscaCliente").send_keys(row[2].value)    
                 Selenium.esperar(self, 5)                                                                  
                 Selenium.get_elements(self, "ClicRadioButton").click()   
                 Selenium.esperar(self, 5)              
                 Selenium.get_elements(self, "ClicAceptar").click()    
                 
                 