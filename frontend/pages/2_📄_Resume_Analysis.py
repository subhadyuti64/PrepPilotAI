import streamlit as st
from utils.api import analyze_resume, upload_resume
from utils.styles import load_css

st.set_page_config(
    page_title="Resume Analysis",
    page_icon="📄",
    layout="wide"
)

load_css()

# =====================================
# HEADER
# =====================================

st.title("📄 Resume Analysis")
st.caption(
    "AI-Powered Resume Intelligence & Career Insights"
)

# =====================================
# UPLOAD RESUME
# =====================================

st.subheader("📤 Upload Resume")

uploaded_file = st.file_uploader(
    "Choose a PDF Resume",
    type=["pdf"]
)

if uploaded_file:

    if st.button(
        "📤 Upload Resume",
        use_container_width=True
    ):

        with st.spinner(
            "Uploading Resume..."
        ):

            try:

                response = upload_resume(
                    uploaded_file
                )

                st.session_state[
                    "session_id"
                ] = response[
                    "session_id"
                ]

                st.success(
                    "✅ Resume uploaded successfully!"
                )

            except Exception as e:

                st.error(
                    str(e)
                )

# =====================================
# ANALYZE BUTTON
# =====================================

col1, col2, col3 = st.columns(
    [1, 2, 1]
)

with col2:

    if st.button(
        "🔍 Analyze Resume",
        use_container_width=True
    ):

        with st.spinner(
            "Analyzing Resume..."
        ):

            try:

                if "session_id" not in st.session_state:

                    st.error(
                        "Please upload a resume first."
                    )

                else:

                    data = analyze_resume(
                        st.session_state[
                            "session_id"
                        ]
                    )

                    st.session_state[
                        "analysis"
                    ] = data

            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )

# =====================================
# DISPLAY ANALYSIS
# =====================================

if "analysis" in st.session_state:

    analysis = st.session_state[
        "analysis"
    ]

    st.success(
        "✅ Resume analyzed successfully!"
    )

    # =====================================
    # PROFILE OVERVIEW
    # =====================================

    st.subheader(
        "👤 Candidate Overview"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(f"""
        <div class='card'>
        <h4>👤 Candidate Name</h4>
        <p>{analysis.get("candidate_name", "Not Available")}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown(f"""
        <div class='card'>
        <h4>🎓 Education</h4>
        <p>{analysis.get("education", "Not Available")}</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # =====================================
    # SKILLS
    # =====================================

    st.subheader(
        "🛠 Technical Skills"
    )

    skills = analysis.get(
        "skills",
        []
    )

    if skills:

        skills_html = ""

        for skill in skills:

            skills_html += f"""
            <span class='skill-badge'>
            {skill}
            </span>
            """

        st.markdown(
            skills_html,
            unsafe_allow_html=True
        )

    else:

        st.warning(
            "No skills found."
        )

    st.divider()

    # =====================================
    # PROJECTS
    # =====================================

    st.subheader(
        "🚀 Projects"
    )

    projects = analysis.get(
        "projects",
        []
    )

    if projects:

        for project in projects:

            # New structured format
            if isinstance(
                project,
                dict
            ):

                st.markdown(f"""
                <div class='project-card'>

                <h3>
                🚀 {project.get("name", "Project")}
                </h3>

                <p>
                <b>📅 Date:</b>
                {project.get("date", "N/A")}
                </p>

                <p>
                {project.get("description", "")}
                </p>

                </div>
                """, unsafe_allow_html=True)

            # Old string format fallback
            else:

                st.markdown(f"""
                <div class='project-card'>
                <h4>🚀 {project}</h4>
                </div>
                """, unsafe_allow_html=True)

    else:

        st.warning(
            "No projects found."
        )
    st.divider()

    # =====================================
    # STRENGTHS
    # =====================================

    st.subheader(
        "💪 Strengths"
    )

    strengths = analysis.get(
        "strengths",
        []
    )

    if strengths:

        for strength in strengths:

            st.markdown(f"""
            <div class='success-card'>
            ✅ {strength}
            </div>
            """, unsafe_allow_html=True)

    else:

        st.warning(
            "No strengths found."
        )

    st.divider()

    # =====================================
    # RECOMMENDED ROLES
    # =====================================

    st.subheader(
        "🎯 Recommended Roles"
    )

    roles = analysis.get(
        "recommended_roles",
        []
    )

    if roles:

        roles_html = ""

        for role in roles:

            roles_html += f"""
            <span class='skill-badge'>
            {role}
            </span>
            """

        st.markdown(
            roles_html,
            unsafe_allow_html=True
        )

    else:

        st.warning(
            "No recommended roles found."
        )

    st.divider()

    # =====================================
    # IMPROVEMENTS
    # =====================================

    st.subheader(
        "📈 Areas for Improvement"
    )

    improvements = analysis.get(
        "areas_for_improvement",
        []
    )

    if improvements:

        for item in improvements:

            st.markdown(f"""
            <div class='warning-card'>
            ⚠ {item}
            </div>
            """, unsafe_allow_html=True)

    else:

        st.success(
            "No major improvements suggested."
        )

    st.divider()

    # =====================================
    # STATS
    # =====================================

    st.subheader(
        "📊 Resume Statistics"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Skills",
        len(skills)
    )

    col2.metric(
        "Projects",
        len(projects)
    )

    col3.metric(
        "Recommended Roles",
        len(roles)
    )