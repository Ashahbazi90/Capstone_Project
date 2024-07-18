import pandas as pd
import os
from dotenv import load_dotenv
import json
import re
import requests
from datetime import datetime


class RedditAPI:
    def __init__(self):
        self.client_id = os.getenv("CLIENT_ID")
        self.secret_token = os.getenv("SECRET_TOKEN")
        self.reddit_password = os.getenv("PASSWORD_REDDIT")
        self.headers = {'User-Agent': 'ADSAPI/0.0.1'}
        self.access_token = self._get_access_token()

    def _get_access_token(self):
        auth = requests.auth.HTTPBasicAuth(self.client_id, self.secret_token)
        data = {
            "grant_type": "password",
            'username': "justinm329",
            'password': self.reddit_password
        }
        res = requests.post('https://www.reddit.com/api/v1/access_token',
                            auth=auth, data=data, headers=self.headers)
        access_token = res.json()['access_token']
        self.headers['Authorization'] = f'Bearer {access_token}'
        return access_token
    
    def _get_reddit_data(self, endpoint):
        res = requests.get(endpoint, headers=self.headers, params={'limit': '100'})
        return res
    
    def get_crypto_curr_data(self):
        crypto_request = self._get_reddit_data('https://oauth.reddit.com/r/CryptoCurrency/hot')
        crypto_json = crypto_request.json()
        crypto_df = pd.DataFrame()
        subreddit_name = 'CryptoCurrency'
        for post in crypto_json['data']['children']:
            new_df = pd.DataFrame({
                'approved_date': [post['data']['approved_at_utc']],
                'thread_id': [post['kind'] + " _ " + post['data']['id']],
                'subreddit': [post['data']['subreddit']],
                'title': [post['data']['title']],
                "body": [post['data']['selftext']],
                'upvote_ratio': [post['data']['upvote_ratio']],
                'ups': [post['data']['ups']],
                'downs': [post['data']['downs']],
                'score':  [post['data']['score']],
                'subreddit_name': [subreddit_name],
                'created_date': [datetime.utcfromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%d %H:%M:%S')]
            })
            crypto_df = pd.concat([crypto_df, new_df], ignore_index=True)
        return crypto_df
    

    def get_crypto_markets_data(self):
        crypto_df = pd.DataFrame()
        crypto_markets_request = self._get_reddit_data('https://oauth.reddit.com/r/CryptoMarkets/hot')
        markets_json = crypto_markets_request.json()
        subreddit_name = 'CryptoMarkets'
        for post in markets_json['data']['children']:
            new_df = pd.DataFrame({
                'approved_date': [post['data']['approved_at_utc']],
                'thread_id': [post['kind'] + " _ " + post['data']['id']],
                'subreddit': [post['data']['subreddit']],
                'title': [post['data']['title']],
                "body": [post['data']['selftext']],
                'upvote_ratio': [post['data']['upvote_ratio']],
                'ups': [post['data']['ups']],
                'downs': [post['data']['downs']],
                'score':  [post['data']['score']],
                'subreddit_name': [subreddit_name],
                'created_date': [datetime.utcfromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%d %H:%M:%S')]
            })
            crypto_df = pd.concat([crypto_df, new_df], ignore_index=True)
        return crypto_df
    
    def get_bitcoin_data(self):
        crypto_df = pd.DataFrame()
        bitcoin_request = self._get_reddit_data('https://oauth.reddit.com/r/Bitcoin/hot')
        bitcoin_json = bitcoin_request.json()
        subreddit_name = 'Bitcoin'
        for post in bitcoin_json['data']['children']:
            new_df = pd.DataFrame({
                'approved_date': [post['data']['approved_at_utc']],
                'thread_id': [post['kind'] + " _ " + post['data']['id']],
                'subreddit': [post['data']['subreddit']],
                'title': [post['data']['title']],
                "body": [post['data']['selftext']],
                'upvote_ratio': [post['data']['upvote_ratio']],
                'ups': [post['data']['ups']],
                'downs': [post['data']['downs']],
                'score':  [post['data']['score']],
                'subreddit_name': [subreddit_name],
                'created_date': [datetime.utcfromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%d %H:%M:%S')]
            })
            crypto_df = pd.concat([crypto_df, new_df], ignore_index=True)
        return crypto_df
    
    def get_eth_data(self):
        crypto_df = pd.DataFrame()
        eths_request = self._get_reddit_data('https://oauth.reddit.com/r/Ethereum/hot')
        eth_json = eths_request.json()
        subreddit_name = 'Ethereum'
        for post in eth_json['data']['children']:
            new_df = pd.DataFrame({
                'approved_date': [post['data']['approved_at_utc']],
                'thread_id': [post['kind'] + " _ " + post['data']['id']],
                'subreddit': [post['data']['subreddit']],
                'title': [post['data']['title']],
                "body": [post['data']['selftext']],
                'upvote_ratio': [post['data']['upvote_ratio']],
                'ups': [post['data']['ups']],
                'downs': [post['data']['downs']],
                'score':  [post['data']['score']],
                'subreddit_name': [subreddit_name],
                'created_date': [datetime.utcfromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%d %H:%M:%S')]
            })
            crypto_df = pd.concat([crypto_df, new_df], ignore_index=True)
        return crypto_df
    
    def get_binance_data(self):
        crypto_df = pd.DataFrame()
        binance_request = self._get_reddit_data('https://oauth.reddit.com/r/binance/hot')
        binance_json = binance_request.json()
        subreddit_name = 'binance'
        for post in binance_json['data']['children']:
            new_df = pd.DataFrame({
                'approved_date': [post['data']['approved_at_utc']],
                'thread_id': [post['kind'] + " _ " + post['data']['id']],
                'subreddit': [post['data']['subreddit']],
                'title': [post['data']['title']],
                "body": [post['data']['selftext']],
                'upvote_ratio': [post['data']['upvote_ratio']],
                'ups': [post['data']['ups']],
                'downs': [post['data']['downs']],
                'score':  [post['data']['score']],
                'subreddit_name': [subreddit_name],
                'created_date': [datetime.utcfromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%d %H:%M:%S')]
            })
            crypto_df = pd.concat([crypto_df, new_df], ignore_index=True)
        return crypto_df
    
    def get_solana_data(self):
        crypto_df = pd.DataFrame()
        solana_request = self._get_reddit_data('https://oauth.reddit.com/r/Solana/hot')
        solana_json = solana_request.json()
        subreddit_name = 'Solana'
        for post in solana_json['data']['children']:
            new_df = pd.DataFrame({
                'approved_date': [post['data']['approved_at_utc']],
                'thread_id': [post['kind'] + " _ " + post['data']['id']],
                'subreddit': [post['data']['subreddit']],
                'title': [post['data']['title']],
                "body": [post['data']['selftext']],
                'upvote_ratio': [post['data']['upvote_ratio']],
                'ups': [post['data']['ups']],
                'downs': [post['data']['downs']],
                'score':  [post['data']['score']],
                'subreddit_name': [subreddit_name],
                'created_date': [datetime.utcfromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%d %H:%M:%S')]
            })
            crypto_df = pd.concat([crypto_df, new_df], ignore_index=True)
        return crypto_df
    
    def get_uniswap_data(self):
        crypto_df = pd.DataFrame()
        uniswap_request = self._get_reddit_data('https://oauth.reddit.com/r/UniSwap/hot')
        uniswap_json = uniswap_request.json()
        subreddit_name = 'UniSwap'
        for post in uniswap_json['data']['children']:
            new_df = pd.DataFrame({
                'approved_date': [post['data']['approved_at_utc']],
                'thread_id': [post['kind'] + " _ " + post['data']['id']],
                'subreddit': [post['data']['subreddit']],
                'title': [post['data']['title']],
                "body": [post['data']['selftext']],
                'upvote_ratio': [post['data']['upvote_ratio']],
                'ups': [post['data']['ups']],
                'downs': [post['data']['downs']],
                'score':  [post['data']['score']],
                'subreddit_name': [subreddit_name],
                'created_date': [datetime.utcfromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%d %H:%M:%S')]
            })
            crypto_df = pd.concat([crypto_df, new_df], ignore_index=True)
        return crypto_df
    
    def get_cardano_data(self):
        crypto_df = pd.DataFrame()
        cardano_request = self._get_reddit_data('https://oauth.reddit.com/r/cardano/hot')
        cardano_json = cardano_request.json()
        subreddit_name = 'cardano'
        for post in cardano_json['data']['children']:
            new_df = pd.DataFrame({
                'approved_date': [post['data']['approved_at_utc']],
                'thread_id': [post['kind'] + " _ " + post['data']['id']],
                'subreddit': [post['data']['subreddit']],
                'title': [post['data']['title']],
                "body": [post['data']['selftext']],
                'upvote_ratio': [post['data']['upvote_ratio']],
                'ups': [post['data']['ups']],
                'downs': [post['data']['downs']],
                'score':  [post['data']['score']],
                'subreddit_name': [subreddit_name],
                'created_date': [datetime.utcfromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%d %H:%M:%S')]
            })
            crypto_df = pd.concat([crypto_df, new_df], ignore_index=True)
        return crypto_df
    
    def get_avax_data(self):
        crypto_df = pd.DataFrame()
        avax_request = self._get_reddit_data('https://oauth.reddit.com/r/Avax/hot')
        avax_json = avax_request.json()
        subreddit_name = 'Avax'
        for post in avax_json['data']['children']:
            new_df = pd.DataFrame({
                'approved_date': [post['data']['approved_at_utc']],
                'thread_id': [post['kind'] + " _ " + post['data']['id']],
                'subreddit': [post['data']['subreddit']],
                'title': [post['data']['title']],
                "body": [post['data']['selftext']],
                'upvote_ratio': [post['data']['upvote_ratio']],
                'ups': [post['data']['ups']],
                'downs': [post['data']['downs']],
                'score':  [post['data']['score']],
                'subreddit_name': [subreddit_name],
                'created_date': [datetime.utcfromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%d %H:%M:%S')]
            })
            crypto_df = pd.concat([crypto_df, new_df], ignore_index=True)
        return crypto_df
    
    def get_chainlink_data(self):
        crypto_df = pd.DataFrame()
        chainlink_request = self._get_reddit_data('https://oauth.reddit.com/r/Chainlink/hot')
        chainlink_json = chainlink_request.json()
        subreddit_name = 'Chainlink'
        for post in chainlink_json['data']['children']:
            new_df = pd.DataFrame({
                'approved_date': [post['data']['approved_at_utc']],
                'thread_id': [post['kind'] + " _ " + post['data']['id']],
                'subreddit': [post['data']['subreddit']],
                'title': [post['data']['title']],
                "body": [post['data']['selftext']],
                'upvote_ratio': [post['data']['upvote_ratio']],
                'ups': [post['data']['ups']],
                'downs': [post['data']['downs']],
                'score':  [post['data']['score']],
                'subreddit_name': [subreddit_name],
                'created_date': [datetime.utcfromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%d %H:%M:%S')]
            })
            crypto_df = pd.concat([crypto_df, new_df], ignore_index=True)
        return crypto_df
    
    def get_litecoin_data(self):
        crypto_df = pd.DataFrame()
        litecoin_request = self._get_reddit_data('https://oauth.reddit.com/r/litecoin/hot')
        litecoin_json = litecoin_request.json()
        subreddit_name = 'litecoin'
        for post in litecoin_json['data']['children']:
            new_df = pd.DataFrame({
                'approved_date': [post['data']['approved_at_utc']],
                'thread_id': [post['kind'] + " _ " + post['data']['id']],
                'subreddit': [post['data']['subreddit']],
                'title': [post['data']['title']],
                "body": [post['data']['selftext']],
                'upvote_ratio': [post['data']['upvote_ratio']],
                'ups': [post['data']['ups']],
                'downs': [post['data']['downs']],
                'score':  [post['data']['score']],
                'subreddit_name': [subreddit_name],
                'created_date': [datetime.utcfromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%d %H:%M:%S')]
            })
            crypto_df = pd.concat([crypto_df, new_df], ignore_index=True)
        return crypto_df
    
    def get_compound_data(self):
        crypto_df = pd.DataFrame()
        compound_request = self._get_reddit_data('https://oauth.reddit.com/r/Compound/hot')
        compound_json = compound_request.json()
        subreddit_name = 'Compound'
        for post in compound_json['data']['children']:
            new_df = pd.DataFrame({
                'approved_date': [post['data']['approved_at_utc']],
                'thread_id': [post['kind'] + " _ " + post['data']['id']],
                'subreddit': [post['data']['subreddit']],
                'title': [post['data']['title']],
                "body": [post['data']['selftext']],
                'upvote_ratio': [post['data']['upvote_ratio']],
                'ups': [post['data']['ups']],
                'downs': [post['data']['downs']],
                'score':  [post['data']['score']],
                'subreddit_name': [subreddit_name],
                'created_date': [datetime.utcfromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%d %H:%M:%S')]
            })
            crypto_df = pd.concat([crypto_df, new_df], ignore_index=True)
        return crypto_df
    
    def get_polygon_data(self):
        crypto_df = pd.DataFrame()
        polygon_request = self._get_reddit_data('https://oauth.reddit.com/r/0xPolygon/hot')
        polygon_json = polygon_request.json()
        subreddit_name = 'Polygon'
        for post in polygon_json['data']['children']:
            new_df = pd.DataFrame({
                'approved_date': [post['data']['approved_at_utc']],
                'thread_id': [post['kind'] + " _ " + post['data']['id']],
                'subreddit': [post['data']['subreddit']],
                'title': [post['data']['title']],
                "body": [post['data']['selftext']],
                'upvote_ratio': [post['data']['upvote_ratio']],
                'ups': [post['data']['ups']],
                'downs': [post['data']['downs']],
                'score':  [post['data']['score']],
                'subreddit_name': [subreddit_name],
                'created_date': [datetime.utcfromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%d %H:%M:%S')]
            })
            crypto_df = pd.concat([crypto_df, new_df], ignore_index=True)
        return crypto_df
    
    def combine_and_save_subreddit_data(self):
        # Combine all subreddit data
        all_data = pd.concat([
            self.get_crypto_curr_data(),
            self.get_crypto_markets_data(),
            self.get_bitcoin_data(),
            self.get_eth_data(),
            self.get_binance_data(),
            self.get_solana_data(),
            self.get_uniswap_data(),
            self.get_cardano_data(),
            self.get_avax_data(),
            self.get_chainlink_data(),
            self.get_litecoin_data(),
            self.get_compound_data(),
            self.get_polygon_data()
        ], ignore_index=True)

        # Save to CSV
        all_data.to_csv('RAW_DATA/combined_subreddit_data.csv', index=False)
        print("Data saved to combined_subreddit_data.csv")

# reddit_api = RedditAPI()
# reddit_api.combine_and_save_subreddit_data()