import mysql.connector
import dbconfig

connection = mysql.connector.connect(
    host = "localhost",
    port = "3306",
    user = dbconfig.db_user,
    passwd = dbconfig.db_password  
)

mycursor = connection.cursor()
'''
sql = "CREATE DATABASE crimemap"
mycursor.execute(sql)'''

       
sql = """CREATE TABLE crimemap.crimes (
            id int NOT NULL AUTO_INCREMENT,
            latitude FLOAT (10, 6),
            longitude FLOAT(10,6),
            date DATETIME,
            category VARCHAR (1000),
            update_at TIMESTAMP,
            PRIMARY KEY (id)
            )"""
mycursor.execute(sql)
connection.close()

