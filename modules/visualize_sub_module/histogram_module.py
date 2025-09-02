import seaborn as sns
import streamlit as st
from modules.download_module import download_chart

def plot_histogram(df, num_cols, col):
    # Create histogram with seaborn
    fig = sns.displot(
        data=df,
        x=col,
        bins=20,
        kde=False,   # set True if you also want a density curve
        height=5,
        aspect=1.3,
        color="skyblue"
    )

    fig.set_axis_labels(col, "Frequency")
    fig.set_titles(f"Histogram of column : {col}")

    st.pyplot(fig)
    download_chart(fig, f"Histogram_{col}.png")

