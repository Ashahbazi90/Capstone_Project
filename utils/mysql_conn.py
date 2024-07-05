import os
import mysql.connector
from dotenv import load_dotenv
import os
_ = load_dotenv()



class db_conn:

    def __init__(self):
        self.host = os.getenv('HOST')
        self.user = os.getenv('USER')
        self.password = os.getenv('PASSWORD')

    def mysql_conn(self):
        try:
            db_conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            if db_conn.is_connected():
                    print("Connected to MySQL database")
                    return db_conn
        except mysql.db_conn.Error as err:
            print(f"Error: {err}")
            return None
        
    def execute_query(self, connection, query, data=None):
         try:
            cursor = connection.cursor()
            if data:
                cursor.executemany(query, data)
            else:
              cursor.execute(query)
            cursor.close()
         except mysql.connector.Error as e:
              print(f"Error {e}")

    def close(self, connection):
        connection.close()

