import matplotlib.pyplot as plt
import streamlit as st
from modules.download_module import download_chart

def plot_line_chart(df, num_cols):
    col = st.selectbox("Select numeric column", num_cols)
    fig, ax = plt.subplots()
    ax.plot(df[col].reset_index(drop=True))
    ax.set_ylabel(col)
    ax.set_title(f"Line plot : {col}")
    st.pyplot(fig)
    download_chart(fig, f"Line_{col}.png")
