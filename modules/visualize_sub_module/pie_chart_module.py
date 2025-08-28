import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from modules.download_module import download_chart

def plot_pie_chart(df, cat_cols, num_cols):
    col = st.selectbox("Select Column", df.columns)
    fig, ax = plt.subplots()

    if col in cat_cols:
        vc = df[col].value_counts()
        vc.plot(kind='pie', ax=ax, autopct='%1.1f%%')
        ax.set_ylabel("")
        ax.set_title(f"Pie Chart: {col}")
    elif col in num_cols:
        bins = st.slider("Select number of bins for numeric pie chart", 2, 10, 5)
        binned_data = pd.cut(df[col], bins=bins)
        vc = binned_data.value_counts()
        vc.plot(kind="pie", ax=ax, autopct='%1.1f%%')
        ax.set_title(f"Pie Chart: {col}")
    else:
        st.error("Invalid column selected for Pie Chart")
        return

    st.pyplot(fig)
    download_chart(fig, f"Pie_Chart_{col}.png")
