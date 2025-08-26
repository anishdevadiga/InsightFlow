import streamlit as st
from modules.upload_module import upload_file

def main():
    st.set_page_config(page_title="Insight-Flow",layout='wide',initial_sidebar_state="expanded")
    st.title("Insight flow ")

    df=upload_file()
    if df is None :
        st.info("Upload a csv file from the left sidebar to get started ")
    

if __name__ == "__main__":
    main()