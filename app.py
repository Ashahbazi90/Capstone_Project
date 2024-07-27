import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from app_plots.streamlit_plts import generate_rolling_vol, generate_avg_pct_change_by_day_plot, comprehensive_crypto_analysis


# Assume df is your DataFrame loaded with the necessary data
# df = pd.read_csv('/Users/justinfarnan_hakkoda/capstone_project/Capstone_Project/Cleaned_Data/cleaned_crypto_updated_722.csv')
# df.set_index('time', inplace=True)
# df.index = pd.to_datetime(df.index)

st.set_page_config(layout="wide")

def home_page():
    st.title("Home Page")
    st.write("Welcome to the Guardians of the Crypto App!")

def about_metrics():
    st.title("Explaning Trading Metrics")
    select_metric = st.selectbox('Select Metrc',['Percentage Change', 'Volume', 'RSI', 'MACD', 'Momentum', 'Volatility'])
    if select_metric == 'Percentage Change':
        st.markdown("## Percentage Change")
        st.markdown('### What it is')
        st.write('This metrics shows how much the price has changed over a given period.')
        st.markdown('### How to interpret it')
        st.write('If the percentage is postive it means the pprice went up, if its negative it means it went down.')
    if select_metric == 'Volume':
        st.markdown("## Volume")
        st.markdown('### What it is')
        st.write('Inicates the number of units cryptocurreinces have been traded over a certain period')
        st.markdown('### How to interpret it')
        st.write('''If volume is high this means aot of trading activity whhich can mean there is a strong interst in that specfic token/coin.
                Low volume means the opposite, so less trading activity. You could see a high volume data when teh price increases and this could mean a strong buying interest''')
    if select_metric == 'RSI':
        st.markdown("## RSI (Relative Strength Index)")
        st.markdown('### What it is')
        st.write('Moomentum Indicator that measures the speed and change of price movements')
        st.markdown('### How to interpret it')
        st.write('''The RSI values range between 0 and 100, an RSI abve 70 suggests that the cyptocurrency might be overbought (the pirce may decrease soon).
                 If the RSI is below 30 this suggests it might be oversold and the price may increase soon. So if the RSI is 25 this could indicate that the crypto has been sold alot and could be due to a price increase''')
    if select_metric == 'MACD':
        st.markdown("## MACD (Moving Average Convergence Divergence)")
        st.markdown('### What it is')
        st.write('A Moving Average indicator that identifies buy and sell signals.')
        st.markdown('### How to interpret it')
        st.write('''The MACD idenitifies buy and sell signals by comparing the short term and long termm trends of the coin. It uses the difference between the 12 and 26 period EMAs (Exponential Moving Average),
                 with a 9 period EMA signal line.''')
    if select_metric == 'Momentum':
        st.markdown("## Momentum")
        st.markdown('### What it is')
        st.write('The speed of prices changes in a given coin.')
        st.markdown('### How to interpret it')
        st.write('''Momentum shows the rate of change in the price movement over a perod of time to help investors/traders determin the strength of a coin. This indicator can help show when the prices are rising (bullish momentum) or when prices fall (bearish momentum)''')
    if select_metric == 'Volatility':
        st.markdown("## Volatility")
        st.markdown('### What it is')
        st.write('This metric represents how much of a price swing there is around the average price.')
        st.markdown('### How to interpret it')
        st.write('''This 30-day volatility chart shows periods with larger spikes indicating higher volatility, while flatter lines indicate lower volatility. Observing how volatility changes year by year can help identify trends of increasing or decreasing volatility.''')


def crypto_analysis():
    st.title("Comprehensive Cryptocurrency Analysis Dashboard")
    comprehensive_crypto_analysis()

def thirty_day_vol():
    st.title("30 Day Rolling Volatility")
    generate_rolling_vol()

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Metrics", "Crypto Analysis",
                                  "30 Day Volatility", "Average Daily Percentage Change by Day of the Week"])

# Page navigation logic
if page == "Home":
    home_page()
elif page == "About Metrics":
    about_metrics()
elif page == "Crypto Analysis":
    comprehensive_crypto_analysis()
elif page == '30 Day Volatility':
    generate_rolling_vol()
elif page == 'Average Daily Percentage Change by Day of the Week':
    generate_avg_pct_change_by_day_plot()

# elif page == "Test":
#     comprehensive_crypto_analysis()