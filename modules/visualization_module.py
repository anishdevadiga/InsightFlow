import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def visualize_data(df):
    st.subheader("Data Visualization")
    chart_type=st.selectbox("Select chart Type",["Bar","Pie","Line","Scatter","Histogram","Boxplot"])

    if chart_type in ["Bar","Pie"]:
        col=st.selectbox("Select column (categorical recommend)",df.columns)
        vc=df[col].value_counts()
        fig,ax=plt.subplots()
        if chart_type == "Bar":
            vc.plot(kind="bar",ax=ax)
            ax.set_ylabel("count")
            ax.set_xlabel(col)
            ax.set_title(f"Bar chart : {col}")
        else:
            vc.plot(kind="pie",ax=ax,autopct='%1.1f%%')
            ax.set_ylabel("")
            ax.set_title(f"Pie chart : {col}")
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
        num_cols=df.select_dtypes(include=['number']).columns.tolist()
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
