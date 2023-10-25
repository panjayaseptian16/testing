import streamlit as st
from streamlit.components.v1 import html


@st.cache_resource
def read_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content

cek_html = read_file("cek.html")

html(cek_html, height=1000)