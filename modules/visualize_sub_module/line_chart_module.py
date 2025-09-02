import seaborn as sns
import streamlit as st
from modules.download_module import download_chart

def plot_line_chart(df, num_cols, col):
    col = st.selectbox("Select numeric column", num_cols)

    # Create line chart with seaborn
    fig = sns.relplot(
        data=df.reset_index(),
        x=df.reset_index().index,
        y=col,
        kind="line",
        height=5,
        aspect=1.5,
        marker="o",
        color="steelblue"
    )

    fig.set_axis_labels("Index", col)
    fig.set_titles(f"Line plot : {col}")

    st.pyplot(fig)
    download_chart(fig, f"Line_{col}.png")

