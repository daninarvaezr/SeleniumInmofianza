# Selenium Inmofianza

_Proyecto de pruebas automatizadas con selenium webdriver para el aplicativo Omnicanalidad_

## Pre-requisitos 📋

_Se debe tener instalado python y el paquete pip adicional a esto se debe instalar los siguientes componentes mediante el archivo requirements.txt con el siguiente comando_ **pip install -r requirements.txt**

* allure-python-commons
* atomicwrites
* attrs
* backports.entry-points-selectable
* behave
* colorama
* distlib
* et-xmlfile
* filelock
* imap-tools
* importlib-metadata
* jdcal
* more-itertools
* openpyxl
* packaging
* parse
* parse-type
* platformdirs
* pluggy
* psycopg2
* py
* pyodbc
* pyparsing
* pytest
* selenium
* six
* requests
* unittest-xml-reporting
* urllib3
* virtualenv
* wcwidth
* zipp


_Crear un archivo_ **Inicializar.py** _ubicado en la  siguiente ruta src\functions\ con la siguiente estructura y agregar los parametros de conectividad necesarios o configuraciones personalizadas que requiera el ambiente segun el equipo_
```
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
        URL = ''
        URL_DEUDOR = ''
        URL_TOKEN = ''
        URL_CASOS =''
        DB_HOST = ''
        DB_PORT = ''
        DB_DATABASE = ''
        DB_USER = ''
        DB_PASS = ''
        USER_TOKEN = ''
        PASSWORD_TOKEN = ''
        APLICATION_TOKEN = ''
        RUTA_CHROME = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
        MAILUSER = ''
        MAILPASSWORD = ''

```

_Crear ambiente virtual en la raiz del proyecto con el comando_ **python -m virtualenv Enviroment** ó **python -m venv + nombre del ambiente** _Seguido a esto activarlo ejecutando el archivo activate.bat ubicado en la ruta Enviroment/Scripts o ejecutando el siguiente comando en la terminal_ **./Enviroment/Scripts/activate.bat**
 

## Comenzar 🚀

_Desde visual Studio code puedes ejecutar el archivo:_ **projectSeleniumInmofianza.py**
_o activar el entorno virtua por consola y ejecutar el archivo antes mencionado_


## Construido con 🛠️

_El presente proyecto esta construido en lenguaje python con la libreria de webdriber de Selenium_


## Autores ✒️

* **Natalia Narvaez** - *Analista QA* - [NataliaNarvaez](https://github.com/daninarvaezr)
* **Daniel Duran** - *Analista QA* - [DaniDuran](https://github.com/DaniDuran)


## Expresiones de Gratitud 🎁
