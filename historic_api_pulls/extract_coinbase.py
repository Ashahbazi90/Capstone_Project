import pandas as pd
import requests
import datetime
import time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta, timezone
from dateutil.relativedelta import relativedelta
from historic_api_pulls.utils.mysql_conn import db_conn
import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import pytz


def historical_three_years():
    ## Set timezone so the data is consistent
    pst = pytz.timezone('US/Pacific')
    # Get today's date
    today = datetime.now(pst)

    ## set variable parameters for start, end and granulairty
    product_ids = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'ADA-USD', 'LINK-USD', 'AVAX-USD', 'LTC-USD', 'UNI-USD', 'COMP-USD', 'MATIC-USD'] ## turn this to a list to get more than BTC
    # start date is 3 years ago
    start = today - relativedelta(months = 36)
    # end date is a 2.5 years ago
    end = today - relativedelta(months=30)
    granularity = 86400 

    # set new master df where all teh data will be stored
    all_data = pd.DataFrame()

    # loop over the product id list to extract 6 months worth of data for the above coins in one dataframe
        ## set URL to perform get request
    for product_id in product_ids:
        url = f'https://api.pro.coinbase.com/products/{product_id}/candles'
        params = {
            'start': start.isoformat(),
            'end': end.isoformat(),
            'granularity': granularity
        }

        # create an empty dataframe to store all the crypto data in at the end
        response = requests.get(url, params=params)
        time.sleep(15)
        try:
            if response.status_code == 200:
                data = response.json()
                # Convert the data to a pandas DataFrame for better readability
                df = pd.DataFrame(data, columns=['time', 'low', 'high', 'open', 'close', 'volume'])
                df['time'] = pd.to_datetime(df['time'], unit='s')
                df['price_change'] = df['close'] - df['open'] 
                df['average_price'] = (df['high'] + df['low']) / 2
                df['volatility'] = (df['high'] - df['low']) / df['low'] * 100
                df['product_id'] = product_id

                # Append to the main DataFrame
                all_data = pd.concat([all_data, df], ignore_index=True)

            else:
                print(f"Error: Received status code {response.status_code} for {product_id}")
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
        except ValueError as e:
            print(f"Value error: {e}")
        except KeyError as e:
            print(f"Key error: Missing key {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return all_data


def historical_two_half_years():
    ## Set timezone so the data is consistent
    pst = pytz.timezone('US/Pacific')
    # Get today's date
    today = datetime.now(pst)

    ## set variable parameters for start, end and granulairty
    product_ids = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'ADA-USD', 'LINK-USD', 'AVAX-USD', 'LTC-USD', 'UNI-USD', 'COMP-USD', 'MATIC-USD'] ## turn this to a list to get more than BTC
    # start date is 2.5 years plus 1 day to avoid overlap
    two_half = today - relativedelta(months=30)
    start =  two_half #+ timedelta(days=1)
    # end date is 2 years ago
    end = today - relativedelta(months=24)
    granularity = 86400 

    # set new master df where all teh data will be stored
    all_data = pd.DataFrame()

    # loop over the product id list to extract 6 months worth of data for teh above coins in one dataframe
    # for id in product_id:
        ## set URL to perform get request
    for product_id in product_ids:
        url = f'https://api.pro.coinbase.com/products/{product_id}/candles'
        params = {
            'start': start.isoformat(),
            'end': end.isoformat(),
            'granularity': granularity
        }

        # create an empty dataframe to store all the crypto data in at the end
        response = requests.get(url, params=params)
        time.sleep(15)
        try:
            if response.status_code == 200:
                data = response.json()
                # Convert the data to a pandas DataFrame for better readability
                df = pd.DataFrame(data, columns=['time', 'low', 'high', 'open', 'close', 'volume'])
                df['time'] = pd.to_datetime(df['time'], unit='s')
                df['price_change'] = df['close'] - df['open'] 
                df['average_price'] = (df['high'] + df['low']) / 2
                df['volatility'] = (df['high'] - df['low']) / df['low'] * 100
                df['product_id'] = product_id

                # Append to the main DataFrame
                all_data = pd.concat([all_data, df], ignore_index=True)

            else:
                print(f"Error: Received status code {response.status_code} for {product_id}")
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
        except ValueError as e:
            print(f"Value error: {e}")
        except KeyError as e:
            print(f"Key error: Missing key {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return all_data

def historical_two_years():
    ## Set timezone so the data is consistent
    pst = pytz.timezone('US/Pacific')
    # Get today's date
    today = datetime.now(pst)

    ## set variable parameters for start, end and granulairty
    product_ids = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'ADA-USD', 'LINK-USD', 'AVAX-USD', 'LTC-USD', 'UNI-USD', 'COMP-USD', 'MATIC-USD'] ## turn this to a list to get more than BTC
    # start date is 2 years 
    two_years = today - relativedelta(months=24)
    start =  two_years #+ timedelta(days=1)
    # end date is a a year an a half ago
    end = today - relativedelta(months=18)
    granularity = 86400 

    # set new master df where all teh data will be stored
    all_data = pd.DataFrame()

    # loop over the product id list to extract 6 months worth of data for teh above coins in one dataframe
    # for id in product_id:
        ## set URL to perform get request
    for product_id in product_ids:
        url = f'https://api.pro.coinbase.com/products/{product_id}/candles'
        params = {
            'start': start.isoformat(),
            'end': end.isoformat(),
            'granularity': granularity
        }

        # create an empty dataframe to store all the crypto data in at the end
        response = requests.get(url, params=params)
        time.sleep(15)
        try:
            if response.status_code == 200:
                data = response.json()
                # Convert the data to a pandas DataFrame for better readability
                df = pd.DataFrame(data, columns=['time', 'low', 'high', 'open', 'close', 'volume'])
                df['time'] = pd.to_datetime(df['time'], unit='s')
                df['price_change'] = df['close'] - df['open'] 
                df['average_price'] = (df['high'] + df['low']) / 2
                df['volatility'] = (df['high'] - df['low']) / df['low'] * 100
                df['product_id'] = product_id

                # Append to the main DataFrame
                all_data = pd.concat([all_data, df], ignore_index=True)

            else:
                print(f"Error: Received status code {response.status_code} for {product_id}")
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
        except ValueError as e:
            print(f"Value error: {e}")
        except KeyError as e:
            print(f"Key error: Missing key {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return all_data

def historical_one_half_years():
    ## Set timezone so the data is consistent
    pst = pytz.timezone('US/Pacific')
    # Get today's date
    today = datetime.now(pst)

    ## set variable parameters for start, end and granulairty
    product_ids = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'ADA-USD', 'LINK-USD', 'AVAX-USD', 'LTC-USD', 'UNI-USD', 'COMP-USD', 'MATIC-USD'] ## turn this to a list to get more than BTC
    # start date is 1.5 years 
    one_half = today - relativedelta(months=18)
    start =  one_half #+ timedelta(days=1)
    # end date is a a year ago
    end = today - relativedelta(months=12)
    granularity = 86400 

    # set new master df where all teh data will be stored
    all_data = pd.DataFrame()

    # loop over the product id list to extract 3months worth of data for teh above coins in one dataframe
        ## set URL to perform get request
    for product_id in product_ids:
        url = f'https://api.pro.coinbase.com/products/{product_id}/candles'
        params = {
            'start': start.isoformat(),
            'end': end.isoformat(),
            'granularity': granularity
        }

        # create an empty dataframe to store all the crypto data in at the end
        response = requests.get(url, params=params)
        time.sleep(15)
        try:
            if response.status_code == 200:
                data = response.json()
                # Convert the data to a pandas DataFrame for better readability
                df = pd.DataFrame(data, columns=['time', 'low', 'high', 'open', 'close', 'volume'])
                df['time'] = pd.to_datetime(df['time'], unit='s')
                df['price_change'] = df['close'] - df['open'] 
                df['average_price'] = (df['high'] + df['low']) / 2
                df['volatility'] = (df['high'] - df['low']) / df['low'] * 100
                df['product_id'] = product_id

                # Append to the main DataFrame
                all_data = pd.concat([all_data, df], ignore_index=True)

            else:
                print(f"Error: Received status code {response.status_code} for {product_id}")
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
        except ValueError as e:
            print(f"Value error: {e}")
        except KeyError as e:
            print(f"Key error: Missing key {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return all_data


def historical_one_years():
    ## Set timezone so the data is consistent
    pst = pytz.timezone('US/Pacific')
    # Get today's date
    today = datetime.now(pst)

    ## set variable parameters for start, end and granulairty
    product_ids = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'ADA-USD', 'LINK-USD', 'AVAX-USD', 'LTC-USD', 'UNI-USD', 'COMP-USD', 'MATIC-USD'] ## turn this to a list to get more than BTC
    # start date is 1 year ago
    one_year = today - relativedelta(months=12)
    start =  one_year #+ timedelta(days=1)
    # end date is 6 months
    end = today - relativedelta(months=6)
    granularity = 86400 

    # set new master df where all teh data will be stored
    all_data = pd.DataFrame()

    # loop over the product id list to extract 6 months worth of data for teh above coins in one dataframe
        ## set URL to perform get request
    for product_id in product_ids:
        url = f'https://api.pro.coinbase.com/products/{product_id}/candles'
        params = {
            'start': start.isoformat(),
            'end': end.isoformat(),
            'granularity': granularity
        }

        response = requests.get(url, params=params)
        time.sleep(15)
        try:
            if response.status_code == 200:
                data = response.json()
                # Convert the data to a pandas DataFrame for better readability
                df = pd.DataFrame(data, columns=['time', 'low', 'high', 'open', 'close', 'volume'])
                df['time'] = pd.to_datetime(df['time'], unit='s')
                df['price_change'] = df['close'] - df['open'] 
                df['average_price'] = (df['high'] + df['low']) / 2
                df['volatility'] = (df['high'] - df['low']) / df['low'] * 100
                df['product_id'] = product_id

                # Append to the main DataFrame
                all_data = pd.concat([all_data, df], ignore_index=True)

            else:
                print(f"Error: Received status code {response.status_code} for {product_id}")
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
        except ValueError as e:
            print(f"Value error: {e}")
        except KeyError as e:
            print(f"Key error: Missing key {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return all_data

def historical_six_months():
    ## Set timezone so the data is consistent
    pst = pytz.timezone('US/Pacific')
    # Get today's date
    today = datetime.now(pst)

    ## set variable parameters for start, end and granulairty
    product_ids = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'ADA-USD', 'LINK-USD', 'AVAX-USD', 'LTC-USD', 'UNI-USD', 'COMP-USD', 'MATIC-USD'] ## turn this to a list to get more than BTC
    # start date is 6 months plus 
    one_year = today - relativedelta(months=6)
    start =  one_year #+ timedelta(days=1)
    # end date is a week ago
    end = today - relativedelta(days = 7)
    granularity = 86400 

    # set new master df where all teh data will be stored
    all_data = pd.DataFrame()

    # loop over the product id list to extract 6 months worth of data for teh above coins in one dataframe
        ## set URL to perform get request
    for product_id in product_ids:
        url = f'https://api.pro.coinbase.com/products/{product_id}/candles'
        params = {
            'start': start.isoformat(),
            'end': end.isoformat(),
            'granularity': granularity
        }

        response = requests.get(url, params=params)
        time.sleep(15)
        try:
            if response.status_code == 200:
                data = response.json()
                # Convert the data to a pandas DataFrame for better readability
                df = pd.DataFrame(data, columns=['time', 'low', 'high', 'open', 'close', 'volume'])
                df['time'] = pd.to_datetime(df['time'], unit='s')
                df['price_change'] = df['close'] - df['open'] 
                df['average_price'] = (df['high'] + df['low']) / 2
                df['volatility'] = (df['high'] - df['low']) / df['low'] * 100
                df['product_id'] = product_id

                # Append to the main DataFrame
                all_data = pd.concat([all_data, df], ignore_index=True)

            else:
                print(f"Error: Received status code {response.status_code} for {product_id}")
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
        except ValueError as e:
            print(f"Value error: {e}")
        except KeyError as e:
            print(f"Key error: Missing key {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return all_data

def previous_week():
    ## Set timezone so the data is consistent
    pst = pytz.timezone('US/Pacific')
    # Get today's date
    today = datetime.now(pst)

    ## set variable parameters for start, end and granulairty
    product_ids = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'ADA-USD', 'LINK-USD', 'AVAX-USD', 'LTC-USD', 'UNI-USD', 'COMP-USD', 'MATIC-USD'] ## turn this to a list to get more than BTC
    # start date is a week ao
    one_week = today - relativedelta(days=7)
    start =  one_week #+ timedelta(days=1)
    # end date is a today
    end = today
    granularity = 86400 

    # set new master df where all teh data will be stored
    all_data = pd.DataFrame()

    # loop over the product id list to extract 3months worth of data for teh above coins in one dataframe
        ## set URL to perform get request
    for product_id in product_ids:
        url = f'https://api.pro.coinbase.com/products/{product_id}/candles'
        params = {
            'start': start.isoformat(),
            'end': end.isoformat(),
            'granularity': granularity
        }

        response = requests.get(url, params=params)
        time.sleep(15)
        try:
            if response.status_code == 200:
                data = response.json()
                # Convert the data to a pandas DataFrame for better readability
                df = pd.DataFrame(data, columns=['time', 'low', 'high', 'open', 'close', 'volume'])
                df['time'] = pd.to_datetime(df['time'], unit='s')
                df['price_change'] = df['close'] - df['open'] 
                df['average_price'] = (df['high'] + df['low']) / 2
                df['volatility'] = (df['high'] - df['low']) / df['low'] * 100
                df['product_id'] = product_id

                # Append to the main DataFrame
                all_data = pd.concat([all_data, df], ignore_index=True)

            else:
                print(f"Error: Received status code {response.status_code} for {product_id}")
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
        except ValueError as e:
            print(f"Value error: {e}")
        except KeyError as e:
            print(f"Key error: Missing key {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return all_data



def fetch_missing_data(product_id, start, end, granularity=86400):
    url = f'https://api.pro.coinbase.com/products/{product_id}/candles'
    params = {
        'start': start.isoformat(),
        'end': end.isoformat(),
        'granularity': granularity
    }
    
    response = requests.get(url, params=params)
    time.sleep(1)  # Be cautious with API rate limits
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data, columns=['time', 'low', 'high', 'open', 'close', 'volume'])
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df['price_change'] = df['close'] - df['open']
        df['average_price'] = (df['high'] + df['low']) / 2
        df['volatility'] = (df['high'] - df['low']) / df['low'] * 100
        df['product_id'] = product_id
        return df
    else:
        print(f"Error: Received status code {response.status_code} for {product_id}")
        return pd.DataFrame()

def check_missing_dates(df, start_date, end_date):
    full_range = pd.date_range(start=start_date, end=end_date, freq='D')
    missing_dates = full_range.difference(df['time'])
    return missing_dates

def fetch_missing_dates(product_id, dates):
    all_data = pd.DataFrame()
    for date in dates:
        start = pd.to_datetime(date)
        end = start + timedelta(days=1)
        df = fetch_missing_data(product_id, start, end)
        all_data = pd.concat([all_data, df], ignore_index=True)
    return all_data



def combine_price_data():
    ### coombine all the funcitons in one to combine the data into one dataframe to work form 
    pst = pytz.timezone('US/Pacific')
    load_dt = datetime.now(pst).date().strftime('%Y-%m-%d')
    three_years = historical_three_years()
    two_half = historical_two_half_years()
    two_years = historical_two_years()
    one_half = historical_one_half_years()
    one_year = historical_one_years()
    six_months = historical_six_months()
    combined_df = pd.concat([three_years, two_half, 
                             two_years, one_half, 
                             one_year, six_months], ignore_index=True)
    combined_df = pd.concat([three_years, two_half, two_years, one_half, one_year, six_months], ignore_index=True)
    combined_df['load_dt'] = load_dt
    combined_df = combined_df.sort_values(by='time').reset_index(drop=True)
    
    # Check for missing dates
    start_date = (datetime.now(pst) - relativedelta(months=36)).date()
    end_date = (datetime.now(pst) - relativedelta(days=7)).date()
    missing_dates = check_missing_dates(combined_df, start_date, end_date)
    if not missing_dates.empty:
        print(f"Missing dates: {missing_dates}")
        for product_id in ['BTC-USD', 'ETH-USD', 'SOL-USD', 'ADA-USD', 'LINK-USD', 'AVAX-USD', 'LTC-USD', 'UNI-USD', 'COMP-USD', 'MATIC-USD']:
            missing_data = fetch_missing_dates(product_id, missing_dates)
            combined_df = pd.concat([combined_df, missing_data], ignore_index=True)
    
    return combined_df

def load_mysql_historic_table():

    ## This function is used to create a database and a table for the training data to be loaded into 
    db = db_conn()
    try:
        crypto_data = combine_price_data()
        database_name = 'CAPSTONE'
        table_name = 'HISTORIC_CRYPTO_PRICES'
        print(f'username:{db.user}, host: {db.host}')

        # Create SQLAlchemy engine using credentials from db_conn
        engine = create_engine(f'mysql+mysqlconnector://{db.user}:{db.password}@{db.host}/{database_name}')
        # Insert data into MySQL table using SQLAlchemy
        crypto_data.to_sql(name=table_name, con=engine, if_exists='append', index=False)

        print("Data inserted successfully into HISTORIC_CRYPTO_PRICES")
    except SQLAlchemyError as err:
        print(f"SQLAlchemy Error: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
            
# load_mysql_historic_table()
print("Imports are working fine")

############### JUSTIN TO-DO ############################################

## 1. Create seperate historic funtions that pull data 6 months at a time -- done
## 2. Create one main function that concats the data together into one df or file -- done 
## 3. create a 2 new scripts, 1 for connecting to MySQL so I can dump the historic combined df into my table - done
## 4. Create new script that pulls data based on the last date in the training table and todays date minus 7 days
