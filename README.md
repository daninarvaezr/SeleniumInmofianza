# Selenium Inmofianza

_Proyecto de pruebas automatizadas con selenium webdriver para el aplicativo Omnicanalidad_

## Pre-requisitos 📋

_Se recominda instalar los siguientes componentes mediante el archivo requirements.txt con el siguiente comando_ **pip install -r requirements.txt**

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


_Crear un archivo_ **config.ini** _ubicado en la  siguiente ruta src\data\config.ini con la siguiente estructura y agregar los parametros de conectividad necesarios_
```
[QA-Omnicanalidad]
DB_HOST = db_host
DB_NAME = db_name
DB_USER = db_user
DB_PASSWORD = db_password
RUTA_CHROME = ruta_chrome.exe
USERTOKEN = Usuario
PASSWORD_TOKEN = Clave
APLICATION_TOKEN = Aplicacion
```

_Crear ambiente virtual en la raiz del proyecto con el comando_ **virtualenv Enviroment** _Seguido a esto activarlo ejecutando el archivo activate.bat ubicado en la ruta Enviroment/Scripts/_
 

## Comenzar 🚀

_Desde visual Studio code puedes ejecutar el archivo:_ **projectSeleniumInmofianza.py**
o activar el entorno virtua por consola y ejecutar el archivo antes mencionado


## Construido con 🛠️

_El presente proyecto esta construido en lenguaje python con la libreria de webdriber de Selenium_


## Autores ✒️

* **Natalia Narvaez** - *Analista QA* - [NataliaNarvaez](https://github.com/daninarvaezr)
* **Daniel Duran** - *Analista QA* - [DaniDuran](https://github.com/DaniDuran)


## Expresiones de Gratitud 🎁
