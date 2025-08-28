import streamlit as st
from modules.visualize_sub_module.fix_arrow_module import fix_arrow_compatibility
from modules.visualize_sub_module.bar_chart_module import plot_bar_chart
from modules.visualize_sub_module.pie_chart_module import plot_pie_chart
from modules.visualize_sub_module.line_chart_module import plot_line_chart
from modules.visualize_sub_module.histogram_module import plot_histogram
from modules.visualize_sub_module.boxplot_module import plot_boxplot
from modules.visualize_sub_module.scatter_module import plot_scatter_chart

def visualize_data(df):
    st.subheader("Data Visualization")

    # Fix Arrow compatibility first
    df = fix_arrow_compatibility(df)

    # Select chart type
    chart_type = st.selectbox(
        "Select chart Type",
        ["Bar", "Pie", "Line", "Scatter", "Histogram", "Boxplot"]
    )

    # Separate numeric and categorical columns
    num_cols = df.select_dtypes(include=['number']).columns.tolist()
    cat_cols = df.select_dtypes(exclude=['number']).columns.tolist()

    # Route to specific chart functions
    if chart_type == "Bar":
        plot_bar_chart(df, cat_cols)
    elif chart_type == "Pie":
        plot_pie_chart(df, cat_cols, num_cols)
    elif chart_type == "Line":
        if num_cols:
            plot_line_chart(df, num_cols)
        else:
            st.warning("No numeric columns available for line chart")
    elif chart_type == "Histogram":
        if num_cols:
            plot_histogram(df, num_cols)
        else:
            st.warning("No numeric columns available for histogram")
    elif chart_type == "Boxplot":
        if num_cols:
            plot_boxplot(df, num_cols)
        else:
            st.warning("No numeric columns available for boxplot")
    elif chart_type == "Scatter":
        plot_scatter_chart(df, num_cols)
