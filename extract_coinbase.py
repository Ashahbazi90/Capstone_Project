import pandas as pd
import requests
import datetime

def fetch_historical_data(product_id, start, end, granularity):
    url = f'https://api.pro.coinbase.com/products/{product_id}/candles'
    params = {
        'start': start,
        'end': end,
        'granularity': granularity
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(data)
    
    # Convert the data to a pandas DataFrame for better readability
    df = pd.DataFrame(data, columns=['time', 'low', 'high', 'open', 'close', 'volume'])
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df['price_change'] = df['close'] - df['open'] 
    df['average_price'] = (df['high'] + df['low']) / 2
    df['volatitlity'] = (df['high'] - df['low']) / df['low'] * 100
     
    return df

# Define the parameters
product_id = 'BTC-USD'
start = '2022-01-01T00:00:00Z'
end = '2023-01-10T00:00:00Z'
granularity = 86400  # 1 day in seconds

# Fetch the historical data
df = fetch_historical_data(product_id, start, end, granularity)

# Display the data
print(df)