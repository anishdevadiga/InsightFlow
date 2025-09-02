import streamlit as st
import plotly.express as px
from modules.download_module import download_chart

def plot_scatter_chart(df, num_cols):
    if len(num_cols) < 2:
        st.warning("Need at least two numeric columns for scatter plot")
        return

    col_x = st.selectbox("X axis", num_cols, index=0)
    col_y = st.selectbox("Y axis", num_cols, index=1)

    # Create scatter plot using Plotly
    fig = px.scatter(
        df,
        x=col_x,
        y=col_y,
        title=f"Scatter: {col_x} vs {col_y}",
        labels={col_x: col_x, col_y: col_y},
        color=None  # can add color option if desired
    )

    st.plotly_chart(fig)
    download_chart(fig, f"Scatter_Plot_{col_x}_{col_y}.png")
