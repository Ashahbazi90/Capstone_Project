import pandas as pd
import requests
import datetime
import time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta, timezone
from dateutil.relativedelta import relativedelta
import pytz


def fetch_historical_data():
    ## set variables for dates, we are starting with 3 months worth of days and going up to
    ## a week from the current date as the current week will be out test set

    ## Set timezone so the data is consistent
    pst = pytz.timezone('US/Pacific')
    # Get today's date
    today = datetime.now(pst)

    ## set variable parameters for start, end and granulairty
    product_id = 'BTC-USD' ## turn this to a list to get more than BTC
    # start date is 3 months ago
    start = today - relativedelta(months=3)
    # end date is a week ago
    end = today - relativedelta(days=7)
    granularity = 86400 

    ## set URL to perform get request
    url = f'https://api.pro.coinbase.com/products/{product_id}/candles'
    params = {
        'start': start,
        'end': end,
        'granularity': granularity
    }
    response = requests.get(url, params=params)
    time.sleep(30)
    data = response.json()
   # print(data)
    
    # Convert the data to a pandas DataFrame for better readability
    df = pd.DataFrame(data, columns=['time', 'low', 'high', 'open', 'close', 'volume'])
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df['price_change'] = df['close'] - df['open'] 
    df['average_price'] = (df['high'] + df['low']) / 2
    df['volatitlity'] = (df['high'] - df['low']) / df['low'] * 100
     
    return df

# # Define the parameters
# product_id = 'BTC-USD'
# start = '2022-01-01T00:00:00Z'
# end = '2022-01-30T00:00:00Z'
# granularity = 86400  # 1 day in seconds

# # Fetch the historical data
df = fetch_historical_data()
create_raw_file = df.to_csv('RAW_Data/BTC_historical.csv')
print(df)

# # Display the data
# #print(df)

# # set timezone to PST 
# pst = pytz.timezone('US/Pacific')
# # Get today's date
# today = datetime.now(pst)
# seven_days_ago = today - relativedelta(days=7)

# # Calculate the date 3 months ago
# three_months_ago = today - relativedelta(months=3)

# # Get the ISO format of that date
# iso_format_date = three_months_ago.strftime('%Y-%m-%dT%H:%M:%SZ')
# iso_format_date_7 = seven_days_ago.strftime('%Y-%m-%dT%H:%M:%SZ')


# print(f"start = '{iso_format_date_7}'")
# print(today.strftime('%Y-%m-%dT%H:%M:%SZ'))
