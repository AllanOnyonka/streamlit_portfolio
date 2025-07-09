import streamlit as st
import time
import pandas as pd
from utils.layout import set_background
set_background("assets/1.jpg")



# --- Page Title ---
st.title("Streamlit Components Showcase")
st.write("This page demonstrates various Streamlit widgets and features I can implement.")

st.divider()

# Basic header information
st.write("Allan")
st.header("Desire")
st.caption("AWS")

# Show source code
st.code("""
st.write("Allan")
st.header("Desire")
st.caption("AWS")
""")

# st.echo block
with st.echo():
    st.write("Hello")

# Editable dataframe
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/data.csv")
edited_df = st.data_editor(df)
st.dataframe(edited_df)
st.write("Editable dataframe")

# Metric
st.metric("Temperature", 16, -22)

# Submit button
if st.button("Submit"):
    st.write("The form has been submitted")

# User feedback (slider replaces st.feedback)
user_feedback = st.slider("Rate the app (1–5)", 1, 5)
if user_feedback >= 4:
    st.write("Thanks for the great feedback!")
else:
    st.write("Thanks for your feedback – we'll improve!")

st.write("You rated:", user_feedback)

# Terms checkbox
terms_conditions = st.checkbox("I agree to the terms and conditions")
if terms_conditions:
    st.write("You are welcome")

# Dark mode toggle (visual only)
dark_mode = st.toggle("Dark Mode")
if dark_mode:
    st.markdown(
        "<style>body { background-color: #0e1117; color: white; }</style>",
        unsafe_allow_html=True
    )

# Gender selection
gender = st.radio("Gender", ("Male", "Female"))
if gender == "Male":
    st.write("Uko Draft Baba")
elif gender == "Female":
    st.write("Medic!!!")

# Fixed selectbox for football teams
team = st.selectbox("Select Your Favourite Team", [
    "Manchester City", "Liverpool", "Arsenal", "Chelsea", "Manchester United"
])
if team == "Manchester United":
    st.write("Glory Glory Manchester United")
elif team == "Liverpool":
    st.write("You'll never walk alone")
elif team == "Arsenal":
    st.write("Lom")
elif team == "Manchester City":
    st.write("Champions again!")
elif team == "Chelsea":
    st.write("Blue is the color!")


age = st.number_input("Age")
kcpe = st.number_input("KCPE")
date = st.date_input("Date")




# Typewriter effect demo
st.title("Typewriter effect")
st.header("Auto type")
st.write("------------------------------------------------")



code = '''  
import streamlit as st
import pandas as pd
import time

st.write("Allan")
st.header("Desire")
st.caption("AWS")

with st.echo():
    st.write("Hello")

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/data.csv")
edited_df = st.data_editor(df)
st.dataframe(edited_df)

st.metric("Temperature", 16, -22)

if st.button("Submit"):
    st.write("The form has been submitted")

user_feedback = st.slider("Rate the app (1–5)", 1, 5)
if user_feedback >= 4:
    st.write("Thanks for the great feedback!")
else:
    st.write("Thanks for your feedback – we'll improve!")
'''

placeholder = st.empty()
typed = ""

for char in code:
    typed += char
    placeholder.code(typed, language='python')
    time.sleep(0.01)  # adjust typing speed


uploaded =st.file_uploader("Upload File")

# selfie = st.camera_input("Take a photo")