import streamlit as st
from utils import render_nav

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    * {
        font-family: 'Inter', sans-serif !important;
    }

    .stApp {
        background: radial-gradient(ellipse at center, rgba(0,212,255,0.07) 0%, transparent 55%),
                    radial-gradient(ellipse at center, #0c1a2e 0%, #071525 55%, #010a14 100%);
        min-height: 100vh;
    }

    /* Sembunyikan header bawaan Streamlit */
    header {visibility: hidden;}

    @keyframes pulse-glow {
        0%   { box-shadow: 0 0 6px rgba(0,212,255,0.4), 0 4px 15px rgba(0,180,216,0.35); }
        50%  { box-shadow: 0 0 22px rgba(0,212,255,0.85), 0 4px 28px rgba(0,180,216,0.65); }
        100% { box-shadow: 0 0 6px rgba(0,212,255,0.4), 0 4px 15px rgba(0,180,216,0.35); }
    }
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

    /* Slider track */
    [data-testid="stSlider"] [data-baseweb="slider"] div[role="slider"] {
        background-color: #00d4ff !important;
        border: 2px solid #00d4ff !important;
        box-shadow: 0 0 8px rgba(0, 212, 255, 0.6) !important;
    }

    [data-testid="stSlider"] [data-baseweb="slider"] div[data-testid="stTickBarMin"],
    [data-testid="stSlider"] [data-baseweb="slider"] div[data-testid="stTickBarMax"] {
        color: rgba(255,255,255,0.5) !important;
    }

    /* Filled portion of track */
    [data-testid="stSlider"] [data-baseweb="slider"] div:nth-child(3) > div:first-child {
        background: linear-gradient(90deg, #00d4ff, #0055a5) !important;
    }

    /* Unfilled portion of track */
    [data-testid="stSlider"] [data-baseweb="slider"] div:nth-child(3) > div:last-child {
        background: rgba(0, 212, 255, 0.15) !important;
    }

    /* Value label */
    [data-testid="stSlider"] [data-baseweb="slider"] div[data-testid="stThumbValue"] {
        color: #00d4ff !important;
        font-weight: 600 !important;
    }

    label[data-testid="stWidgetLabel"] p {
        font-size: 1.1rem !important;
        font-weight: 400 !important;
    }

    [data-testid="stForm"] {
        border: 1px solid rgba(0, 212, 255, 0.18) !important;
        padding: 2rem 2.5rem !important;
        border-radius: 16px !important;
        background: rgba(0, 180, 216, 0.06) !important;
        backdrop-filter: blur(14px) !important;
        -webkit-backdrop-filter: blur(14px) !important;
        box-shadow: 0 8px 40px rgba(0, 0, 0, 0.6) !important;
        animation: fade-in-up 0.5s ease both !important;
        transition: border-color 0.35s ease, box-shadow 0.35s ease !important;
    }

    [data-testid="stForm"]:hover {
        border-color: rgba(0, 212, 255, 0.55) !important;
        box-shadow: 0 8px 40px rgba(0, 0, 0, 0.6), 0 0 28px rgba(0, 212, 255, 0.18) !important;
    }

    [data-testid="stFormSubmitButton"] {
        display: flex;
        justify-content: center;
        margin-top: 40px;
    }

    [data-testid="stFormSubmitButton"] button {
        border-radius: 50px !important;
        background: linear-gradient(90deg, #00d4ff, #0055a5) !important;
        border: none !important;
        animation: pulse-glow 2.4s ease-in-out infinite !important;
        transition: transform 0.15s ease !important;
    }

    [data-testid="stFormSubmitButton"] button:hover {
        transform: scale(1.03) !important;
    }

    [data-testid="stFormSubmitButton"] button p {
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

render_nav()

# The Main Title
st.markdown(
    """
    <h1 class='gradient-title' style='margin-top: -60px; margin-bottom: -40px;'>MEASURE YOUR BURNOUT</h1>
    <h1 class='gradient-title' style='margin-bottom: 20px;'>& PREDICT YOUR GRADE</h1>
    """,
    unsafe_allow_html=True,
)

# Short Desc
st.markdown(
    "<p style='text-align: center;'>Chronic <a href='https://en.wikipedia.org/wiki/Occupational_burnout' target='_blank' style='color: white; text-decoration: none;'>burnout</a> reduces focus, memory, and motivation, directly lowering your GPA. Track your daily habits to see where you stand.</p>",
    unsafe_allow_html=True,
)
st.markdown("<br>", unsafe_allow_html=True)

with st.form("page1_form"):
    # Input Study Time
    study_hours = st.slider(
        label="How many hours do you study per day?",
        min_value=0.0,
        max_value=10.0,
        step=0.5,
        value=st.session_state.get("study_hours", 4.0),
        help="Average study hours per day including assignments and self-study.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Sleep Time
    sleep_hours = st.slider(
        label="How long do you sleep per day?",
        min_value=0.0,
        max_value=12.0,
        step=0.5,
        value=st.session_state.get("sleep_hours", 8.0),
        help="Average hours of sleep per night. Naps count too.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Extracurricular Time
    eca_hours = st.slider(
        label="How long do you spend your time in extracurricular activities per day?",
        min_value=0.0,
        max_value=8.0,
        step=0.5,
        value=st.session_state.get("eca_hours", 1.0),
        help="Time spent on clubs, organizations, or extracurricular activities per day.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Social/Free Time
    social_hours = st.slider(
        label="How long do you socialize per day?",
        min_value=0.0,
        max_value=10.0,
        step=0.5,
        value=st.session_state.get("social_hours", 5.0),
        help="Time spent hanging out or socializing with friends or family per day.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Physical Time
    physical_hours = st.slider(
        label="How long do you exercise per day?",
        min_value=0.0,
        max_value=8.0,
        step=0.5,
        value=st.session_state.get("physical_hours", 2.0),
        help="Time spent on exercise, sports, or any physical activity per day.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Next Button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        submitted = st.form_submit_button(
            "Next", type="primary", use_container_width=True
        )

if submitted:
    st.session_state.study_hours = study_hours
    st.session_state.sleep_hours = sleep_hours
    st.session_state.eca_hours = eca_hours
    st.session_state.social_hours = social_hours
    st.session_state.physical_hours = physical_hours

    st.switch_page("pages/Page_2.py")
