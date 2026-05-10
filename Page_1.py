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
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        min-height: 100vh;
    }

    header {visibility: hidden;}

    /* Wrapper jadi satu pill utuh */
    .stNumberInput [data-baseweb="input"] {
        background: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 50px !important;
        overflow: hidden !important;
        gap: 0 !important;
        padding: 0 !important;
        box-shadow: none !important;
    }

    /* Input field transparan, ikut background wrapper */
    .stNumberInput input {
        background: transparent !important;
        border: none !important;
        border-radius: 0 !important;
        text-align: center !important;
        font-size: 1.0rem !important;
        font-weight: 600 !important;
        color: #ffffff !important;
    }

    /* Tombol transparan, ikut background wrapper */
    .stNumberInput button {
        background: transparent !important;
        border: none !important;
        color: #ffffff !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
    }

    .stNumberInput button:hover {
        background: transparent !important;
        color: #00b4d8 !important;
        filter: drop-shadow(0 0 2px rgba(0, 180, 216, 0.8)) drop-shadow(0 0 5px rgba(0, 180, 216, 0.6)) drop-shadow(0 0 8px rgba(0, 180, 216, 0.4)) !important;
        transition: all 0.2s ease !important;
    }

    .stNumberInput > div {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    label[data-testid="stWidgetLabel"] p {
        font-size: 1.1rem !important;
        font-weight: 400 !important;
    }

    [data-testid="stForm"] {
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        padding: 2rem 2.5rem !important;
        border-radius: 16px !important;
        background: rgba(255, 255, 255, 0.07) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3) !important;
    }

    [data-testid="stFormSubmitButton"] {
        display: flex;
        justify-content: center;
        margin-top: 40px;
    }

    [data-testid="stFormSubmitButton"] button {
        border-radius: 50px !important;
        background: linear-gradient(90deg, #00b4d8, #0077b6) !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(0, 180, 216, 0.35) !important;
    }

    [data-testid="stFormSubmitButton"] button p {
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        color: #ffffff !important;
    }

    [data-testid="stTooltipIcon"]:hover {
        filter: drop-shadow(0 0 1px rgba(0, 180, 216, 0.8)) drop-shadow(0 0 4px rgba(0, 180, 216, 0.6)) drop-shadow(0 0 7px rgba(0, 180, 216, 0.4)) !important;
        transition: all 0.2s ease !important;
        cursor: pointer !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

render_nav()

# The Main Title
st.markdown(
    """
    <h1 style='text-align: center; margin-top: -60px; margin-bottom: -40px;'>MEASURE YOUR BURNOUT</h1>
    <h1 style='text-align: center; margin-bottom: 20px;'>& PREDICT YOUR GRADE</h1>
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
    study_hours = st.number_input(
        label="How many hours do you study per day?",
        min_value=0.0,
        max_value=10.0,
        step=0.5,
        format="%.1f",
        value=st.session_state.get("study_hours", 4.0),
        help="Average study hours per day including assignments and self-study.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Sleep Time
    sleep_hours = st.number_input(
        label="How long do you sleep per day?",
        min_value=0.0,
        max_value=12.0,
        step=0.5,
        format="%.1f",
        value=st.session_state.get("sleep_hours", 8.0),
        help="Average hours of sleep per night. Naps count too.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Extracurricular Time
    eca_hours = st.number_input(
        label="How long do you spend your time in extracurricular activities per day?",
        min_value=0.0,
        max_value=8.0,
        step=0.5,
        format="%.1f",
        value=st.session_state.get("eca_hours", 1.0),
        help="Time spent on clubs, organizations, or extracurricular activities per day.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Social/Free Time
    social_hours = st.number_input(
        label="How long do you socialize per day?",
        min_value=0.0,
        max_value=10.0,
        step=0.5,
        format="%.1f",
        value=st.session_state.get("social_hours", 5.0),
        help="Time spent hanging out or socializing with friends or family per day.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Physical Time
    physical_hours = st.number_input(
        label="How long do you exercise per day?",
        min_value=0.0,
        max_value=8.0,
        step=0.5,
        format="%.1f",
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
