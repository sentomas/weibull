from typing import List, Dict, Any
import pandas as pd

# Define a custom type for the uploaded test data
TestData = pd.DataFrame

# Define a custom type for the Weibull distribution parameters
WeibullParameters = Dict[str, float]

# Define a custom type for reliability metrics
ReliabilityMetrics = Dict[str, Any]

# Define a custom type for the report content
ReportContent = Dict[str, Any]

# Define a custom type for the visualization data
VisualizationData = List[Dict[str, float]]