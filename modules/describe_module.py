import streamlit as st
import pandas as pd

#providing description for the module

def describe_dataset(df:pd.DateFrame):
    st.subheader("Dataset Overview")
    rows,cols=df.shape
    st.write(f"-Number of rows:{rows}")
    st.write(f"-Number of columns :{cols}")
    st.write(f"-Column names:{list(df.columns)}")

    st.markdown("--Missing value--")
    st.dataframe(df.isna().sum().to_frame("missing_count"))

    st.markdown("--Statistical Summary--")
    st.dataframe(df.describe(include='all'))

    with st.expander("Show first 10 rows"):
        st.dataframe(df.head(10))
