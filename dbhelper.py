import mysql.connector
import dbconfig

class DBHelper:
    def connect (self, database="crimemap"):
        return mysql.connector.connect(host="localhost",
         user=dbconfig.db_user, 
         passwd=dbconfig.db_password,
         db=database)

    def get_all_inputs(self):
        connection = self.connect()
        query = "SELECT description FROM crimes"
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
        connection.commit()
        connection.close()

    def add_input(self, data):
        connection = self.connect()
        query = "INSERT INTO crimes (description) VALUES ('{}')".format(data)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()   
        connection.close()

    def clear(self):
        connection = self.connect()
        query = "DELETE FROM crimes"
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()
    
