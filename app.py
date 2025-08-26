import streamlit as st
from modules.upload_module import upload_file
from modules.describe_module import describe_dataset
from modules.visualization_module import visualize_data

def main():
    st.set_page_config(page_title="Insight-Flow",layout='wide',initial_sidebar_state="expanded")
    st.title("Insight-Flow ")

    df=upload_file()
    if df is None :
        st.info("Upload a csv file from the left sidebar to get started ")
    else:
        describe_dataset(df)
        print()
        visualize_data(df)
    

if __name__ == "__main__":
    main()