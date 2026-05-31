import streamlit as st
from utils.api import generate_questions

st.set_page_config(
    page_title="Question Generator",
    page_icon="❓",
    layout="wide"
)

st.title("❓ Interview Question Generator")

st.caption(
    "Generate personalized interview questions from your uploaded resume"
)

# =====================================
# CHECK RESUME
# =====================================

if "session_id" not in st.session_state:

    st.warning(
        "⚠ Please upload a resume first from the Resume Analysis page."
    )

    st.stop()

# =====================================
# DOMAIN SELECTION
# =====================================

domains = [
    "Python",
    "Machine Learning",
    "Data Structures",
    "Algorithms",
    "DBMS",
    "Operating Systems",
    "Computer Networks",
    "OOP",
    "SQL",
    "FastAPI"
]

domain = st.selectbox(
    "Select Domain",
    domains
)

# =====================================
# GENERATE QUESTIONS
# =====================================

if st.button(
    "🚀 Generate Questions",
    use_container_width=True
):

    with st.spinner(
        "Generating personalized questions..."
    ):

        try:

            response = generate_questions(
                domain,
                st.session_state[
                    "session_id"
                ]
            )

            st.session_state[
                "generated_questions"
            ] = response[
                "questions"
            ]

        except Exception as e:

            st.error(
                str(e)
            )

# =====================================
# DISPLAY QUESTIONS
# =====================================

if "generated_questions" in st.session_state:

    st.divider()

    st.subheader(
        f"📚 Questions for {domain}"
    )

    questions = st.session_state[
        "generated_questions"
    ]

    st.markdown(
        f"""
<div style="
padding:20px;
border-radius:12px;
background-color:#1E293B;
border:1px solid #334155;
">
<pre style="
white-space: pre-wrap;
font-size:15px;
">
{questions}
</pre>
</div>
""",
        unsafe_allow_html=True
    )

# =====================================
# CLEAR
# =====================================

if st.button(
    "🗑 Clear Questions"
):

    if "generated_questions" in st.session_state:

        del st.session_state[
            "generated_questions"
        ]

    st.rerun()