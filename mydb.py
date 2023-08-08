import mysql.connector
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'hnf3838'
)
cursorObject = database.cursor()
cursorObject.execute("CREATE DATABASE hisham")
print("All done")