import pymysql
import dbconfig

connection = pymysql.connect(host='loacalhost',
user=dbconfig.db_user,
passwd=dbconfig.db_password)

try:
    with connection.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXITSTS crimemap"
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS crimemap.crimes (id int NOT NULL AUTO_INCREMENT,
        latitude FLOAT (10, 6),
        longitude FLOAT(10,6),
        date DATETIME,
        category VARCHAR (1000),
        update_at TIMESTAMP,
        PRIMARY KEY (id)
        )"""
        cursor.execute(sql)
        connection.commit()
finally:
    connection.close()
    
