import streamlit as st
import pandas as pd
from components.upload import upload_file
from components.visualization import plot_weibull_distribution, plot_reliability
from components.report import generate_report
from utils.weibull import calculate_weibull_parameters

def main():
    st.set_page_config(page_title="Weibull Distribution Analysis", layout="wide")

    # Custom CSS for posh look
    st.markdown("""
        <style>
        .main {background-color: #f7f7fa;}
        .block-container {padding-top: 2rem;}
        .stButton>button {background-color: #4F8BF9; color: white; border-radius: 8px;}
        .stDownloadButton>button {background-color: #21bf73; color: white; border-radius: 8px;}
        .stSuccess {background-color: #e6f4ea;}
        .stHeader {font-size: 2rem; font-weight: 700; color: #4F8BF9;}
        .stSubheader {font-size: 1.2rem; font-weight: 600; color: #21bf73;}
        .stDataFrame {background-color: #fff; border-radius: 8px;}
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color: #4F8BF9;'>✨ Weibull Distribution Analysis App</h1>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 1px solid #4F8BF9;'>", unsafe_allow_html=True)

    left_col, right_col = st.columns([1, 2], gap="large")

    with left_col:
        st.markdown("<h2 class='stHeader'>📤 Upload Data</h2>", unsafe_allow_html=True)
        data = upload_file()
        if data is not None:
            st.markdown("<h3 class='stSubheader'>🔍 Preview of Uploaded Data</h3>", unsafe_allow_html=True)
            st.dataframe(data, use_container_width=True)
            st.write("Data types:", data.dtypes)

    with right_col:
        if data is not None:
            try:
                st.markdown("<h2 class='stHeader'>📊 Results & Visualizations</h2>", unsafe_allow_html=True)
                shape, scale = calculate_weibull_parameters(data)
                st.success(f"**Weibull Shape Parameter:** {shape:.4f}")
                st.success(f"**Weibull Scale Parameter:** {scale:.4f}")

                st.markdown("<h3 class='stSubheader'>📈 Weibull Distribution Chart</h3>", unsafe_allow_html=True)
                plot_weibull_distribution(data, shape, scale)

                st.markdown("<h3 class='stSubheader'>🛡️ Reliability Chart</h3>", unsafe_allow_html=True)
                plot_reliability(data, shape, scale)

                st.markdown("<hr>", unsafe_allow_html=True)
                if st.button("📝 Generate Report"):
                    report = generate_report(data, shape, scale)
                    st.success("Report generated successfully! You can download it below.")
                    st.download_button("⬇️ Download Report", report, file_name="weibull_report.docx")
            except Exception as e:
                st.error(f"Data validation failed. Please check your file format. Details: {e}")

if __name__ == "__main__":
    main()