import streamlit as st
from utils.api import (
    start_interview,
    evaluate_answer
)

st.set_page_config(
    page_title="Mock Interview",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 AI Mock Interview")

st.markdown(
    """
Practice interviews with AI and receive detailed feedback.
"""
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
# SESSION STATE
# =====================================

if "current_question" not in st.session_state:
    st.session_state.current_question = None

if "evaluation_result" not in st.session_state:
    st.session_state.evaluation_result = None

if "interview_history" not in st.session_state:
    st.session_state.interview_history = []

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
    "Select Interview Domain",
    domains
)

# =====================================
# GENERATE QUESTION
# =====================================

if st.button(
    "🎯 Generate Interview Question"
):

    with st.spinner(
        "Preparing interview question..."
    ):

        try:

            response = start_interview(
                domain,
                st.session_state[
                    "session_id"
                ]
            )

            st.session_state.current_question = (
                response["question"]
            )

            st.session_state.evaluation_result = None

        except Exception as e:

            st.error(
                str(e)
            )

# =====================================
# DISPLAY QUESTION
# =====================================

if st.session_state.current_question:

    st.divider()

    st.subheader(
        "📌 Interview Question"
    )

    st.info(
        st.session_state.current_question
    )

    answer = st.text_area(
        "Your Answer",
        height=250,
        placeholder="Type your answer here..."
    )

    if st.button(
        "🚀 Evaluate Answer"
    ):

        if answer.strip() == "":

            st.warning(
                "Please enter an answer."
            )

        else:

            with st.spinner(
                "Evaluating..."
            ):

                try:

                    result = evaluate_answer(
                        st.session_state.current_question,
                        answer
                    )

                    st.session_state.evaluation_result = (
                        result
                    )

                    if "score" in result:

                        st.session_state.interview_history.append(
                            {
                                "question":
                                st.session_state.current_question,

                                "score":
                                result.get(
                                    "score",
                                    0
                                ),

                                "technical_accuracy":
                                result.get(
                                    "technical_accuracy",
                                    0
                                ),

                                "completeness":
                                result.get(
                                    "completeness",
                                    0
                                ),

                                "depth_of_understanding":
                                result.get(
                                    "depth_of_understanding",
                                    0
                                ),

                                "communication":
                                result.get(
                                    "communication",
                                    0
                                )
                            }
                        )

                except Exception as e:

                    st.error(
                        str(e)
                    )

# =====================================
# DISPLAY EVALUATION
# =====================================

if st.session_state.evaluation_result:

    result = st.session_state.evaluation_result

    st.divider()

    st.header(
        "📊 Evaluation Report"
    )

    score = result.get(
        "score",
        0
    )

    st.metric(
        "Overall Score",
        f"{score}/10"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "Technical Accuracy"
        )

        st.progress(
            result.get(
                "technical_accuracy",
                0
            ) / 10
        )

        st.write(
            f"{result.get('technical_accuracy', 0)}/10"
        )

        st.subheader(
            "Completeness"
        )

        st.progress(
            result.get(
                "completeness",
                0
            ) / 10
        )

        st.write(
            f"{result.get('completeness', 0)}/10"
        )

    with col2:

        st.subheader(
            "Depth of Understanding"
        )

        st.progress(
            result.get(
                "depth_of_understanding",
                0
            ) / 10
        )

        st.write(
            f"{result.get('depth_of_understanding', 0)}/10"
        )

        st.subheader(
            "Communication"
        )

        st.progress(
            result.get(
                "communication",
                0
            ) / 10
        )

        st.write(
            f"{result.get('communication', 0)}/10"
        )

    st.divider()

    st.subheader("✅ Strengths")

    for item in result.get(
        "strengths",
        []
    ):
        st.success(item)

    st.subheader("⚠ Weaknesses")

    for item in result.get(
        "weaknesses",
        []
    ):
        st.warning(item)

    st.subheader("📚 Missing Concepts")

    for item in result.get(
        "missing_concepts",
        []
    ):
        st.error(item)

    st.subheader("🌟 Ideal Answer")

    st.info(
        result.get(
            "ideal_answer",
            "Not available"
        )
    )

    st.subheader(
        "🎯 Follow-up Questions"
    )

    for item in result.get(
        "follow_up_questions",
        []
    ):
        st.markdown(
            f"- {item}"
        )

# =====================================
# RESET
# =====================================

if st.button(
    "🗑 Reset Interview"
):

    st.session_state.current_question = None

    st.session_state.evaluation_result = None

    st.rerun()