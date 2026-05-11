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

    .tip-card {
        border: 1px solid rgba(0, 212, 255, 0.18);
        padding: 1.5rem 2rem;
        border-radius: 16px;
        background: rgba(0, 180, 216, 0.06);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        box-shadow: 0 8px 40px rgba(0, 0, 0, 0.6);
        margin-bottom: 1.5rem;
        color: white;
        animation: fade-in-up 0.45s ease both;
        transition: border-color 0.3s ease, box-shadow 0.3s ease, transform 0.2s ease;
    }

    .tip-card:hover {
        border-color: rgba(0, 212, 255, 0.6);
        box-shadow: 0 8px 40px rgba(0, 0, 0, 0.6), 0 0 30px rgba(0, 212, 255, 0.2);
        transform: translateY(-3px);
    }

    .tip-card.active {
        border: 1px solid rgba(0, 212, 255, 0.7);
        background: rgba(0, 212, 255, 0.09);
        box-shadow: 0 8px 40px rgba(0, 0, 0, 0.6), 0 0 35px rgba(0, 212, 255, 0.25);
    }

    .tip-card h3 {
        margin-top: 0;
        margin-bottom: 0.8rem;
    }

    .tip-card ul {
        margin: 0;
        padding-left: 1.4rem;
        line-height: 2;
        color: rgba(255,255,255,0.85);
    }

    .badge {
        display: inline-block;
        padding: 2px 12px;
        border-radius: 50px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-left: 10px;
        vertical-align: middle;
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

# Detect user's burnout category from session state if available
burnout_score = st.session_state.get("burnout_score", None)

if burnout_score is not None:
    if burnout_score >= 70:
        user_category = "burnout"
    elif burnout_score >= 40:
        user_category = "mild"
    else:
        user_category = "healthy"
    st.markdown(
        f"<p style='text-align:center; color:rgba(255,255,255,0.7); margin-bottom: 1.5rem;'>"
        f"Showing tips based on your burnout score: <b style='color:white;'>{burnout_score:.1f}/100</b></p>",
        unsafe_allow_html=True,
    )
else:
    user_category = None
    st.markdown(
        "<p style='text-align:center; color:rgba(255,255,255,0.6); margin-bottom: 1.5rem;'>"
        "Complete the assessment to get personalized tips, or browse all categories below.</p>",
        unsafe_allow_html=True,
    )

# --- Healthy ---
active_healthy = "active" if user_category == "healthy" else ""
you_badge = "<span class='badge' style='background:rgba(46,204,113,0.3); color:#2ecc71;'>You are here</span>" if user_category == "healthy" else ""
st.markdown(
    f"""
    <div class='tip-card {active_healthy}' style='animation-delay: 0s;'>
        <h3 style='color:#2ecc71;'>🟢 Healthy (Score 0–39) {you_badge}</h3>
        <p style='color:rgba(255,255,255,0.7); margin-bottom:0.8rem;'>
            You're in great shape. The goal now is to stay consistent and protect your balance.
        </p>
        <ul>
            <li>Keep your sleep schedule consistent — even on weekends.</li>
            <li>Don't let exam season be an excuse to drop exercise or social time.</li>
            <li>Do a weekly check-in with yourself: how's your energy and mood?</li>
            <li>Protect your free time — it's not wasted time, it's recovery time.</li>
            <li>Stay connected with friends and family regularly.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Mildly Burnout ---
active_mild = "active" if user_category == "mild" else ""
you_badge = "<span class='badge' style='background:rgba(243,156,18,0.3); color:#f39c12;'>You are here</span>" if user_category == "mild" else ""
st.markdown(
    f"""
    <div class='tip-card {active_mild}' style='animation-delay: 0.1s;'>
        <h3 style='color:#f39c12;'>🟡 Mildly Burnout (Score 40–69) {you_badge}</h3>
        <p style='color:rgba(255,255,255,0.7); margin-bottom:0.8rem;'>
            Early warning signs are showing. Small adjustments now can prevent full burnout.
        </p>
        <ul>
            <li>Aim for at least 7 hours of sleep — cut late-night study sessions.</li>
            <li>Use the Pomodoro technique: 25 min focus, 5 min break.</li>
            <li>Identify your biggest stressor and tackle it first each day.</li>
            <li>Reduce screen time 30 minutes before bed to improve sleep quality.</li>
            <li>Add at least 20 minutes of light physical activity (walk, stretch) daily.</li>
            <li>Talk to a friend or family member about how you're feeling.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Burnout ---
active_burnout = "active" if user_category == "burnout" else ""
you_badge = "<span class='badge' style='background:rgba(231,76,60,0.3); color:#e74c3c;'>You are here</span>" if user_category == "burnout" else ""
st.markdown(
    f"""
    <div class='tip-card {active_burnout}' style='animation-delay: 0.2s;'>
        <h3 style='color:#e74c3c;'>🔴 Burnout (Score 70–100) {you_badge}</h3>
        <p style='color:rgba(255,255,255,0.7); margin-bottom:0.8rem;'>
            Your burnout level is high. Recovery should be your top priority right now.
        </p>
        <ul>
            <li>Take at least one full rest day this week — no studying, no obligations.</li>
            <li>Temporarily reduce your study load and focus only on what's critical.</li>
            <li>Prioritize the basics: 8 hours of sleep, regular meals, and hydration.</li>
            <li>Reach out to your campus counselor or a trusted person you can talk to.</li>
            <li>Avoid comparing your progress to others — focus on your own recovery.</li>
            <li>Consider speaking to a mental health professional if symptoms persist.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)
