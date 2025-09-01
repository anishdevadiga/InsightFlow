import streamlit as st
from modules.upload_module import upload_file
from modules.describe_module import describe_dataset
from modules.visualization_module import visualize_data
from modules.ml_module import run_ml

def main():
    st.set_page_config(page_title="Insight-Flow", layout="wide", initial_sidebar_state="expanded")
    st.title("Insight-Flow")

    # Initialize session state variables if they don't exist
    if "df" not in st.session_state:
        st.session_state.df = None
    if "action" not in st.session_state:
        st.session_state.action = None

    # Upload CSV
    uploaded_df = upload_file()
    if uploaded_df is not None:
        st.session_state.df = uploaded_df

    df = st.session_state.df

    if df is None:
        st.info("Upload a CSV file from the left sidebar to get started")
    else:
        # Put buttons in one row
        col1, col2, col3 = st.columns(3)

        # --- Action buttons ---
        if col1.button("📝 Describe", use_container_width=True):
            st.session_state.action = "describe"
        if col2.button("📊 Visualize", use_container_width=True):
            st.session_state.action = "visualize"
        if col3.button("🤖 ML Models", use_container_width=True):
            st.session_state.action = "ml"

        # --- Action handling with loader ---
        if st.session_state.action == "describe":
            with st.spinner("Summarizing your dataset..."):
                st.info("This will summarize your dataset (shape, columns, stats, etc.)")
                describe_dataset(df)

        elif st.session_state.action == "visualize":
            with st.spinner("Creating visualizations..."):
                st.info("This will create different charts and visualizations of your dataset")
                visualize_data(df)

        elif st.session_state.action == "ml":
            with st.spinner("Running ML models..."):
                st.info("This will run machine learning models and predictions")
                run_ml(df)


if __name__ == "__main__":
    main()
