import streamlit as st
from utils.api import ask_resume

st.set_page_config(
    page_title="Resume Chat",
    page_icon="💬",
    layout="wide"
)

st.title("💬 Chat With Your Resume")

st.markdown("""
Ask anything about your resume.

Examples:
- What skills are mentioned in my resume?
- What projects have I worked on?
- What technologies do I know?
- Summarize my profile.
""")

# =====================================
# CHECK RESUME UPLOAD
# =====================================

if "session_id" not in st.session_state:

    st.warning(
        "⚠ Please upload a resume first from the Resume Analysis page."
    )

    st.stop()

# =====================================
# SESSION STATE
# =====================================

if "chat_history" not in st.session_state:

    st.session_state.chat_history = []

# =====================================
# QUESTION FORM
# =====================================

with st.form(
    "chat_form",
    clear_on_submit=True
):

    question = st.text_input(
        "Ask a question"
    )

    submit = st.form_submit_button(
        "🚀 Ask PrepPilot"
    )

# =====================================
# ASK QUESTION
# =====================================

if submit:

    if question.strip():

        with st.spinner(
            "Thinking..."
        ):

            try:

                response = ask_resume(
                    question,
                    st.session_state[
                        "session_id"
                    ]
                )

                st.session_state.chat_history.append(
                    {
                        "question": question,
                        "answer": response["answer"]
                    }
                )

            except Exception as e:

                st.error(
                    str(e)
                )

# =====================================
# DISPLAY CHAT
# =====================================

st.divider()

st.subheader(
    "🧠 Conversation"
)

if len(
    st.session_state.chat_history
) == 0:

    st.info(
        "Ask your first question."
    )

else:

    for chat in reversed(
        st.session_state.chat_history
    ):

        st.chat_message(
            "user"
        ).write(
            chat["question"]
        )

        st.chat_message(
            "assistant"
        ).write(
            chat["answer"]
        )

# =====================================
# CLEAR CHAT
# =====================================

if st.button(
    "🗑 Clear Chat"
):

    st.session_state.chat_history = []

    st.rerun()