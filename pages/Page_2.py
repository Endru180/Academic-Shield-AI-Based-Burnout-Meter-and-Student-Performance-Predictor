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

    /* Slider thumb */
    [data-testid="stSlider"] [data-baseweb="slider"] div[role="slider"] {
        background-color: #00d4ff !important;
        border: 2px solid #00d4ff !important;
        box-shadow: 0 0 8px rgba(0, 212, 255, 0.6) !important;
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

    [data-testid="stSelectbox"] > div > div {
        background-color: rgba(0, 20, 45, 0.7) !important;
        border: 1px solid rgba(0, 212, 255, 0.25) !important;
        border-radius: 8px !important;
        color: #ffffff !important;
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

    .stButton > button {
        border-radius: 50px !important;
        background: linear-gradient(90deg, #00d4ff, #0055a5) !important;
        border: none !important;
        animation: pulse-glow 2.4s ease-in-out infinite !important;
        transition: transform 0.15s ease !important;
    }

    .stButton > button p {
        font-weight: 700 !important;
        color: white !important;
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

st.markdown(
    """
    <div style='
        background-color: rgba(255,255,255,0.15);
        border-left: 4px solid red;
        padding: 12px 16px;
        border-radius: 4px;
        margin-top: 5px;
        margin-bottom: 45px;
        font-size: 0.9rem;
        color: white;
    '>
        🔒 <b>Privacy Notice:</b> Your responses to the questions below are sensitive in nature. 
        All inputs are used solely for prediction purposes and are <b>never stored or shared</b>.
    </div>
    """,
    unsafe_allow_html=True,
)

# Checking the input completeness from page 1
required_keys = [
    "study_hours",
    "sleep_hours",
    "eca_hours",
    "social_hours",
    "physical_hours",
]

if not all(key in st.session_state for key in required_keys):
    st.warning("Please complete all the form in page 1 first.")
    if st.button("Back to page 1"):
        st.switch_page("app.py")
    st.stop()

with st.form("page2_form"):
    # Input Stress Level
    stress_level_category = st.selectbox(
        label="How is your stress condition recently?",
        options=["Low", "Moderate", "High"],
        index=["Low", "Moderate", "High"].index(
            st.session_state.get("stress_level_category", "Moderate")
        ),
        help="Low = rarely stressed, Moderate = sometimes stressed, High = frequently stressed.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Exam Pressure
    exam_pressure = st.slider(
        label="How much is your exam pressure (0–10)",
        min_value=0,
        max_value=10,
        step=1,
        value=int(st.session_state.get("exam_pressure", 5)),
        help="How much pressure do you feel from upcoming exams? 0 = none, 10 = extreme.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Family Expectation
    family_expectation = st.slider(
        label='How much is your "Harapan Keluarga"? (0–10)',
        min_value=0,
        max_value=10,
        step=1,
        value=int(st.session_state.get("family_expectation", 5)),
        help="How much academic pressure do you feel from your family? 0 = none, 10 = extremely high.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Financial Stress
    financial_stress = st.slider(
        label="How worry you are over your financial condition? (0–10)",
        min_value=0,
        max_value=10,
        step=1,
        value=int(st.session_state.get("financial_stress", 5)),
        help="How worried are you about financial matters? 0 = not at all, 10 = extremely.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Social Support
    social_support = st.slider(
        label="How often your surrounding support you? (0–10)",
        min_value=0,
        max_value=10,
        step=1,
        value=int(st.session_state.get("social_support", 5)),
        help="How supported do you feel by friends, family, or peers? 0 = no support, 10 = fully supported.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Anxiety Score
    anxiety_score = st.slider(
        label="How anxious are you? (0–10)",
        min_value=0,
        max_value=10,
        step=1,
        value=int(st.session_state.get("anxiety_score", 5)),
        help="How anxious do you feel on a daily basis? 0 = not anxious, 10 = extremely anxious.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Depression Score
    depression_score = st.slider(
        label="How depressed you are recently? (0–10)",
        min_value=0,
        max_value=10,
        step=1,
        value=int(st.session_state.get("depression_score", 5)),
        help="How low or hopeless do you feel lately? 0 = not at all, 10 = severely.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Analyze Button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        submitted = st.form_submit_button(
            "Analyze!", type="primary", use_container_width=True
        )

if submitted:
    st.session_state.stress_level_category = stress_level_category
    st.session_state.exam_pressure = exam_pressure
    st.session_state.family_expectation = family_expectation
    st.session_state.financial_stress = financial_stress
    st.session_state.social_support = social_support
    st.session_state.anxiety_score = anxiety_score
    st.session_state.depression_score = depression_score

    st.switch_page("pages/result.py")

# To go back to page 1
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Back", use_container_width=True, type="secondary"):
        st.switch_page("Page_1.py")
