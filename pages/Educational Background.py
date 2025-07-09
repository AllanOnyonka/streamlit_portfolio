import streamlit as st
import pandas as pd
from utils.layout import load_css, set_background

# --- Page Configuration ---
st.set_page_config(
    page_title="Educational Background | Allan Bisonga",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom styling
set_background("assets/1.jpg")
load_css("styles/style.css")

# --- Page Header ---
st.title("🎓 Educational Background")
st.markdown("---")

# --- Academic Qualifications ---
st.header("📚 Academic Qualifications")

# Create columns for better layout
ed_col1, ed_col2 = st.columns(2)

with ed_col1:
    st.subheader("🏫 Current Education")
    st.markdown("""
    **Bachelor of Science in Computer Science**
    - *University/Institution*: [Your University Name]
    - *Expected Graduation*: [Year]
    - *Current GPA*: [Your GPA]
    - *Relevant Coursework*:
      - Data Structures & Algorithms
      - Database Systems
      - Software Engineering
      - Computer Networks
      - Cybersecurity Fundamentals
    """)

with ed_col2:
    st.subheader("🎯 Specializations")
    st.markdown("""
    **Focus Areas:**
    - Artificial Intelligence & Machine Learning
    - Cybersecurity
    - Full Stack Development
    - Data Science & Analytics
    
    **Minor/Concentration:**
    - Information Security
    - Web Technologies
    """)

st.markdown("---")

# --- Certifications ---
st.header("🏆 Certifications & Training")

cert_col1, cert_col2 = st.columns(2)

with cert_col1:
    st.subheader("🔒 Cybersecurity Certifications")
    certifications = [
        "CompTIA Security+ (In Progress)",
        "Ethical Hacking Fundamentals",
        "Network Security Basics",
        "Python for Cybersecurity"
    ]
    
    for cert in certifications:
        st.markdown(f"- {cert}")

with cert_col2:
    st.subheader("💻 Technical Certifications")
    tech_certs = [
        "AWS Cloud Practitioner (Planned)",
        "Google Cloud Platform Fundamentals",
        "Docker & Kubernetes Basics",
        "Git & GitHub Professional"
    ]
    
    for cert in tech_certs:
        st.markdown(f"- {cert}")

st.markdown("---")

# --- Online Learning ---
st.header("🌐 Online Learning & MOOCs")

learning_platforms = {
    "Platform": [
        "Coursera",
        "edX",
        "Udemy",
        "Codecademy",
        "freeCodeCamp"
    ],
    "Courses Completed": [5, 3, 8, 4, 6],
    "Focus Area": [
        "AI/ML & Data Science",
        "Computer Science Theory",
        "Full Stack Development",
        "Python Programming",
        "Web Development"
    ],
    "Certification": ["Yes", "Yes", "Yes", "Yes", "No"]
}

learning_df = pd.DataFrame(learning_platforms)
st.dataframe(learning_df, use_container_width=True)

# --- Academic Projects ---
st.header("🔬 Academic Projects")

project_col1, project_col2 = st.columns(2)

with project_col1:
    st.subheader("🧮 Major Projects")
    st.markdown("""
    **1. Student Management System**
    - *Course*: Database Systems
    - *Technologies*: MySQL, PHP, HTML/CSS
    - *Description*: Full CRUD application for managing student records
    
    **2. Network Security Scanner**
    - *Course*: Cybersecurity
    - *Technologies*: Python, Nmap, Wireshark
    - *Description*: Automated network vulnerability assessment tool
    """)

with project_col2:
    st.subheader("🎯 Research Projects")
    st.markdown("""
    **1. Machine Learning for Fraud Detection**
    - *Type*: Independent Study
    - *Technologies*: Python, Scikit-learn, Pandas
    - *Status*: Completed
    
    **2. Blockchain in Supply Chain**
    - *Type*: Group Research
    - *Technologies*: Ethereum, Solidity, Web3
    - *Status*: In Progress
    """)

st.markdown("---")

# --- Skills Development Timeline ---
st.header("📈 Skills Development Timeline")

timeline_data = {
    "Year": ["2022", "2023", "2023", "2024", "2024", "2025"],
    "Milestone": [
        "Started Computer Science",
        "First Python Program",
        "Web Development Basics",
        "Advanced Programming",
        "Cybersecurity Focus",
        "AI/ML Specialization"
    ],
    "Key Learning": [
        "Programming Fundamentals",
        "Object-Oriented Programming",
        "Frontend & Backend",
        "Data Structures & Algorithms",
        "Security Principles",
        "Machine Learning Models"
    ]
}

timeline_df = pd.DataFrame(timeline_data)
st.dataframe(timeline_df, use_container_width=True)

# --- Academic Achievements ---
st.header("🏅 Academic Achievements")

achievements_col1, achievements_col2 = st.columns(2)

with achievements_col1:
    st.subheader("🎖️ Awards & Recognition")
    st.markdown("""
    - Dean's List (Multiple Semesters)
    - Outstanding Programming Project Award
    - Cybersecurity Competition Participant
    - Hackathon Top 10 Finalist
    """)

with achievements_col2:
    st.subheader("📊 Academic Performance")
    
    # GPA visualization
    semesters = ["Sem 1", "Sem 2", "Sem 3", "Sem 4", "Sem 5", "Sem 6"]
    gpa_scores = [3.2, 3.5, 3.7, 3.8, 3.9, 3.95]
    
    gpa_df = pd.DataFrame({
        "Semester": semesters,
        "GPA": gpa_scores
    })
    
    st.line_chart(gpa_df.set_index("Semester"))

st.markdown("---")

# --- Extracurricular Activities ---
st.header("🎪 Extracurricular Activities")

extra_col1, extra_col2 = st.columns(2)

with extra_col1:
    st.subheader("🤝 Student Organizations")
    st.markdown("""
    - **Computer Science Society** - Member
    - **Cybersecurity Club** - Secretary
    - **Programming Club** - Treasurer
    - **Tech Entrepreneurship Society** - Member
    """)

with extra_col2:
    st.subheader("🌟 Leadership Roles")
    st.markdown("""
    - **Peer Tutor** - Programming Courses
    - **Event Organizer** - Tech Meetups
    - **Mentor** - First-year students
    - **Workshop Facilitator** - Coding workshops
    """)

st.markdown("---")

# --- Future Learning Goals ---
st.header("🎯 Future Learning Goals")

st.markdown("""
### 📅 Short-term Goals (Next 6 months)
- Complete AWS Cloud Practitioner certification
- Advanced Python programming certification
- Participate in more cybersecurity competitions
- Contribute to open-source projects

### 🚀 Long-term Goals (Next 2 years)
- Master's degree in Cybersecurity or AI
- Industry certifications (CISSP, CEH)
- Research publication in AI/Security
- Leadership role in tech community

### 💡 Continuous Learning Philosophy
I believe in lifelong learning and staying updated with the latest technologies. My approach combines:
- Formal education foundation
- Hands-on project experience
- Industry certifications
- Community involvement
""")

# --- Contact for Academic Collaboration ---
st.header("🤝 Academic Collaboration")

st.markdown("""
I'm always interested in academic collaborations, research projects, and knowledge sharing. 
Feel free to reach out if you're working on similar projects or research areas!

**Research Interests:**
- Machine Learning Applications in Cybersecurity
- Blockchain Technology
- Web Application Security
- Data Science for Social Good
""")

# Footer
st.markdown("---")
st.markdown("*🎓 Education is the foundation of innovation*")
