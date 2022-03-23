import selenium
from functions.Functions import Functions as Selenium
from classes.FormLogin import EventLogin
from classes.PeticionJson import CaseInmofianza
import unittest

class CasosInmofianza(Selenium,unittest.TestCase): 
        
    def testCasosInmofianza(self):
        idCliente=Selenium.leer_celda(self, 'E2')
        #Arrendatario
        a_primerNombre=Selenium.leer_celda(self, 'F2')
        a_segundoNombre=Selenium.leer_celda(self, 'G2')
        a_primerApellido=Selenium.leer_celda(self, 'H2')
        a_segundoApellido=Selenium.leer_celda(self, 'I2')
        a_idTipoDocumento=Selenium.leer_celda(self, 'J2')
        a_numeroDocumento=Selenium.leer_celda(self, 'K2')
        a_contactoCelular=Selenium.leer_celda(self, 'L2')
        a_correoNotificaciones=Selenium.leer_celda(self, 'M2')
        a_fechaNacimiento=Selenium.leer_celda(self, 'N2')
        a_fechaExpedicionDocumento=Selenium.leer_celda(self, 'O2')
        a_ciudadExpedicionDocumento=Selenium.leer_celda(self, 'P2')
        #Deudor
        d_primerNombre=Selenium.leer_celda(self, 'S2')
        d_segundoNombre=Selenium.leer_celda(self, 'T2')
        d_primerApellido=Selenium.leer_celda(self, 'U2')
        d_segundoApellido=Selenium.leer_celda(self, 'V2')
        d_idTipoDocumento=Selenium.leer_celda(self, 'W2')
        d_numeroDocumento=Selenium.leer_celda(self, 'X2')
        d_contactoCelular=Selenium.leer_celda(self, 'Y2')
        d_correoNotificaciones=Selenium.leer_celda(self, 'Z2')
        d_fechaNacimiento=Selenium.leer_celda(self, 'AA2')
        d_fechaExpedicionDocumento=Selenium.leer_celda(self, 'AB2')
        d_ciudadExpedicionDocumento=Selenium.leer_celda(self, 'AC2')
        #Documentos
        nombreDocumento_a=Selenium.leer_celda(self, 'AF2')
        nombreDocumento_b=Selenium.leer_celda(self, 'AJ2')
        #Representante
        r_primerNombre=Selenium.leer_celda(self, 'AN2')
        r_segundoNombre=Selenium.leer_celda(self, 'AO2')
        r_primerApellido=Selenium.leer_celda(self, 'AP2')
        r_segundoApellido=Selenium.leer_celda(self, 'AQ2')
        r_razonSocial=Selenium.leer_celda(self, 'AR2')
        r_idTipoDocumento=Selenium.leer_celda(self, 'AS2')
        r_numeroDocumento=Selenium.leer_celda(self, 'AT2')
        r_ciudadDocumento=Selenium.leer_celda(self, 'AU2')
        r_numeroNit=Selenium.leer_celda(self, 'AV2')
        r_digitoVerificacion=Selenium.leer_celda(self, 'AW2')
        r_contactoCelular=Selenium.leer_celda(self, 'AX2')
        r_correoNotificaciones=Selenium.leer_celda(self, 'AY2')
        r_fechaNacimiento=Selenium.leer_celda(self, 'AZ2')
        r_fechaExpedicionDocumento=Selenium.leer_celda(self, 'BA2')    
        r_emailContactoInmobiliaria=Selenium.leer_celda(self, 'BC2')
        #Inmo
        i_primerNombre=Selenium.leer_celda(self, 'BD2')
        i_segundoNombre=Selenium.leer_celda(self, 'BE2')
        i_primerApellido=Selenium.leer_celda(self, 'BF2')
        i_segundoApellido=Selenium.leer_celda(self, 'BG2')
        i_razonSocial=Selenium.leer_celda(self, 'BH2')
        i_idTipoDocumento=Selenium.leer_celda(self, 'BI2')
        i_numeroDocumento=Selenium.leer_celda(self, 'BJ2')
        i_ciudadDocumento=Selenium.leer_celda(self, 'BK2')
        i_numeroNit=Selenium.leer_celda(self, 'BL2')
        i_digitoVerificacion=Selenium.leer_celda(self, 'BM2')
        i_contactoCelular=Selenium.leer_celda(self, 'BN2')
        i_correoNotificaciones=Selenium.leer_celda(self, 'BM2')
        i_fechaNacimiento=Selenium.leer_celda(self, 'BP2')
        i_fechaExpedicionDocumento=Selenium.leer_celda(self, 'BQ2')    
        i_emailContactoInmobiliaria=Selenium.leer_celda(self, 'BS2')
        #DatosInmueble
        direccionInmueble=Selenium.leer_celda(self, 'BT2')
        municipioInmueble=Selenium.leer_celda(self, 'BU2')
        inmobiliaria=Selenium.leer_celda(self, 'BV2')
        nombreAsesor=Selenium.leer_celda(self, 'BW2') 
        CaseInmofianza.AssembleJson(self,idCliente,a_primerNombre,a_segundoNombre,a_primerApellido,a_segundoApellido,a_idTipoDocumento,a_numeroDocumento,a_contactoCelular,a_correoNotificaciones,a_fechaNacimiento,a_fechaExpedicionDocumento,a_ciudadExpedicionDocumento,d_primerNombre,d_segundoNombre,d_primerApellido,d_segundoApellido,d_idTipoDocumento,d_numeroDocumento,d_contactoCelular,d_correoNotificaciones,d_fechaNacimiento,d_fechaExpedicionDocumento,d_ciudadExpedicionDocumento,nombreDocumento_a,nombreDocumento_b,r_primerNombre,r_segundoNombre,r_primerApellido,r_segundoApellido,r_razonSocial,r_idTipoDocumento,r_numeroDocumento,r_ciudadDocumento,r_numeroNit,r_digitoVerificacion,r_contactoCelular,r_correoNotificaciones,r_fechaNacimiento,r_fechaExpedicionDocumento,r_emailContactoInmobiliaria,i_primerNombre,i_segundoNombre,i_primerApellido,i_segundoApellido,i_razonSocial,i_idTipoDocumento,i_numeroDocumento,i_ciudadDocumento,i_numeroNit,i_digitoVerificacion,i_contactoCelular,i_correoNotificaciones,i_fechaNacimiento,i_fechaExpedicionDocumento,i_emailContactoInmobiliaria,direccionInmueble,municipioInmueble,inmobiliaria,nombreAsesor)

if __name__ == '__main__':
    unittest.main() 
