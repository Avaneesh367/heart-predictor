import streamlit as st
import streamlit.components.v1 as components

# Tell Streamlit to use the whole screen
st.set_page_config(layout="wide")

# Read your html file
with open("prediction.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Show your page
components.html(html_code, height=1200, scrolling=True)