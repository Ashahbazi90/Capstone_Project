import os
import mysql.connector
from dotenv import load_dotenv
import os
_ = load_dotenv()



class db_conn:

    def __init__(self):
        self.host = os.getenv('HOST_NAME')
        self.user = os.getenv('USERNAME')
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


def create_capstone_db():
    try:
        db = db_conn()
        connection = db.mysql_conn()
        db.execute_query(connection, "CREATE DATABASE IF NOT EXISTS CAPSTONE")
        print(f'Sucessful Creation on Database')
    except mysql.connector.Error as e:
        print(f'An Error has occured {e}')

def create_historical_price_table():
    try:
        db = db_conn()
        connection = db.mysql_conn()
        db.execute_query(connection, "USE CAPSTONE")
        query = """
                CREATE TABLE IF NOT EXISTS HISTORIC_CRYPTO_PRICES (
                    time DATE,
                    low FLOAT,
                    high FLOAT,
                    open FLOAT,
                    close FLOAT,
                    volume FLOAT,
                    price_change FLOAT,
                    average_price FLOAT,
                    volatility FLOAT,
                    product_id VARCHAR(255),
                    load_dt TIMESTAMP 
                    )"""
        db.execute_query(connection, query)
        print(f'Sucessful Creation on Table')
    except mysql.connector.Error as e:
        print(f'An Error has occured {e}')

if __name__ == "__main__":
    create_capstone_db()
    create_historical_price_table()
