import streamlit as st
import pandas as pd
from utils.layout import load_css, set_background

# --- Page Configuration ---
st.set_page_config(
    page_title="Projects | Allan Bisonga",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom styling
set_background("assets/1.jpg")
load_css("styles/style.css")

# --- Page Header ---
st.title("🛠️ My Projects Portfolio")
st.markdown("---")

# --- Featured Projects ---
st.header("🌟 Featured Projects")

# Create columns for project cards
col1, col2 = st.columns(2)

with col1:
    st.subheader("🤖 AI-Powered Chatbot")
    st.markdown("""
    **Description:** A conversational AI chatbot built with Python and natural language processing.
    
    **Technologies:** Python, TensorFlow, NLTK, Streamlit
    
    **Features:**
    - Natural language understanding
    - Context-aware responses
    - Web interface with Streamlit
    - Sentiment analysis
    """)
    
    if st.button("View Chatbot Demo", key="chatbot"):
        st.info("🚀 Demo coming soon!")

with col2:
    st.subheader("📊 Data Analytics Dashboard")
    st.markdown("""
    **Description:** Interactive dashboard for analyzing business metrics and KPIs.
    
    **Technologies:** Python, Pandas, Plotly, Streamlit
    
    **Features:**
    - Real-time data visualization
    - Interactive charts and graphs
    - Export functionality
    - Responsive design
    """)
    
    if st.button("View Dashboard Demo", key="dashboard"):
        st.info("📈 Demo coming soon!")

st.markdown("---")

# --- Current Projects ---
st.header("🚧 Current Projects")

projects_data = {
    "Project": [
        "Cybersecurity Monitoring Tool",
        "Personal Finance Tracker",
        "E-commerce API",
        "Machine Learning Pipeline"
    ],
    "Status": ["In Progress", "Planning", "Development", "Testing"],
    "Technology": ["Python, Go", "React, Node.js", "Go, PostgreSQL", "Python, Docker"],
    "Completion": [75, 25, 60, 90]
}

df = pd.DataFrame(projects_data)

# Display projects table
st.dataframe(df, use_container_width=True)

# Progress visualization
st.subheader("📈 Project Progress")
for idx, row in df.iterrows():
    st.markdown(f"**{row['Project']}**")
    st.progress(row['Completion'] / 100)
    st.markdown(f"*Status: {row['Status']} | Tech: {row['Technology']}*")
    st.markdown("")

st.markdown("---")

# --- GitHub Repositories ---
st.header("📁 GitHub Repositories")

repo_col1, repo_col2, repo_col3 = st.columns(3)

with repo_col1:
    st.markdown("""
    ### 🐍 Python Projects
    - **Web Scraper**: Data extraction tools
    - **Automation Scripts**: System automation
    - **Data Analysis**: Business intelligence
    """)

with repo_col2:
    st.markdown("""
    ### 🌐 Web Development
    - **Portfolio Website**: Personal showcase
    - **API Projects**: RESTful services
    - **Frontend Apps**: Interactive UIs
    """)

with repo_col3:
    st.markdown("""
    ### 🔧 System Tools
    - **CLI Applications**: Command-line tools
    - **DevOps Scripts**: Deployment automation
    - **Security Tools**: Cybersecurity utilities
    """)

# GitHub link
st.markdown("---")
st.markdown("### 🔗 [Visit My GitHub Profile](https://github.com/onyonka)")

# --- Skills Used in Projects ---
st.header("💼 Technical Skills Demonstrated")

skills_col1, skills_col2 = st.columns(2)

with skills_col1:
    st.markdown("""
    **Programming Languages:**
    - Python (Flask, Django, FastAPI)
    - JavaScript (React, Node.js)
    - Go (Gin, Echo)
    - C/C++ (System programming)
    """)

with skills_col2:
    st.markdown("""
    **Tools & Technologies:**
    - Docker & Kubernetes
    - PostgreSQL & MongoDB
    - Git & GitHub Actions
    - Linux & Bash scripting
    """)

# --- Project Timeline ---
st.header("⏰ Project Timeline")

timeline_data = {
    "Year": ["2023", "2023", "2024", "2024", "2025"],
    "Project": [
        "First Python Script",
        "Web Scraping Tool",
        "Streamlit Dashboard",
        "AI Chatbot",
        "Current Portfolio"
    ],
    "Impact": [
        "Learning Foundation",
        "Automation Success",
        "Data Visualization",
        "AI Integration",
        "Professional Showcase"
    ]
}

timeline_df = pd.DataFrame(timeline_data)
st.dataframe(timeline_df, use_container_width=True)

# --- Contact for Collaborations ---
st.header("🤝 Let's Collaborate!")

st.markdown("""
I'm always open to interesting projects and collaborations. Whether you have an idea for a new project or want to contribute to existing ones, let's connect!

**Areas of Interest:**
- AI/ML Projects
- Web Development
- Cybersecurity Tools
- Data Analytics
- Open Source Contributions
""")

# Contact form
with st.form("collaboration_form"):
    st.subheader("💬 Get in Touch")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    project_idea = st.text_area("Project Idea or Collaboration Proposal")
    
    if st.form_submit_button("Send Message"):
        if name and email and project_idea:
            st.success("Thank you for your message! I'll get back to you soon.")
            st.balloons()
        else:
            st.error("Please fill in all fields.")

# Footer
st.markdown("---")
st.markdown("*💡 More projects coming soon! Stay tuned for updates.*")
