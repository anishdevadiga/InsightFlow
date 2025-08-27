import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def fix_arrow_compatibility(df):
    """
    Ensures the dataframe is compatible with Streamlit's Arrow serialization.
    - Converts all 'object' dtype columns to strings.
    - Detects mixed-type columns and converts them to strings.
    """
    for col in df.columns:
        unique_types=df[col].apply(lambda x:type(x).unique())
        if len(unique_types)>1:
            st.warning(f"Column {col} has mixed data types {unique_types}")
            df[col]=df[col].astype(str)
        elif df[col].dtype=='object':
            df[col]=df[col].astype(str)
    
    return df
def visualize_data(df):
    st.subheader("Data Visualization")
    chart_type=st.selectbox("Select chart Type",["Bar","Pie","Line","Scatter","Histogram","Boxplot"])
    num_cols=df.select_dtypes(include=['number']).columns.tolist()
    cat_cols=df.select_dtypes(exclude=['number']).columns.tolist()
    #bar chart for both catergorical data and numeric
    if chart_type in "Bar":
        col=st.selectbox("Select column for visualization",df.columns)
        fig,ax=plt.subplots()
        if col in cat_cols:
            vc=df[col].value_counts()
            vc.plot(kind="bar",ax=ax)
            ax.set_ylabel("Count")
            ax.set_xlabel(col)
            ax.set_title(f"Bar Chart : {col}")
        else:
            df[col].plot(kind='bar',ax=ax)
            ax.set_ylabel(col)
            ax.set_xlabel("Index")
            ax.set_title(f"Bar Chart : {col}")
        st.pyplot(fig)
    #pie chart for catergorical data and using bin for numerical data 
    elif chart_type=="Pie":
        col =st.selectbox("Select Column",df.columns)
        fig,ax=plt.subplots()
        if col in cat_cols:
            vc=df[col].value_counts()
            vc.plot(kind='pie',ax=ax,autopct='%1.1f%%')
            ax.set_ylabel("")
            ax.set_title(f"Pie chart: {col}")
        elif col in num_cols:
            bins=st.slider("Select number of bins for numeric pie chart",2,10,5)
            binned_data=pd.cut(df[col],bins=bins)
            vc=binned_data.value_counts()
            vc.plot(kind="pie",ax=ax,autopct='%1.1f%%')
            ax.set_title(f"Pie Chart: {col}")
        else:
            st.error("Invalid column selected for Pie Chart")
            return
        st.pyplot(fig)

    elif chart_type in ["Line","Histogram","Boxplot"]:
        num_cols=df.select_dtypes(include=['number']).columns.tolist()
        if not num_cols:
            st.warning("No numeric columns available for this chart")
            return 
        col=st.selectbox('Select numeric column',num_cols,index=0)
        fig,ax=plt.subplots()
        if chart_type=="Line":
            ax.plot(df[col].reset_index(drop=True))
            ax.set_ylabel(col)
            ax.set_title(f"Line plot :{col}")
        elif chart_type=="Histogram":
            ax.hist(df[col].dropna(),bins=20)
            ax.set_xlabel(col)
            ax.set_ylabel('Frequency')
            ax.set_title(f"Histogram of column :{col}")
        else:
            ax.boxplot(df[col].dropna())
            ax.set_ylabel(col)
            ax.set_title(f"Boxplot:{col}")
        st.pyplot(fig)

    else:
        if len(num_cols)<2:
            st.warning("Need at least two numerice columns for scatter plot")
            return
        col_x=st.selectbox("X axis",num_cols,index=0)
        col_y=st.selectbox("Y axis",num_cols,index=1)
        fig,ax=plt.subplots()
        ax.scatter(df[col_x],df[col_y])
        ax.set_xlabel(col_x)
        ax.set_ylabel(col_y)
        ax.set_title(f"Scatter : {col_x} vs {col_y}")
        st.pyplot(fig)
