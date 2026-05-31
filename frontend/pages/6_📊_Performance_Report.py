import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Performance Report",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Interview Performance Report")

# =====================================
# CHECK HISTORY
# =====================================

history = st.session_state.get(
    "interview_history",
    []
)

if len(history) == 0:

    st.info(
        "No interview attempts yet. Complete a mock interview first."
    )

    st.stop()

# =====================================
# DATAFRAME
# =====================================

df = pd.DataFrame(history)

# =====================================
# OVERALL METRICS
# =====================================

avg_score = round(
    df["score"].mean(),
    1
)

best_score = round(
    df["score"].max(),
    1
)

total_attempts = len(df)

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "📈 Average Score",
        f"{avg_score}/10"
    )

with col2:

    st.metric(
        "🏆 Best Score",
        f"{best_score}/10"
    )

with col3:

    st.metric(
        "🎯 Total Interviews",
        total_attempts
    )

st.divider()

# =====================================
# SCORE TREND
# =====================================

st.subheader("📉 Score Trend")

chart_df = pd.DataFrame(
    {
        "Attempt": range(
            1,
            len(df) + 1
        ),
        "Score": df["score"]
    }
)

st.line_chart(
    chart_df.set_index(
        "Attempt"
    )
)

st.divider()

# =====================================
# SKILL BREAKDOWN
# =====================================

st.subheader("📊 Skill Breakdown")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Technical Accuracy",
        round(
            df[
                "technical_accuracy"
            ].mean(),
            1
        )
    )

    st.metric(
        "Completeness",
        round(
            df[
                "completeness"
            ].mean(),
            1
        )
    )

with col2:

    st.metric(
        "Depth of Understanding",
        round(
            df[
                "depth_of_understanding"
            ].mean(),
            1
        )
    )

    st.metric(
        "Communication",
        round(
            df[
                "communication"
            ].mean(),
            1
        )
    )

st.divider()

# =====================================
# PERFORMANCE INSIGHTS
# =====================================

st.subheader("🎯 Performance Insights")

categories = {
    "Technical Accuracy":
    df[
        "technical_accuracy"
    ].mean(),

    "Completeness":
    df[
        "completeness"
    ].mean(),

    "Depth of Understanding":
    df[
        "depth_of_understanding"
    ].mean(),

    "Communication":
    df[
        "communication"
    ].mean()
}

best_area = max(
    categories,
    key=categories.get
)

worst_area = min(
    categories,
    key=categories.get
)

col1, col2 = st.columns(2)

with col1:

    st.success(
        f"💪 Strongest Area: {best_area}"
    )

with col2:

    st.error(
        f"📈 Needs Improvement: {worst_area}"
    )

st.divider()

# =====================================
# AI COACH
# =====================================

st.subheader("🤖 AI Coach Recommendation")

if worst_area == "Technical Accuracy":

    st.warning(
        """
Focus on strengthening your core technical concepts.

Tips:
- Revise fundamentals
- Practice explaining concepts clearly
- Learn common interview patterns
"""
    )

elif worst_area == "Completeness":

    st.warning(
        """
Your answers often miss important details.

Tips:
- Cover all aspects of the question
- Mention edge cases
- Include examples
"""
    )

elif worst_area == "Depth of Understanding":

    st.warning(
        """
Try to go deeper than definitions.

Tips:
- Explain why things work
- Discuss tradeoffs
- Connect concepts with real-world usage
"""
    )

elif worst_area == "Communication":

    st.warning(
        """
Improve answer structure and clarity.

Tips:
- Think before answering
- Use step-by-step explanations
- Provide concise examples
"""
    )

st.divider()

# =====================================
# PERFORMANCE SUMMARY
# =====================================

st.subheader("🎯 Overall Assessment")

if avg_score >= 8:

    st.success(
        """
Excellent interview performance.

You are close to being interview-ready.
Keep practicing advanced questions.
"""
    )

elif avg_score >= 6:

    st.warning(
        """
Good performance.

Focus on improving weaker areas to consistently score above 8.
"""
    )

else:

    st.error(
        """
You need more interview practice.

Focus on fundamentals, structured answers and technical depth.
"""
    )

st.divider()

# =====================================
# INTERVIEW HISTORY
# =====================================

st.subheader("📝 Interview History")

for i, row in df.iterrows():

    with st.expander(
        f"Interview #{i+1} | Score: {row['score']}/10"
    ):

        st.write(
            "Question:"
        )

        st.info(
            row["question"]
        )

        st.write(
            f"Technical Accuracy: {row['technical_accuracy']}/10"
        )

        st.write(
            f"Completeness: {row['completeness']}/10"
        )

        st.write(
            f"Depth of Understanding: {row['depth_of_understanding']}/10"
        )

        st.write(
            f"Communication: {row['communication']}/10"
        )

st.divider()

# =====================================
# CLEAR HISTORY
# =====================================

if st.button(
    "🗑 Clear Performance History",
    use_container_width=True
):

    st.session_state.interview_history = []

    st.success(
        "History cleared successfully."
    )

    st.rerun()