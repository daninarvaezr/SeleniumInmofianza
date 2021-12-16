import os

class Inicializar():
    # Directorio Base
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    # JsonData
    Json = basedir + u"/pages"

    # BROWSER DE PRUEBAS
    NAVEGADOR = u'CHROME'

    # DIRECTORIO DE LA EVIDENCIA
    Path_Evidencias = basedir + u'/data/capturas'

    # HOJA DE DATOS EXCEL
    Excel = basedir + u'/data/ArchivoConfig.xlsx'

    Environment = 'QA'

    if Environment == 'QA':
        URL = 'https://seguroqa.thomasgreg.com/Omnicanalidad/Login?id=MQAzADkAMQA5AA=='
        mailuser = ''
        mailpassword = ''
        DB_HOST = ''
        DB_PORT = ''
        DB_DATABASE = ''
        DB_USER = ''
        DB_PASS = ''