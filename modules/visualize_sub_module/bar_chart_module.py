import matplotlib.pyplot as plt
import streamlit as st
from modules.download_module import download_chart

def plot_bar_chart(df, cat_cols):
    col = st.selectbox("Select column for visualization", df.columns)
    fig, ax = plt.subplots()

    if col in cat_cols:
        vc = df[col].value_counts()
        vc.plot(kind="bar", ax=ax)
        ax.set_ylabel("Count")
        ax.set_xlabel(col)
        ax.set_title(f"Bar Chart : {col}")
    else:
        df[col].plot(kind='bar', ax=ax)
        ax.set_ylabel(col)
        ax.set_xlabel("Index")
        ax.set_title(f"Bar Chart : {col}")

    st.pyplot(fig)
    download_chart(fig, f"Bar_Chart_{col}.png")
