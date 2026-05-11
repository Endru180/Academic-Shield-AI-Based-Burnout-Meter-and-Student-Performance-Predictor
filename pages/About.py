import streamlit as st
from utils import render_nav

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    * {
        font-family: 'Inter', sans-serif !important;
    }

    .stApp {
        background: linear-gradient(160deg, #010a14 0%, #071525 50%, #0c1a2e 100%);
        min-height: 100vh;
    }

    header {visibility: hidden;}

    @keyframes fade-in-up {
        from { opacity: 0; transform: translateY(28px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes title-shimmer {
        0%   { background-position: 0% center; }
        100% { background-position: 200% center; }
    }

    .gradient-title {
        text-align: center;
        background: linear-gradient(90deg, #00d4ff 0%, #a0c8ff 50%, #00d4ff 100%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: title-shimmer 4s linear infinite;
        filter: drop-shadow(0 0 12px rgba(0, 212, 255, 0.5));
    }
    </style>
    """,
    unsafe_allow_html=True,
)

render_nav()

st.markdown(
    """
    <h1 class='gradient-title' style='margin-top: -60px; margin-bottom: -40px;'>MEASURE YOUR BURNOUT</h1>
    <h1 class='gradient-title' style='margin-bottom: 20px;'>& PREDICT YOUR GRADE</h1>
    """,
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    """
    <div style='
        border: 1px solid rgba(0, 212, 255, 0.18);
        padding: 2rem 2.5rem;
        border-radius: 16px;
        background: rgba(0, 180, 216, 0.06);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        box-shadow: 0 8px 40px rgba(0, 0, 0, 0.6);
        color: white;
        animation: fade-in-up 0.5s ease both;
        transition: border-color 0.35s ease, box-shadow 0.35s ease;
    '>
        <h3 style='margin-top: 0;'>How It Works</h3>
        <p style='line-height: 1.8; color: rgba(255,255,255,0.85);'>
            Academic Shield uses two machine learning models trained on student lifestyle and wellbeing data.
            The first model predicts your <b>burnout score</b> (0–100) based on inputs like study hours, sleep,
            exam pressure, stress level, anxiety, depression, financial stress, social support, and family expectations.
            The second model predicts your <b>future GPA</b> using your daily time allocation across studying,
            extracurricular activities, sleep, socializing, and physical activity, combined with your stress level.
            Both models were trained using supervised learning with scikit-learn, and the predictions are meant
            to give you a data-driven snapshot of your academic wellbeing — not a clinical diagnosis.
        </p>
        <h3>About the Data</h3>
        <p style='line-height: 1.8; color: rgba(255,255,255,0.85);'>
            The models were trained on anonymized student survey data covering a range of academic workloads,
            sleep patterns, and mental health indicators. Stress level categories (Low, Moderate, High) are
            encoded using a label encoder fitted during training. All predictions are local to your session
            and no personal data is stored or transmitted.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
