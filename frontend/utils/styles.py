import streamlit as st

def load_css():

    st.markdown("""
    <style>

    .main {
        padding-top: 1rem;
    }

    .block-container {
        padding-top: 1rem;
        max-width: 1400px;
    }

    .hero-title {
        text-align:center;
        font-size:3rem;
        font-weight:700;
        color:#4F46E5;
        margin-bottom:0;
    }

    .hero-subtitle {
        text-align:center;
        color:#94A3B8;
        font-size:1.1rem;
        margin-bottom:2rem;
    }

    .card {
        background:#111827;
        padding:20px;
        border-radius:16px;
        border:1px solid #374151;
        margin-bottom:15px;
    }

    .project-card {
        background:linear-gradient(
            135deg,
            #0F172A,
            #1E293B
        );
        padding:20px;
        border-radius:16px;
        border:1px solid #334155;
        margin-bottom:12px;
    }

    .skill-badge {
        display:inline-block;
        background:#2563EB;
        color:white;
        padding:8px 14px;
        border-radius:20px;
        margin:4px;
        font-size:14px;
    }

    .success-card {
        background:#052e16;
        padding:15px;
        border-radius:12px;
        border:1px solid #16a34a;
    }

    .warning-card {
        background:#3f2a00;
        padding:15px;
        border-radius:12px;
        border:1px solid #f59e0b;
    }

    .danger-card {
        background:#450a0a;
        padding:15px;
        border-radius:12px;
        border:1px solid #ef4444;
    }

    </style>
    """, unsafe_allow_html=True)