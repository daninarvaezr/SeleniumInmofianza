import pyodbc
import configparser
import os
config = configparser.ConfigParser()
basedir = os.path.abspath(os.path.join(__file__, "../.."))
config.read(basedir + u'\\data\\config.ini')
database_name = config['QA-Omnicanalidad']['DB_NAME']
database_password = config['QA-Omnicanalidad']['DB_PASSWORD']
database_host = config['QA-Omnicanalidad']['DB_HOST']
database_user = config['QA-Omnicanalidad']['DB_USER']


try:
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+database_host+';DATABASE='+database_name+';UID='+database_user+';PWD='+database_password+'')
    print("Conexión exitosa")

except Exception as ex:
    print(ex)
cursor= connection.cursor()

cursor.execute("DECLARE @IDFIANZA nvarchar(100) = (select top 1 IdUserCaseBail FROM Omnicanalidad.dbo.UserCase order by CreatedAt desc); SELECT UC.IDUSERCASE ,U.USERDOCNUMBER AS CEDULA ,U.USERMOBILENUMBER AS CELULAR ,CASE UC.IDPROCESS WHEN 25 THEN 'FIRMANTE' WHEN 26 THEN 'REPRESENTANTE' ELSE 'DESCONOCIDO' END +' '+CASE WHEN UC.IDPARENT IS NULL THEN 'PRINCIPAL' ELSE 'SECUNDARIO' END AS TIPOFIRMANTE FROM OMNICANALIDAD.DBO.USERCASE UC LEFT JOIN OMNICANALIDAD.DBO.[USER] U ON U.IDUSER = UC.IDUSER LEFT JOIN OMNICANALIDAD.DBO.OBJECTSTATE OE ON UC.IDOBJECTSTATE= OE.IDOBJECTSTATE WHERE UC.IDUSERCASEBAIL = @IDFIANZA ORDER BY UC.IDUSERCASEBAIL,UC.IDUSERCASE,UC.CREATEDAT,UC.UPDATEDAT desc;")

x=cursor.fetchall()


while x :
    print(x)
    x=cursor.fetchall()



cursor.close()
connection.close()
