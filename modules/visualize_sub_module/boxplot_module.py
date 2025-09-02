import seaborn as sns
import streamlit as st
from modules.download_module import download_chart

def plot_boxplot(df, num_cols, col):
    # Create the seaborn boxplot
    fig = sns.catplot(
        data=df,
        y=col,
        kind="box",
        height=5,
        aspect=1.2,
        palette="Set2"
    )

    fig.set_axis_labels("", col)
    fig.set_titles(f"Boxplot: {col}")

    st.pyplot(fig)
    download_chart(fig, f"Boxplot_{col}.png")
