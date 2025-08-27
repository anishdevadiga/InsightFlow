import streamlit as st
from modules.upload_module import upload_file
from modules.describe_module import describe_dataset
from modules.visualization_module import visualize_data
#from modules.ml_module import ml_models

def main():
    st.set_page_config(page_title="Insight-Flow",layout='wide',initial_sidebar_state="expanded")
    st.title("Insight-Flow ")

    df=upload_file()
    if df is None :
        st.info("Upload a csv file from the left sidebar to get started ")
    else:
        col1 ,col2,col3 =st.columns(3)

        with col1:
            describe_btn = st.button("Describe")
        with col2:
            visualize_btn=st.button("Visualize")
        with col3:
            ml_btn=st.button('ML models')
        
        if describe_btn:
            describe_dataset(df)
        elif visualize_btn:
            pass
            visualize_data(df)
        elif ml_btn:
            st.subheader("Machine Learning models")
            st.write("Under development")
            #ml_models(df)

if __name__ == "__main__":
    main()