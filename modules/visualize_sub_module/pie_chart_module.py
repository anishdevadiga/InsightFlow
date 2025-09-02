import streamlit as st
import pandas as pd
import plotly.express as px
from modules.download_module import download_chart

def plot_pie_chart(df, cat_cols, num_cols, col):
    # Categorical column
    if col in cat_cols:
        vc = df[col].value_counts().reset_index()
        vc.columns = [col, "Count"]
        fig = px.pie(vc, names=col, values="Count", title=f"Pie Chart: {col}")
    
    # Numeric column (binned)
    elif col in num_cols:
        bins = st.slider("Select number of bins for numeric pie chart", 2, 10, 5)
        binned_data = pd.cut(df[col], bins=bins)
        vc = binned_data.value_counts().reset_index()
        vc.columns = ["Range", "Count"]
        fig = px.pie(vc, names="Range", values="Count", title=f"Pie Chart: {col}")
    
    else:
        st.error("Invalid column selected for Pie Chart")
        return

    st.plotly_chart(fig)
    download_chart(fig, f"Pie_Chart_{col}.png")
