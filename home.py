import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
            <h2 style="text-align: center;color:#1F4172;">Air Quality Realtime Monitoring</h2>
            """,unsafe_allow_html=True)
# Baca konten HTML dari berkas interactive_aqi_widget.html
with open("widget.html", "r") as file:
    widget_html = file.read()

with open("map.html", "r") as file:
    map_html = file.read()

with st.container():
    # Tampilkan widget HTML dalam aplikasi Streamlit
    html(widget_html, width=800, height=210)
    # Tambahkan teks caption
    #st.caption("Air Quality Index scale as defined by the US-EPA 2016 standard. Check details in [here](https://aqicn.org/scale/)")
    st.markdown(
    "<div style='margin-top: -20px; text-align: left; font-size: 14px; color:#1F4172;'>Air Quality Index (AQI) scale as defined by the US-EPA 2016 standard. Check details in <a href='https://aqicn.org/scale/'>here</a></div>",
    unsafe_allow_html=True)
    st.markdown("""
            <h3 style="text-align: center; color:#1F4172; margin-bottom: -50px;">Map AQI Jakarta</h3>
            """,unsafe_allow_html=True)
    col1, col2 = st.columns([2,1])
    html(map_html, width=900, height=750)