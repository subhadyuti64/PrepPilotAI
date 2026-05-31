import streamlit as st
from utils.styles import load_css

load_css()

# =====================================
# SESSION DATA
# =====================================

analysis = st.session_state.get("analysis", {})

interview_history = st.session_state.get(
    "interview_history",
    []
)

skills_count = len(
    analysis.get("skills", [])
)

projects_count = len(
    analysis.get("projects", [])
)

resume_status = (
    "✅ Uploaded"
    if analysis
    else "❌ Not Uploaded"
)

avg_score = 0

if interview_history:

    avg_score = round(
        sum(
            item["score"]
            for item in interview_history
        ) / len(interview_history),
        1
    )

# =====================================
# HERO SECTION
# =====================================
st.markdown("""
<div class='hero-title' style='margin-top:60px;'>
🚀 PrepPilot AI
</div>

<div class='hero-subtitle'>
Your Personal AI Interview Coach
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================
# METRICS
# =====================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "📄 Resume",
        resume_status
    )

with col2:

    st.metric(
        "🛠 Skills",
        skills_count
    )

with col3:

    st.metric(
        "🚀 Projects",
        projects_count
    )

with col4:

    st.metric(
        "🎯 Avg Score",
        avg_score
    )

st.divider()

# =====================================
# QUICK SUMMARY
# =====================================

st.subheader("📊 Quick Summary")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class='card'>
    <h3>🎯 Interview Progress</h3>

    Track your interview performance,
    strengths, weaknesses and growth
    over time.

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class='card'>
    <h3>📈 AI-Powered Insights</h3>

    Analyze your resume,
    generate questions,
    practice interviews,
    and receive detailed feedback.

    </div>
    """, unsafe_allow_html=True)

st.divider()

# =====================================
# FEATURES
# =====================================

st.subheader("✨ Platform Features")

c1, c2 = st.columns(2)

with c1:

    st.markdown("""
    <div class='card'>
    <h3>📄 Resume Analysis</h3>

    • Extract skills

    • Analyze projects

    • Identify strengths

    • Recommend job roles

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    <h3>❓ Question Generator</h3>

    • Domain-specific questions

    • Resume-aware generation

    • Beginner → Advanced levels

    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown("""
    <div class='card'>
    <h3>💬 Resume Chat</h3>

    • Ask questions about your resume

    • Powered by RAG

    • Instant responses

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    <h3>🎤 Mock Interview</h3>

    • AI interviewer

    • Answer evaluation

    • Detailed scorecards

    • Follow-up questions

    </div>
    """, unsafe_allow_html=True)

# =====================================
# FOOTER
# =====================================

st.divider()

st.caption(
    "Built with FastAPI • LangChain • OpenAI • FAISS • Streamlit"
)