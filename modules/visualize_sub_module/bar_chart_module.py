import seaborn as sns
import streamlit as st
from modules.download_module import download_chart

def plot_bar_chart(df, cat_cols,col):
    #col = st.selectbox("Select column for visualization", df.columns)
    if col in cat_cols:
        vc=df[col].value_counts().reset_index()
        vc.columns=[col,"Count"]
        fig=sns.catplot(data=vc,x=col,y="Count",kind="bar",palette="viridis",height=5,aspect=1.5)
        fig.set_axis_labels(col,"Count")
        fig.set_titles(f"Bar chart : {col}")
    else:
        fig=sns.catplot(x=df.index,y=df[col],kind='bar',palette='coolwarm',height=5,aspect=1.5)
        fig.set_axis_labels("Index",col)
        fig.set_titles(f"Bar Chart : {col}")

    st.pyplot(fig)
    download_chart(fig,f"Bar_Chart_{col}.png")