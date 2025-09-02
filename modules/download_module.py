import streamlit as st
import io

def download_chart(fig,filename="chart.png"):
    if fig is None:
        st.warning("No chart available to download")
        return 

    buf=io.BytesIO()
    try:
        fig.savefig(buf,format='png',bbox_inches='tight')
    except Exception as e:
        st.error(f"Failed to generate chart: {e}")
        return 
    
    #download button logic 
    clicked=st.download_button(
            label="Download chart as PNG",
            data=buf.getvalue(),
            file_name=filename,
            mime="image/png"
        )

    if clicked:
        st.session_state[f"download_clicked_{filename}"]=True
    
    if st.session_state.get(f"download_clicked_{filename}",False):
        #check the data is actaully available
        if buf.getvalue():
            st.success("Image Downloaded Sucessfully")
        else:
            st.error("Failed to Download Image")