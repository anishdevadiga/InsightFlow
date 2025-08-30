import streamlit as st
from modules.upload_module import upload_file
from modules.describe_module import describe_dataset
from modules.visualization_module import visualize_data
from modules.ml_module import run_ml

def main():
    st.set_page_config(page_title="Insight-Flow", layout="wide", initial_sidebar_state="expanded")
    st.title("Insight-Flow")

    df = upload_file()
    if df is None:
        st.info("Upload a CSV file from the left sidebar to get started")
    else:
        # Initialize session state
        if "active_tab" not in st.session_state:
            st.session_state.active_tab = "Describe"

        col1, col2, col3 = st.columns(3)

        # --- Button Styling ---
        def button_style(tab_name, label):
            if st.session_state.active_tab == tab_name:
                return st.button(label, use_container_width=True, key=tab_name)
            else:
                return st.button(label, use_container_width=True, key=tab_name)

        with col1:
            if button_style("Describe", "📝 Describe"):
                st.session_state.active_tab = "Describe"
        with col2:
            if button_style("Visualize", "📊 Visualize"):
                st.session_state.active_tab = "Visualize"
        with col3:
            if button_style("ML", "🤖 ML Models"):
                st.session_state.active_tab = "ML"

        # --- Info messages near button ---
        if st.session_state.active_tab == "Describe":
            st.info("📌 This will summarize your dataset (shape, columns, stats, etc.)")
            describe_dataset(df)

        elif st.session_state.active_tab == "Visualize":
            st.info("📌 This will create different charts and visualizations of your dataset")
            visualize_data(df)

        elif st.session_state.active_tab == "ML":
            st.info("📌 This will run machine learning models and predictions")
            run_ml(df)


if __name__ == "__main__":
    main()
