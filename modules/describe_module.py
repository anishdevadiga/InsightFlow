import streamlit as st
import pandas as pd

def describe_dataset(df:pd.DateFrame):
    st.subheader("Dataset Overview")
    rows,cols=df.shape
    st.write(f"-Number of rows:{rows}")
    st.write(f"-Number of columns :{cols}")
    st.write(f"-Column names:{list(df.columns)}")

    st