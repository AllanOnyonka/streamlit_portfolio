import streamlit as st
import time
import pandas as pd
from utils.layout import load_css, set_background, typewriter

# --- Page Configuration ---
st.set_page_config(
    page_title="Allan Bisonga | Tech Journal", 
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/onyonka/streamlit_portfolio',
        'Report a bug': "https://github.com/onyonka/streamlit_portfolio/issues",
        'About': "# Allan Bisonga's Portfolio\nBuilt with Streamlit"
    }
)

# Load custom styling
set_background("assets/1.jpg")
load_css("styles/style.css")

# Technologies I'm learning
learning = [
    "Rust for High-Performance Systems",
    "React for Modern Frontend Development", 
    "Docker & Kubernetes for Deployment",
    "Advanced C and Pointer Arithmetic",
    "Transformer-based NLP Models",
]

# --- Optimized Typewriter Intro Animation ---
if 'intro_complete' not in st.session_state:
    st.session_state.intro_complete = False

if not st.session_state.intro_complete:
    intro_text = "Hi, I'm Allan - welcome to my tech journal."
    placeholder = st.empty()
    full_intro = ""
    for char in intro_text:
        full_intro += char
        placeholder.markdown(f"# {full_intro}")
        time.sleep(0.03)  # Faster typing speed
    st.session_state.intro_complete = True
else:
    st.markdown("# Hi, I'm Allan - welcome to my tech journal.")

# --- Header Section ---
st.subheader("Aspiring Software Engineer | Full Stack Dev | AI & Cyber Enthusiast")
st.write("Building intelligent systems for Africa's future")

st.divider()

# --- Skills Section (Improved Toolbox) ---
st.header("My Toolbox")

# Organize skills by category
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Programming Languages**")
    prog_langs = ["Python", "Golang", "JavaScript", "C"]
    for lang in prog_langs:
        st.markdown(f"- {lang}")

with col2:
    st.markdown("**Technologies & Tools**")
    tools = ["Linux", "Docker", "Git", "Streamlit"]
    for tool in tools:
        st.markdown(f"- {tool}")

with col3:
    st.markdown("**Focus Areas**")
    focus = ["Cybersecurity", "AI/ML", "DevOps", "Web Development"]
    for area in focus:
        st.markdown(f"- {area}")

# Skills as tags (keeping the visual appeal)
skills = ["Python", "Golang", "JavaScript", "C", "Linux", "Streamlit", "Cybersecurity", "AI", "DevOps"]
skill_tags_html = "".join([f'<span class="skill-tag">{skill}</span>' for skill in skills])
st.markdown(f"<div>{skill_tags_html}</div>", unsafe_allow_html=True)

st.divider()

# --- Detailed Skills Section for Recruiters ---
st.header("Professional Skills Overview")

# Improved button to trigger the detailed view
if st.button("View Detailed Skills Assessment", type="primary"):
    st.session_state.reveal_details = True

# This part is only shown after the button is clicked
if st.session_state.get('reveal_details', False):
    # Using expanders for better organization
    with st.expander("Programming Languages", expanded=True):
        skills_data = {
            "Language": ["Python", "JavaScript", "Go (Golang)", "C/C++", "Bash"],
            "Experience": ["3+ years", "2+ years", "1+ year", "1 year", "4+ years"],
            "Proficiency": ["Advanced", "Intermediate", "Intermediate", "Beginner", "Advanced"],
            "Key Applications": [
                "Data Science, Backend, Automation",
                "Frontend Development, Web Apps",
                "Backend Systems, CLI Tools",
                "System Programming, Algorithms",
                "System Administration, Scripting"
            ]
        }
        st.dataframe(pd.DataFrame(skills_data), use_container_width=True)
    
    with st.expander("Frameworks & Technologies"):
        frameworks = {
            "Framework/Tool": ["Streamlit", "Pandas & NumPy", "LSTM/TensorFlow", "Docker", "Git & GitHub"],
            "Experience": ["1+ year", "3+ years", "1 year", "2+ years", "4+ years"],
            "Use Cases": [
                "Interactive Web Apps, Dashboards",
                "Data Analysis, Numerical Computing",
                "Time-series Analysis, NLP",
                "Containerization, DevOps",
                "Version Control, CI/CD"
            ]
        }
        st.dataframe(pd.DataFrame(frameworks), use_container_width=True)
    
    with st.expander("Soft Skills & Methodologies"):
        soft_skills = [
            "**Problem Solving:** Methodical approach to complex challenges",
            "**Team Collaboration:** Agile methodologies and version control",
            "**Communication:** Technical concepts to diverse audiences",
            "**Continuous Learning:** Staying current with tech trends",
            "**Project Management:** Planning and executing technical projects"
        ]
        for skill in soft_skills:
            st.markdown(skill)

st.divider()

# --- Current Learning Section ---
st.header("Currently Learning")
col1, col2 = st.columns(2)

with col1:
    if st.button("Show Learning Path"):
        typewriter(learning)

with col2:
    # Progress indicators
    st.markdown("**Learning Progress:**")
    progress_data = {
        "Technology": ["Rust", "React", "Docker/K8s", "Advanced C", "NLP Models"],
        "Progress": [30, 45, 60, 25, 40]
    }
    for tech, progress in zip(progress_data["Technology"], progress_data["Progress"]):
        st.progress(progress / 100, text=f"{tech}: {progress}%")

st.divider()

# --- Navigation/CTA Section ---
st.header("Connect & Explore")

# Create columns for better layout
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<a href="/Projects" target="_self" class="button-link">View My Projects</a>', unsafe_allow_html=True)

with col2:
    st.markdown('<a href="/Streamlit_Demo" target="_self" class="button-link">See Streamlit Demo</a>', unsafe_allow_html=True)

with col3:
    st.markdown('<a href="/Educational_Background" target="_self" class="button-link">Educational Background</a>', unsafe_allow_html=True)

# Contact section
with st.expander("Contact Information"):
    contact_col1, contact_col2 = st.columns(2)
    
    with contact_col1:
        st.markdown("""
        **Professional Contact:**
        - **Email:** [bisonga@gmail.com](mailto:bisonga@gmail.com)
        - **Phone:** +254 724 015278
        """)
    
    with contact_col2:
        st.markdown("""
        **Social & Professional:**
        - **LinkedIn:** [Connect with me](https://linkedin.com/in/allan-bisonga)
        - **GitHub:** [View my repositories](https://github.com/onyonka)
        """)

# Footer
st.markdown("---")
st.markdown("*Built with Streamlit | 2025 Allan Bisonga*")
