import streamlit as st
import matplotlib.pylot as plt
import io

def donwload_chart(fig,filename="chart.png"):
    if fig is None:
        st.warning("No chart available to download")
        return 
    
    buf=io.BytesIO()
    fig.savefig(buf,format='png',bbox_inches='tight')
    alert=st.download_button(
        label="Download chart as PNG",
        data=buf.getvalue(),
        file_name=filename,
        mime="image/png"
    )

    if alert:
        st.sucess("Image Downloaded Successfully")
    else:
        st.error("Failed to Download Image")