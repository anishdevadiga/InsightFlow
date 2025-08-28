import streamlit as st

def fix_arrow_compatibility(df):
    """
    Ensures the dataframe is compatible with Streamlit's Arrow serialization.
    - Converts all 'object' dtype columns to strings.
    - Detects mixed-type columns and converts them to strings.
    """
    for col in df.columns:
        # Get unique data types for the column
        unique_types = df[col].map(type).unique()

        # If there are multiple types in the same column → convert to string
        if len(unique_types) > 1:
            st.warning(f"Column '{col}' has mixed data types: {unique_types}. Converting to string.")
            df[col] = df[col].astype(str)

        # If the column is object → convert to string for Arrow compatibility
        elif df[col].dtype == 'object':
            df[col] = df[col].astype(str)

    return df
