import streamlit as st
import pandas as pd

def upload_file():
    st.sidebar.header("Upload Dataset")
    upload_file=st.sidebar.file_uploader("CSV file",type=["csv"])
    use_example=st.sidebar.checkbox("Use example Iris dataset",value=False)

    st.markdown(
    """
    <style>
    /* Sidebar container */
    section[data-testid="stSidebar"] {
        border-right: 1px solid #c7c4c4ff; 
        border-radius: 12px;  /* Right-side colored border */
        padding: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    if upload_file is not None:
        try:
            df=pd.read_csv(upload_file)
            st.sidebar.success("File uploaded Successfully")
            return df   
        except Exception as e:
            st.sidebar.error(f"Error reading csv: {e}")   
            return None 
    elif use_example:
        #small example dataset to get started
        from sklearn.datasets import load_iris
        iris=load_iris(as_frame=True)
        df=iris.frame
        st.sidebar.success("Loaded example iris dataset")
        return df
    else:
        return None