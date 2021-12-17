# Selenium Inmofianza

_Proyecto de pruebas automatizadas con selenium webdriver para el aplicativo Omnicanalidad_

## Pre-requisitos 📋

_Componentes que deben estar instalados_
* virtualenv: pip install virtualenv
* selenium: pip install -U selenium
* pyodbc: pip install pyodbc
* openpyxl: pip install openpyxl
* imap-tools: pip install imap-tools
* psycopg2: pip install psycopg2
* smtplib: pip install secure-smtplib
* pytest: pip install pytest
* json: pip install jsonlib
* configparser: pip install configparser
* requests: pip install requests

_Crear un archivo_ **config.ini** _ubicado en la  siguiente ruta src\data\config.ini con la siguiente estructura y agregar los parametros de conectividad necesarios_
```
[QA-Omnicanalidad]
DB_HOST = db_host
DB_NAME = db_name
DB_USER = db_user
DB_PASSWORD = db_password
RUTA_chrome = ruta_chrome.exe
UserToken = Usuario
PasswordToken = Clave
AplicationToken = Aplicacion
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
