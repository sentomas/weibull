import streamlit as st
import pandas as pd

def upload_file():
    st.title("Upload Test Data")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        try:
            # Read the uploaded CSV file
            data = pd.read_csv(uploaded_file)
            st.success("File uploaded successfully!")
            
            # Display the first few rows of the dataframe
            st.write("Preview of the uploaded data:")
            st.dataframe(data.head())
            
            # Convert the first column to numeric values
            data[data.columns[0]] = pd.to_numeric(data[data.columns[0]], errors='coerce')
            
            # Validate the data (you can add more validation rules as needed)
            if validate_data(data):
                st.success("Data validation successful!")
                return data
            else:
                st.error("Data validation failed. Please check your file format.")
        except Exception as e:
            st.error(f"Error reading the file: {e}")
    
    return None

def validate_data(data):
    # Validation: At least one numeric column with non-null values
    numeric_cols = data.select_dtypes(include='number')
    return not numeric_cols.empty and numeric_cols.shape[1] > 0 and numeric_cols.notnull().sum().sum() > 0