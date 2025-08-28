import matplotlib.pyplot as plt
import streamlit as st
from modules.download_module import download_chart

def plot_scatter_chart(df, num_cols):
    if len(num_cols) < 2:
        st.warning("Need at least two numeric columns for scatter plot")
        return

    col_x = st.selectbox("X axis", num_cols, index=0)
    col_y = st.selectbox("Y axis", num_cols, index=1)

    fig, ax = plt.subplots()
    ax.scatter(df[col_x], df[col_y])
    ax.set_xlabel(col_x)
    ax.set_ylabel(col_y)
    ax.set_title(f"Scatter: {col_x} vs {col_y}")

    st.pyplot(fig)
    download_chart(fig, f"Scatter_Plot_{col_x}_{col_y}.png")
