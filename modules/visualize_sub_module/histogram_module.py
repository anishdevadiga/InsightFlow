import matplotlib.pyplot as plt
import streamlit as st
from modules.download_module import download_chart

def plot_histogram(df, num_cols):
    col = st.selectbox("Select numeric column", num_cols)
    fig, ax = plt.subplots()
    ax.hist(df[col].dropna(), bins=20)
    ax.set_xlabel(col)
    ax.set_ylabel("Frequency")
    ax.set_title(f"Histogram of column : {col}")
    st.pyplot(fig)
    download_chart(fig, f"Histogram_{col}.png")
