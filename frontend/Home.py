import streamlit as st

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="PrepPilot AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 3.5rem;
    font-weight: bold;
    color: #4F46E5;
}

.sub-title {
    text-align: center;
    font-size: 1.2rem;
    color: #94A3B8;
    margin-bottom: 30px;
}

.feature-card {
    background-color: #1E293B;
    padding: 20px;
    border-radius: 12px;
    border-left: 5px solid #4F46E5;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("🚀 PrepPilot AI")

st.sidebar.success(
    "Navigate using the pages above."
)

# st.sidebar.markdown("---")

# st.sidebar.markdown("""
# ### Available Modules

# 🏠 Dashboard

# 📄 Resume Analysis

# 💬 Resume Chat

# ❓ Question Generator

# 🎤 Mock Interview

# 📊 Performance Report
# """)

# =====================================
# HEADER
# =====================================

st.markdown(
    "<div class='main-title'>🚀 PrepPilot AI</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>AI-Powered Interview Preparation Assistant</div>",
    unsafe_allow_html=True
)

# =====================================
# HERO SECTION
# =====================================

col1, col2 = st.columns([2, 1])

with col1:

    st.markdown("""
### Welcome to PrepPilot

PrepPilot helps you prepare for technical interviews using AI.

Upload your resume and get:

- 📄 Resume Analysis
- 💬 Resume-based Q&A (RAG)
- ❓ Personalized Interview Questions
- 🎤 Mock Interviews
- 📊 Detailed Performance Evaluation
""")

st.markdown("---")

# =====================================
# FEATURE OVERVIEW
# =====================================

st.header("✨ Features")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
<div class="feature-card">

### 📄 Resume Analysis

Extract:

- Skills
- Projects
- Strengths
- Recommended Roles

</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div class="feature-card">

### ❓ Question Generator

Generate personalized interview questions based on:

- Resume
- Skills
- Selected Domain

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="feature-card">

### 💬 Resume Chat

Ask questions like:

- What skills are mentioned?
- What projects have I worked on?
- What technologies do I know?

</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div class="feature-card">

### 🎤 Mock Interview

- Generate interview questions
- Submit answers
- Receive scores
- Get improvement suggestions

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =====================================
# GET STARTED
# =====================================

st.success(
    "👈 Use the sidebar to navigate through PrepPilot's modules."
)

st.caption(
    "Built with FastAPI, LangChain, OpenAI, FAISS and Streamlit."
)