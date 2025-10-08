import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import weibull_min

def plot_weibull_distribution(data, shape, scale):
    """Plot the Weibull distribution based on the uploaded data and parameters."""
    # Get the first numeric column
    numeric_col = data.select_dtypes(include=[np.number]).columns[0]
    values = data[numeric_col].dropna().values.flatten()
    x = np.linspace(0, max(values), 100)
    y = weibull_min.pdf(x, shape, scale=scale)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='Weibull Distribution', color='blue')
    plt.hist(values, bins=30, density=True, alpha=0.5, color='gray', label='Data Histogram')
    plt.title('Weibull Distribution Fit')
    plt.xlabel('Data Values')
    plt.ylabel('Density')
    plt.legend()
    st.pyplot(plt)

def plot_reliability_function(data):
    """Plot the reliability function based on the uploaded data."""
    shape, loc, scale = weibull_min.fit(data, floc=0)
    x = np.linspace(0, max(data), 100)
    reliability = weibull_min.sf(x, shape, loc=loc, scale=scale)

    plt.figure(figsize=(10, 6))
    plt.plot(x, reliability, label='Reliability Function', color='green')
    plt.title('Reliability Function')
    plt.xlabel('Data Values')
    plt.ylabel('Reliability')
    plt.legend()
    st.pyplot(plt)

def plot_reliability(data, shape, scale):
    """Plot the reliability function using provided Weibull parameters."""
    numeric_col = data.select_dtypes(include=[np.number]).columns[0]
    values = data[numeric_col].dropna().values.flatten()
    x = np.linspace(0, max(values), 100)
    reliability = weibull_min.sf(x, shape, scale=scale)

    plt.figure(figsize=(10, 6))
    plt.plot(x, reliability, label='Reliability Function', color='green')
    plt.title('Reliability Function')
    plt.xlabel('Data Values')
    plt.ylabel('Reliability')
    plt.legend()
    st.pyplot(plt)

def visualize_data(data):
    """Generate visualizations for the uploaded data."""
    st.subheader('Weibull Distribution Visualization')
    shape, loc, scale = weibull_min.fit(data, floc=0)
    plot_weibull_distribution(data, shape, scale)
    
    st.subheader('Reliability Function Visualization')
    plot_reliability_function(data)