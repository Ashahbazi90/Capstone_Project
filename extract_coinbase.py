import pandas as pd
import requests
import datetime
import time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta, timezone
from dateutil.relativedelta import relativedelta
import pytz


def historical_three_years():
    ## Set timezone so the data is consistent
    pst = pytz.timezone('US/Pacific')
    # Get today's date
    today = datetime.now(pst)

    ## set variable parameters for start, end and granulairty
    product_ids = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'ADA-USD', 'LINK-USD', 'XRP-USD', 'LTC-USD'] ## turn this to a list to get more than BTC
    # start date is 3 years ago
    start = today - relativedelta(months = 36)
    # end date is a week ago
    end = today - relativedelta(months=30)
    granularity = 86400 

    # set new master df where all teh data will be stored
    all_data = pd.DataFrame()

    # loop over the product id list to extract 3months worth of data for teh above coins in one dataframe
    # for id in product_id:
        ## set URL to perform get request
    for product_id in product_ids:
        url = f'https://api.pro.coinbase.com/products/{product_id}/candles'
        params = {
            'start': start.isoformat(),
            'end': end.isoformat(),
            'granularity': granularity
        }

        # Print URL and parameters for debugging
        # print(f"Fetching data for {product_id}")
        # print(f"URL: {url}")
        # print(f"Parameters: {params}")
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
                df['volatitlity'] = (df['high'] - df['low']) / df['low'] * 100
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
    product_ids = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'ADA-USD', 'LINK-USD', 'XRP-USD', 'LTC-USD'] ## turn this to a list to get more than BTC
    # start date is 2.5 years plus 1 day to avoid overlap
    two_half = today - relativedelta(months=30)
    start =  two_half + timedelta(days=1)
    # end date is a week ago
    end = today - relativedelta(months=24)
    granularity = 86400 

    # set new master df where all teh data will be stored
    all_data = pd.DataFrame()

    # loop over the product id list to extract 3months worth of data for teh above coins in one dataframe
    # for id in product_id:
        ## set URL to perform get request
    for product_id in product_ids:
        url = f'https://api.pro.coinbase.com/products/{product_id}/candles'
        params = {
            'start': start.isoformat(),
            'end': end.isoformat(),
            'granularity': granularity
        }

        # Print URL and parameters for debugging
        # print(f"Fetching data for {product_id}")
        # print(f"URL: {url}")
        # print(f"Parameters: {params}")
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
                df['volatitlity'] = (df['high'] - df['low']) / df['low'] * 100
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
    product_ids = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'ADA-USD', 'LINK-USD', 'XRP-USD', 'LTC-USD'] ## turn this to a list to get more than BTC
    # start date is 2.5 years plus 1 day to avoid overlap
    two_years = today - relativedelta(months=24)
    start =  two_years + timedelta(days=1)
    # end date is a week ago
    end = today - relativedelta(months=18)
    granularity = 86400 

    # set new master df where all teh data will be stored
    all_data = pd.DataFrame()

    # loop over the product id list to extract 3months worth of data for teh above coins in one dataframe
    # for id in product_id:
        ## set URL to perform get request
    for product_id in product_ids:
        url = f'https://api.pro.coinbase.com/products/{product_id}/candles'
        params = {
            'start': start.isoformat(),
            'end': end.isoformat(),
            'granularity': granularity
        }

        # Print URL and parameters for debugging
        # print(f"Fetching data for {product_id}")
        # print(f"URL: {url}")
        # print(f"Parameters: {params}")
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
                df['volatitlity'] = (df['high'] - df['low']) / df['low'] * 100
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
    product_ids = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'ADA-USD', 'LINK-USD', 'XRP-USD', 'LTC-USD'] ## turn this to a list to get more than BTC
    # start date is 2.5 years plus 1 day to avoid overlap
    one_half = today - relativedelta(months=18)
    start =  one_half + timedelta(days=1)
    # end date is a week ago
    end = today - relativedelta(months=12)
    granularity = 86400 

    # set new master df where all teh data will be stored
    all_data = pd.DataFrame()

    # loop over the product id list to extract 3months worth of data for teh above coins in one dataframe
    # for id in product_id:
        ## set URL to perform get request
    for product_id in product_ids:
        url = f'https://api.pro.coinbase.com/products/{product_id}/candles'
        params = {
            'start': start.isoformat(),
            'end': end.isoformat(),
            'granularity': granularity
        }

        # Print URL and parameters for debugging
        # print(f"Fetching data for {product_id}")
        # print(f"URL: {url}")
        # print(f"Parameters: {params}")
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
                df['volatitlity'] = (df['high'] - df['low']) / df['low'] * 100
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
    product_ids = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'ADA-USD', 'LINK-USD', 'XRP-USD', 'LTC-USD'] ## turn this to a list to get more than BTC
    # start date is 2.5 years plus 1 day to avoid overlap
    one_year = today - relativedelta(months=12)
    start =  one_year + timedelta(days=1)
    # end date is a week ago
    end = today - relativedelta(months=6)
    granularity = 86400 

    # set new master df where all teh data will be stored
    all_data = pd.DataFrame()

    # loop over the product id list to extract 3months worth of data for teh above coins in one dataframe
    # for id in product_id:
        ## set URL to perform get request
    for product_id in product_ids:
        url = f'https://api.pro.coinbase.com/products/{product_id}/candles'
        params = {
            'start': start.isoformat(),
            'end': end.isoformat(),
            'granularity': granularity
        }

        # Print URL and parameters for debugging
        # print(f"Fetching data for {product_id}")
        # print(f"URL: {url}")
        # print(f"Parameters: {params}")
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
                df['volatitlity'] = (df['high'] - df['low']) / df['low'] * 100
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
    product_ids = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'ADA-USD', 'LINK-USD', 'XRP-USD', 'LTC-USD'] ## turn this to a list to get more than BTC
    # start date is 2.5 years plus 1 day to avoid overlap
    one_year = today - relativedelta(months=6)
    start =  one_year + timedelta(days=1)
    # end date is a week ago
    end = today - relativedelta(days = 7)
    granularity = 86400 

    # set new master df where all teh data will be stored
    all_data = pd.DataFrame()

    # loop over the product id list to extract 3months worth of data for teh above coins in one dataframe
    # for id in product_id:
        ## set URL to perform get request
    for product_id in product_ids:
        url = f'https://api.pro.coinbase.com/products/{product_id}/candles'
        params = {
            'start': start.isoformat(),
            'end': end.isoformat(),
            'granularity': granularity
        }

        # Print URL and parameters for debugging
        # print(f"Fetching data for {product_id}")
        # print(f"URL: {url}")
        # print(f"Parameters: {params}")
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
                df['volatitlity'] = (df['high'] - df['low']) / df['low'] * 100
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


def main():
    three_years = historical_three_years()
    two_half = historical_two_half_years()
    two_years = historical_two_years()
    one_half = historical_one_half_years()
    one_year = historical_one_years()
    six_months = historical_six_months()
    combined_df = pd.concat([three_years, two_half, 
                             two_years, one_half, 
                             one_year, six_months], ignore_index=True)
    return combined_df

main_df = main()
main_to_csv = main_df.to_csv("RAW_Data/main_data.csv")
grouped_df = main_df.groupby('product_id')['time'].nunique().reset_index()
grouped_df.columns = ['product_id', 'unique_date_count']
num_rows = len(main_df)

if num_rows > grouped_df['unique_date_count'].sum():
    print('Duplicate Dates Found')
else:
    print('No duplicates Found')


# # Define the parameters
# product_id = 'BTC-USD'
# start = '2022-01-01T00:00:00Z'
# end = '2022-01-30T00:00:00Z'
# granularity = 86400  # 1 day in seconds

# # Fetch the historical data
# df = fetch_historical_data()
#create_raw_file = df.to_csv('RAW_Data/BTC_historical.csv')
# create_raw_file = df.to_csv('RAW_Data/all_historical_first_six_mths.csv')

# pst = pytz.timezone('US/Pacific')
# # Get today's date
# today = datetime.now(pst)

# ## set variable parameters for start, end and granulairty
# #product_ids = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'ADA-USD', 'LINK-USD', 'XRP-USD', 'LTC-USD'] ## turn this to a list to get more than BTC
# # start date is 3 months ago
# three_yrs = today - relativedelta(months = 36)
# # end date is a week ago
# two_half = today - relativedelta(months=30)
# two_half_plus_one_day = two_half + timedelta(days=1)

# two_years = today - relativedelta(months=24)

# one_half = today - relativedelta(months=18)

# one_year = today - relativedelta(months=12)

# six_months = today - relativedelta(months=6)

# three_months = today - relativedelta(months=3)

# week_ago = today - relativedelta(days = 7)

# print('3 years ago')
# print(three_yrs)
# print("---------------------------------------------")
# print('2.5 years ago')
# print(two_half)
# print("---------------------------------------------")
# print('2.5 plus 1 day years ago')
# print(two_half_plus_one_day)
# print("---------------------------------------------")
# print('2 years ago')
# print(two_years)
# print("---------------------------------------------")
# print('1.5 years ago')
# print(one_half)
# print("---------------------------------------------")
# print('1 years ago')
# print(one_year)
# print("---------------------------------------------")
# print('6 months ago')
# print(six_months)
# print("---------------------------------------------")
# print('3 months ago')
# print(three_months)
# print("---------------------------------------------")
# print('week ago')
# print(week_ago)
# print("---------------------------------------------")


############### JUSTIN TO-DO ############################################

## 1. Create seperate historic funtions that pull data 6 months at a time
## 2. Create one main function that concats the data together into one df or file
## 3. create a 2 new scripts, 1 for connecting to MySQL so I can dump the historic combined df into my table
## 4. Create new script that pulls data based on the last date in the training table and todays date minus 7 days
