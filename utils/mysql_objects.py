from mysql_conn import db_conn
import pandas as pd

#rom capstone_project.extract_coinbase import main_df
import mysql.connector

def create_historical_price_table():
    try:
        db = db_conn()
        connection = db.mysql_conn()
        db.execute_query(connection, "CREATE DATABASE CAPSTONE")
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

# def insert_into_historic_prices():
#     try:
#         db = db_conn()
#         connection = db.mysql_conn()
#         db.execute_query(connection, "USE CAPSTONE")
#         query = """

create_historical_price_table()

        