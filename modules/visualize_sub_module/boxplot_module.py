import matplotlib.pyplot as plt
import streamlit as st
from modules.download_module import download_chart

def plot_boxplot(df, num_cols):
    col = st.selectbox("Select numeric column", num_cols)
    fig, ax = plt.subplots()
    ax.boxplot(df[col].dropna())
    ax.set_ylabel(col)
    ax.set_title(f"Boxplot: {col}")
    st.pyplot(fig)
    download_chart(fig, f"Boxplot_{col}.png")
