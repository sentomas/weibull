import numpy as np
from scipy.stats import weibull_min
from scipy.special import gamma

def calculate_weibull_parameters(data):
    """Calculate Weibull shape and scale parameters from the first numeric column in data."""
    # Select the first numeric column
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) == 0:
        raise ValueError("No numeric columns found in the uploaded data.")
    col = numeric_cols[0]
    values = data[col].dropna().values.flatten()
    shape, loc, scale = weibull_min.fit(values, floc=0)
    return shape, scale

def calculate_reliability(shape, scale, time):
    return np.exp(- (time / scale) ** shape)

def generate_reliability_data(shape, scale, time_range):
    reliability_data = {}
    for time in time_range:
        reliability_data[time] = calculate_reliability(shape, scale, time)
    return reliability_data

def weibull_parameters_summary(shape, scale):
    return {
        "Shape Parameter": shape,
        "Scale Parameter": scale,
        "Mean": scale * gamma(1 + 1 / shape),
        "Variance": (scale ** 2) * (gamma(1 + 2 / shape) - (gamma(1 + 1 / shape) ** 2))
    }