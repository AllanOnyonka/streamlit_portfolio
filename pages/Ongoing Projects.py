import streamlit as st
import time
import pandas as pd
from utils.layout import load_css
from utils.layout import set_background
set_background("assets/1.jpg")

load_css("styles/style.css")

# --- Page Content ---
st.title("Ongoing Projects")

st.header("Project Alpha: AI-Powered Chatbot")
st.markdown("__*Status: In Development*__")
st.write("""
Developing a context-aware chatbot using Python, TensorFlow, and natural language processing techniques. 
This project aims to provide intelligent customer support for e-commerce platforms.
""")
st.markdown("--- ")

st.header("Project Beta: Portfolio Website")
st.markdown("__*Status: Live*__")
st.write("""
This very website! Built with Streamlit and Python to showcase my skills and projects. 
I'm continuously improving it with new features and a refined design.
""")
