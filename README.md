# Project Overview

### Objective

The "Guardians of the Crypto" project aims to develop a user-friendly application for predicting cryptocurrency price changes using historical data. By building a predictive model, the application provides traders and investors with forecasts to improve decision-making accuracy and reduce financial risks. The project explores the effectiveness of these predictive tools to guide better investment strategies and highlights the limitations of current analytical techniques.

### Data Extraction

The data extraction process is handled by a Python script, extract_coinbase.py, which collects three years' worth of data for ten cryptocurrencies in six-month intervals. This approach addresses the limitations of the Coinbase API, which restricts pulling large data sets at once. The extracted data is combined and saved as RAW_Data/train_historic_updt_717.csv for model training. A separate RAW_Data/test_weekago_updt_717.csv file is created using the current week's data to forecast against once the model is built.

The ten cryptocurrencies analyzed are:

1. BTC-USD (Bitcoin)
2. ETH-USD (Ethereum)
3. SOL-USD (Solana)
4. ADA-USD (Cardano)
5. LINK-USD (Chainlink)
6. AVAX-USD (Avalanche)
7. LTC-USD (Litecoin)
8. UNI-USD (Uniswap)
9. COMP-USD (Compound)
10. MATIC-USD (Polygon)

The extracted and engineered features include:

- Time
- Low
- High
- Open
- Close
- Volume
- Price Change
- Average Price
- Volatility
- Product ID

### Exploratory Data Analysis

A comprehensive exploratory data analysis (EDA) was conducted using the project_analysis.ipynb notebook. This step involved understanding the data, creating additional features and metrics, and generating visualizations to inform the modeling process and identify necessary data cleaning steps. The EDA helped uncover insights that guided subsequent modeling decisions and ensured data quality.

### Modeling Process

The modeling phase was carried out in the data_preparation_and_modeling.ipynb notebook. This notebook includes various techniques for preparing Time Series data, such as specific data splits, grouping, scaling, filling null values, and adding or removing features that could impact modeling accuracy. The cleaned data used for modeling is stored in cleaned_data/cleaned_crypto_updated_722.csv.

Multiple models were developed for time series forecasting, and the Ridge Regression model emerged as the best choice due to its ability to handle multicollinearity effectively and its minimal overfitting compared to other models. After fine-tuning the Ridge Regression model, forecasted values were generated.

The final step involved comparing these forecasted values to the untouched RAW_Data/test_weekago_updt_717.csv dataset to assess the model's accuracy. The comparison is visually represented in a graph, highlighting the alignment between forecasted and actual values.

### Streamlit Application

The project culminates in a Streamlit application designed to help traders understand cryptocurrency price movements and analyze various indicators. The application features multiple pages with charts that provide insights into price trends, including those derived from the exploratory data analysis (EDA). Notably, charts such as Average Percent Change by Weekday and 30-Day Rolling Volatility were included due to their impact on trading decisions.

Additionally, the application includes a page displaying forecasted values over actual values, offering traders an opportunity to evaluate the Ridge Regression model's reliability in predicting price directions across different cryptocurrencies.

These plots are stored in a folder named app_plots and managed by a file called app_plots/streamlit_plts.py.

The main application resides in the app.py file, which imports all the plots from app_plots/streamlit_plts.py and organizes them into various sections. Users can select different pages to view specific plots based on their interests. The application is hosted on GitHub and can be accessed via this link: https://guardiasnsofcrypto.streamlit.app/
