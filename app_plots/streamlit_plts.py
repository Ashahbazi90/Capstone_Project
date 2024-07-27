import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import matplotlib.dates as mdates
import plotly.express as px
import plotly.graph_objects as go
from ipywidgets import interact, Dropdown
from plotly.subplots import make_subplots
import ipywidgets as widgets
from ipywidgets import interact, IntSlider, Dropdown, IntRangeSlider
import ipywidgets as widgets
import streamlit as st
from datetime import datetime
# Configuration to suppress warnings
warnings.filterwarnings('ignore')

# Additional configurations for better control over visualizations (optional)
plt.style.use('ggplot')  # For ggplot-like style in plots
pd.options.display.max_columns = None 


### read in the file that will be used for the plots
file_path = '/Users/justinfarnan_hakkoda/capstone_project/Capstone_Project/Cleaned_Data/cleaned_crypto_updated_722.csv'
df = pd.read_csv(file_path)
df['time'] = pd.to_datetime(df['time'])
df.set_index('time', inplace = True)

def comprehensive_crypto_analysis():
    st.title("Comprehensive Cryptocurrency Analysis Dashboard")

    # Filter Section
    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        selected_crypto = st.selectbox(
            'Select Cryptocurrency',
            df['product_id'].unique(),
            index=0,
            key='crypto_select'
        )

    with col2:
        start_date = st.date_input(
            'Start date', 
            df.index.min().date(),
            key='start_date'
        )

    with col3:
        end_date = st.date_input(
            'End date', 
            df.index.max().date(),
            key='end_date'
        )

    # Filter data based on selections
    filtered_data = df[(df['product_id'] == selected_crypto) &
                       (df.index >= pd.to_datetime(start_date)) & 
                       (df.index <= pd.to_datetime(end_date))]

    # Create subplots with 2 rows and 3 columns
    fig = make_subplots(
        rows=2, cols=3, 
        shared_xaxes=True, 
        vertical_spacing=0.1,
        horizontal_spacing=0.05,
        subplot_titles=(
            'Percentage Change', 'Volume', 'RSI', 
            'MACD', '7-Day Momentum', '30-Day Volatility'
        )
    )

    # Percentage Change plot
    fig.add_trace(
        go.Scatter(x=filtered_data.index, y=filtered_data['pct_change'], name='Percentage Change', line=dict(color='#00FFFF')), 
        row=1, col=1
    )

    # Volume plot
    fig.add_trace(
        go.Bar(x=filtered_data.index, y=filtered_data['volume'], name='Volume', marker_color='#00FFFF'), 
        row=1, col=2
    )

    # RSI plot with critical levels
    fig.add_trace(
        go.Scatter(x=filtered_data.index, y=filtered_data['RSI'], name='RSI', line=dict(color='#FF69B4')), 
        row=1, col=3
    )
    fig.add_hline(y=70, line_dash="dash", line_color="red", row=1, col=3)
    fig.add_hline(y=30, line_dash="dash", line_color="green", row=1, col=3)

    # MACD plot
    fig.add_trace(
        go.Scatter(x=filtered_data.index, y=filtered_data['MACD'], name='MACD', line=dict(color='#FF69B4')), 
        row=2, col=1
    )
    fig.add_trace(
        go.Scatter(x=filtered_data.index, y=filtered_data['Signal_Line'], name='Signal Line', line=dict(color='red', dash='dot')), 
        row=2, col=1
    )

    # Momentum plot
    fig.add_trace(
        go.Scatter(x=filtered_data.index, y=filtered_data['momentum_7d'], name='7-Day Momentum', line=dict(color='#32CD32')), 
        row=2, col=2
    )

    # Volatility plot
    fig.add_trace(
        go.Scatter(x=filtered_data.index, y=filtered_data['volatility_30d'], name='30-Day Volatility', line=dict(color='#FFA500')), 
        row=2, col=3
    )

    fig.update_layout(
        height=800,
        width=1400,  # Increase the width to make plots wider
        title_text=f"Comprehensive Analysis for {selected_crypto}",
        title_font=dict(size=24),
        showlegend=False,
        plot_bgcolor='#1E1E1E',
        paper_bgcolor='#1E1E1E',
        font=dict(color='white'),
        margin=dict(l=50, r=50, t=100, b=50)
    )

    fig.update_layout(
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    # Update axes
    fig.update_xaxes(
        showgrid=True, gridwidth=1, gridcolor='#383838',
        showline=True, linewidth=1, linecolor='#383838',
        tickfont=dict(size=10)
    )
    fig.update_yaxes(
        showgrid=True, gridwidth=1, gridcolor='#383838',
        showline=True, linewidth=1, linecolor='#383838',
        tickfont=dict(size=10)
    )

    # Display the plot using the full width of the page
    st.plotly_chart(fig, use_container_width=True)


def generate_rolling_vol():
    st.title('30 Rolling Volatility')
  
    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        selected_crypto = st.selectbox(
            'Select Cryptocurrency',
            df['product_id'].unique(),
            index=0,
            key='crypto_select'
        )

    with col2:
        start_date = st.date_input(
            'Start date', 
            df.index.min().date(),
            key='start_date'
        )

    with col3:
        end_date = st.date_input(
            'End date', 
            df.index.max().date(),
            key='end_date'
        )

    # Convert start_date and end_date to datetime
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    filtered_data = df.loc[(df.index >= start_date) & 
                           (df.index <= end_date) & 
                           (df['product_id'] == selected_crypto)]

    # Plot
    fig = px.line(filtered_data.reset_index(), x='time', y='volatility_30d', color='product_id',
                  labels={'volatility_30d': '30-Day Volatility'},
                  title='30-Day Rolling Volatility for Each Cryptocurrency')

    st.plotly_chart(fig, use_container_width=True)

def generate_avg_pct_change_by_day_plot():
    """
    Generates an interactive line plot of average percentage change by day of the week for each cryptocurrency.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing the data with 'pct_change', 'product_id', and a datetime index.
    
    Returns:
    fig (plotly.graph_objs._figure.Figure): The interactive plotly figure.
    """
    st.title('Average Daily Percentage Change by Day of the Week')
    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        selected_crypto = st.selectbox(
            'Select Cryptocurrency',
            df['product_id'].unique(),
            index=0,
            key='crypto_select'
        )

    with col2:
        start_date = st.date_input(
            'Start date', 
            df.index.min().date(),
            key='start_date'
        )

    with col3:
        end_date = st.date_input(
            'End date', 
            df.index.max().date(),
            key='end_date'
        )
    # Convert start_date and end_date to datetime
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    filtered_data = df.loc[(df.index >= start_date) & 
                           (df.index <= end_date) & 
                           (df['product_id'] == selected_crypto)]
    # Calculate average percentage change by day of the week for each product
    avg_pct_change_by_day = filtered_data.groupby(['product_id', 'day_of_week', 'day_name'])['pct_change'].mean().reset_index()

    # Ensure the data is sorted by day of the week to avoid plotting issues
    avg_pct_change_by_day.sort_values(by=['product_id', 'day_of_week'], inplace=True)

    # Generate the interactive line plot
    fig = px.line(avg_pct_change_by_day, x='day_name', y='pct_change', color='product_id',
                  title='Average Percentage Change by Day of the Week',
                  labels={'day_name': 'Day of the Week', 'pct_change': 'Average Percentage Change (%)'},
                  category_orders={'day_name': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']})

    # Set all traces to be hidden by default, appear on legend click
    st.plotly_chart(fig, use_container_width=True)



