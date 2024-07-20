import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Assume df is your DataFrame loaded with the necessary data
df = pd.read_csv('/Users/justinfarnan_hakkoda/capstone_project/Capstone_Project/Cleaned_Data/cleaned_crypto_data.csv')
df.set_index('time', inplace=True)
df.index = pd.to_datetime(df.index)


def home_page():
    st.title("Home Page")
    st.write("Welcome to the Guardians of the Crypto App!")

def about_page():
    st.title("About Page")
    st.write("This is a comprehensive cryptocurrency analysis dashboard built with Streamlit and Plotly.")

def comprehensive_crypto_analysis():
    st.title("Comprehensive Cryptocurrency Analysis Dashboard")

    # Horizontal filters
    col1, col2, col3 = st.columns(3)

    with col1:
        selected_crypto = st.selectbox(
            'Select Cryptocurrency',
            df['product_id'].unique(),
            index=0
        )

    with col2:
        start_date = st.date_input('Start date', df.index.min().date())

    with col3:
        end_date = st.date_input('End date', df.index.max().date())

    # Filter data based on selections
    filtered_data = df[(df['product_id'] == selected_crypto) &
                    (df.index >= pd.to_datetime(start_date)) & (df.index <= pd.to_datetime(end_date))]

    # Create subplots
    fig = make_subplots(rows=3, cols=2, shared_xaxes=True, vertical_spacing=0.10,horizontal_spacing=0.05,
                        subplot_titles=('Percentage Change', 'Volume', 'RSI', 'MACD', 'Momentum', 'Volatility'))

    # Percentage Change plot
    fig.add_trace(go.Scatter(x=filtered_data.index, y=filtered_data['pct_change'], name='Percentage Change'), row=1, col=1)

    # Volume plot
    fig.add_trace(go.Bar(x=filtered_data.index, y=filtered_data['volume'], name='Volume'), row=1, col=2)

    # RSI plot with critical levels
    fig.add_trace(go.Scatter(x=filtered_data.index, y=filtered_data['RSI'], name='RSI'), row=2, col=1)
    fig.add_hline(y=70, line_dash="dash", line_color="red", row=2, col=1)
    fig.add_hline(y=30, line_dash="dash", line_color="green", row=2, col=1)

    # MACD plot
    fig.add_trace(go.Scatter(x=filtered_data.index, y=filtered_data['MACD'], name='MACD'), row=2, col=2)
    fig.add_trace(go.Scatter(x=filtered_data.index, y=filtered_data['Signal_Line'], name='Signal Line', line=dict(color='red', dash='dot')), row=2, col=2)

    # Momentum plot
    fig.add_trace(go.Scatter(x=filtered_data.index, y=filtered_data['momentum_7d'], name='7-Day Momentum'), row=3, col=1)

    # Volatility plot
    fig.add_trace(go.Scatter(x=filtered_data.index, y=filtered_data['volatility_30d'], name='30-Day Volatility'), row=3, col=2)

    fig.update_layout(height=900, width=1200, title_text=f"Comprehensive Analysis for {selected_crypto}")

    # Display the plot
    st.plotly_chart(fig)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Crypto Analysis", "About"])

# Page navigation logic
if page == "Home":
    home_page()
elif page == "Crypto Analysis":
    comprehensive_crypto_analysis()
elif page == "About":
    about_page()