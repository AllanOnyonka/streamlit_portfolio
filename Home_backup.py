import streamlit as st
import time
import pandas as pd
from utils.layout import load_css
from utils.layout import set_background
from utils.layout import typewriter



set_background("assets/1.jpg")
load_css("styles/style.css")

learning = [
    "📚 Rust for High-Performance Systems",
    "📚 React for Modern Frontend Development",
    "📚 Docker & Kubernetes for Deployment",
    "📚 Advanced C and Pointer Arithmetic",
    "📚 Transformer-based NLP Models",
]

# -- Buttons for Showcases --





# --- Page Configuration ---
st.set_page_config(page_title="Allan Bisonga | Tech Journal", layout="wide")

# --- Typewriter Intro Animation ---
intro_text = "Hi, I'm Allan — welcome to my tech journal."
placeholder = st.empty()
full_intro = ""
for char in intro_text:
    full_intro += char
    placeholder.markdown(f"# {full_intro}")
    time.sleep(0.05) # Adjust typing speed

st.markdown("", unsafe_allow_html=True) # Clear the placeholder after animation

# --- Header Section ---
st.subheader("Aspiring Software Engineer | Full Stack Dev | AI & Cyber Enthusiast")
st.write("Building intelligent systems for Africa's future 🚀")

st.divider()

# --- Skills Section (Original Toolbox) ---
st.header("My Toolbox 🧰")
skills = ["Python", "Golang", "JavaScript", "C", "Linux", "Streamlit", "Cybersecurity", "AI", "DevOps"]
skill_tags_html = "".join([f'<span class="skill-tag">{skill}</span>' for skill in skills])
st.markdown(f"<div>{skill_tags_html}</div>", unsafe_allow_html=True)

st.divider()

# --- Detailed Skills Section for Recruiters ---
st.header("A Deeper Look for Recruiters")

# Button to trigger the detailed view
if st.button("Click to Reveal Skill Details ✨"):
    st.session_state.reveal_details = True

# This part is only shown after the button is clicked
if st.session_state.get('reveal_details', False):
    # Using tabs to organize the skills neatly
    lang_tab, framework_tab, tools_tab, soft_skills_tab = st.tabs([
        "Programming Languages",
        "Frameworks & Libraries",
        "Tools & Platforms",
        "Soft Skills"
    ])

    # Function to create the typing effect for skill details
    def type_out_text(text_list):
        placeholder_detail = st.empty()
        full_text = ""
        for item in text_list:
            full_text += item + "\n"
            placeholder_detail.markdown(full_text)
            time.sleep(0.03) # Adjust speed of typing here

    with lang_tab:
        type_out_text([
            "- **Python:** (3+ years) Proficient in using Python for data science (Pandas, NumPy), web scraping, automation scripts, and building backend services.",
            "- **JavaScript:** (2+ years) Experienced in frontend development for interactive web applications and using it for building custom tooling.",
            "- **Go (Golang):** (1+ year) Used for developing high-performance, concurrent backend systems and command-line tools.",
            "- **C/C++:** (1 year) Solid foundation in low-level programming, memory management, and performance optimization from academic projects.",
            "- **Bash:** (4+ years) My go-to for scripting, automating workflows, and managing Linux environments."
        ])

    with framework_tab:
        type_out_text([
            "- **Streamlit:** (1+ year) Extensive experience in building interactive web applications and dashboards, including this very portfolio.",
            "- **Pandas & NumPy:** (3+ years) Core libraries in my data science toolkit for data manipulation, analysis, and numerical computation.",
            "- **LSTM (Keras/TensorFlow):** (1 year) Experience in implementing Long Short-Term Memory networks for time-series analysis and NLP tasks in personal AI projects."
        ])

    with tools_tab:
        type_out_text([
            "- **Git & GitHub:** (4+ years) Daily driver for version control, collaboration, and CI/CD workflows.",
            "- **Linux:** (4+ years) My primary operating system for development. Comfortable with system administration and the command line.",
            "- **Docker:** (2+ years) Used for containerizing applications to ensure consistent development and deployment environments.",
            "- **WSL & Kali Linux:** (2+ years) Experience using WSL for a seamless Linux environment on Windows and Kali Linux for cybersecurity exercises and projects.",
            "- **Notion & Obsidian:** (3+ years) Used for knowledge management, project planning, and maintaining a personal knowledge base."
        ])

    with soft_skills_tab:
        type_out_text([
            "- **Problem Solving:** Methodical approach to breaking down complex problems and developing effective solutions.",
            "- **Collaboration:** Experience working in team environments using agile methodologies and tools like Git.",
            "- **Communication:** Able to clearly articulate technical concepts to both technical and non-technical audiences.",
            "- **Continuous Learning:** Passionate about staying up-to-date with the latest technologies and industry best practices."
        ])

st.divider()

# --- Navigation/CTA Section ---
st.header("Connect & Explore")

# Create columns for a cleaner layout
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<a href="/Projects" target="_self" class="button-link">🛠️ View My Projects</a>', unsafe_allow_html=True)

with col2:
    pass




with col3:
    # You should place your resume in the 'assets' folder for this link to work
    pass
with st.expander("📬 Contact Me"):
        st.markdown("""
               - **Email:** [bisonga@gmail.com](mailto:bisonga@gmail.com)  
               
               - **Phone:** +254 724 015278
           """)
if st.button("Technologies"):
    typewriter(learning)





