import streamlit as st
import time
import pandas as pd
from utils.layout import set_background
set_background("assets/1.jpg")



# --- Page Content ---
st.title("References")

st.info("References are available upon request.")

st.write("Please feel free to reach out to me for a list of professional and academic references.")

st.markdown('<a href="mailto:allanbisonga@example.com" class="button-link">Request References</a>', unsafe_allow_html=True)
