## Abstract
[“Guardians of the Crypto”](https://guardiasnsofcrypto.streamlit.app/) is a Streamlit application designed to address the challenges posed by the highly volatile cryptocurrency market. By leveraging advanced data science techniques and machine learning algorithms, the application offers accurate and timely predictions of cryptocurrency price movements, aiding users in making informed trading decisions. The application provides a comprehensive solution, integrating historical price data, sentiment analysis, and technical indicators to empower novice and experienced traders alike.
## Table of Contents
1. Business Background
2. Problem Statement
3. Summary of Findings
4. Business Questions
5. Scope of Analysis
6. Approach
7. Limitations
8. Solution Details
9. Concluding Summary
10. Call to Action (CTA)
## Business Background
The cryptocurrency market has gained significant popularity over the past decade, offering new opportunities for investment and trading. However, the market’s extreme volatility and unpredictability present substantial risks, making it challenging for investors and traders to make well-informed decisions. Traditional investment strategies often fail to keep up with the dynamic nature of cryptocurrency markets, necessitating the development of advanced analytical tools that can provide accurate price predictions and insights.
## Problem Statement
Cryptocurrency traders and investors face the critical issue of navigating the market’s volatility, which can lead to significant financial losses and deter potential investors. The lack of reliable predictive tools exacerbates this problem, leaving market participants without the necessary resources to make informed decisions. This white paper aims to address this issue by presenting a solution that leverages historical data and machine learning algorithms to forecast cryptocurrency price movements accurately.
## Summary of Findings
Through extensive data analysis and modeling, [“Guardians of the Crypto”](https://guardiasnsofcrypto.streamlit.app/) identified Ridge Regression as the most reliable model for predicting cryptocurrency price movements. Despite some overfitting, this model consistently performed well across various metrics, including adjusted R-squared, mean squared error, and root mean squared error. The application also demonstrated the importance of using higher-frequency data and integrating sentiment analysis to improve predictive accuracy. The final solution is a user-friendly Streamlit application that showcases trading indicators and forecasted percentage change predictions, providing a valuable tool for traders and investors.
## Business Questions
To address the problem statement, the following business questions were defined:
1. How can historical price data be leveraged to forecast future cryptocurrency price movements?
2. What machine learning algorithms are most effective for predicting cryptocurrency prices?
3. How can the application be designed to cater to both novice and experienced traders?
4. What additional data sources (e.g., sentiment analysis) can be integrated to enhance predictive accuracy?
5. How can the application be made accessible and user-friendly?
## Scope of Analysis
The scope of this analysis includes:
- **Included:** Historical cryptocurrency price data, machine learning algorithms (Ridge Regression, XGBoost, etc.), sentiment analysis, and technical indicators (RSI, MACD, Bollinger Bands).
- **Excluded:** High-frequency trading data, proprietary trading algorithms, and cryptocurrencies with limited historical data.
The selection was made to focus on widely traded cryptocurrencies (e.g., Bitcoin, Ethereum) and commonly used technical indicators, ensuring the solution’s relevance and applicability to a broad audience.
## Approach
To answer the business questions, the following methodology was used:
1. **Data Collection:** Historical price data for multiple cryptocurrencies was extracted using the [Coinbase API](https://github.com/Ashahbazi90/Capstone_Project/blob/main/historic_api_pulls/extract_coinbase.py). Features such as price change, average price, volatility, and sentiment indicators were engineered.
2. **Modeling:** Various machine learning algorithms were evaluated, including Ridge Regression, XGBoost, and ARIMA. Detailed data preparation and modeling steps can be reviewed in this [notebook](https://github.com/Ashahbazi90/Capstone_Project/blob/main/main_ds_notebooks/data_preparation_and_modeling.ipynb). Ridge Regression was selected for its robustness in handling multicollinearity and consistent performance across all evaluated metrics.
3. **Application Development:** The application was developed using Streamlit, offering an intuitive interface for users to access and interpret data. It provides tools to filter by specific cryptocurrencies and timeframes, displaying relevant trading indicators and forecasted price changes. The implementation details are available in the [Streamlit application code](https://github.com/Ashahbazi90/Capstone_Project/blob/main/app.py), with specific plots handled by the [streamlit_plts.py script](https://github.com/Ashahbazi90/Capstone_Project/blob/main/app_plots/streamlit_plts.py).
## Limitations
The analysis encountered several limitations:
1. **Data Granularity:** The analysis was limited to daily price data, which may not capture the high-frequency fluctuations characteristic of cryptocurrency markets.
2. **Model Overfitting:** The Ridge Regression model exhibited slight overfitting, which could be mitigated with further hyperparameter tuning.
3. **BTC-USD Forecasting:** The model showed inconsistencies when forecasting Bitcoin prices, suggesting the need for specialized models for certain cryptocurrencies.
4. **Exclusion of High-Frequency Trading:** The application is designed for daily trading decisions and may not be suitable for high-frequency trading scenarios.
## Solution Details
[“Guardians of the Crypto”](https://guardiasnsofcrypto.streamlit.app/) offers a comprehensive solution that integrates multiple data sources and advanced analytical techniques to provide accurate cryptocurrency price predictions. The Streamlit application features:
- **Historical Data Analysis:** Users can explore historical price data for various cryptocurrencies, identify trends, and make informed predictions. The analysis methods are detailed in this [notebook](https://github.com/Ashahbazi90/Capstone_Project/blob/main/main_ds_notebooks/project_analysis.ipynb).
- **Technical Indicators:** The application displays key trading metrics, such as RSI, MACD, and Bollinger Bands, providing insights into market conditions.
- **Forecasting:** The application uses Ridge Regression to forecast percentage changes in cryptocurrency prices, helping users anticipate market movements.
- **User-Friendly Interface:** The application is designed to cater to both novice and experienced traders, with an intuitive interface and customizable features.
## Concluding Summary
“Guardians of the Crypto” represents a significant advancement in cryptocurrency price prediction, offering a robust and user-friendly tool for traders and investors. The application leverages historical data, advanced machine learning algorithms, and sentiment analysis to provide accurate and timely forecasts. While the Ridge Regression model was identified as the most reliable, future work will focus on integrating higher-frequency data, improving model generalization, and expanding the application’s features to cater to a broader audience.
## Call to Action (CTA)
To explore the capabilities of “Guardians of the Crypto” and enhance your trading strategies, visit our [website](https://guardiasnsofcrypto.streamlit.app/) to access the Streamlit application. For personalized assistance or to discuss potential collaborations, schedule a call with our team today.
