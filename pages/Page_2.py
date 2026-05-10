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

    .stNumberInput input {
        background: transparent !important;
        border: none !important;
        border-radius: 0 !important;
        text-align: center !important;
        font-size: 1.0rem !important;
        font-weight: 600 !important;
        color: #ffffff !important;
    }

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
        filter: drop-shadow(0 0 1px rgba(0, 180, 216, 0.8)) drop-shadow(0 0 4px rgba(0, 180, 216, 0.6)) drop-shadow(0 0 7px rgba(0, 180, 216, 0.4)) !important;
        transition: all 0.2s ease !important;
    }

    .stNumberInput > div {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* Selectbox — khusus Page 2 */
    [data-testid="stSelectbox"] > div > div {
        background-color: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 8px !important;
        color: #ffffff !important;
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

    .stButton > button {
        border-radius: 50px !important;
        background: linear-gradient(90deg, #00b4d8, #0077b6) !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(0, 180, 216, 0.3) !important;
    }

    .stButton > button p {
        font-weight: 700 !important;
        color: white !important;
    }
    
    [data-testid="stTooltipIcon"]:hover svg {
        filter: drop-shadow(0 0 3px rgba(0, 180, 216, 1)) drop-shadow(0 0 7px rgba(0, 180, 216, 0.8)) drop-shadow(0 0 12px rgba(0, 180, 216, 0.6)) !important;
        transition: all 0.2s ease !important;
    }

    [data-testid="stButton"][key="back_btn"] button,
        div:has(> [data-testid="stBaseButton-secondary"]) button {
        border-radius: 50px !important;
        background: transparent !important;
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
        color: white !important;
        box-shadow: none !important;
        margin-top: 50px;
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
        st.switch_page("Page_1.py")
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
    exam_pressure = st.number_input(
        label="How much is your exam pressure (0–10)",
        min_value=0.0,
        max_value=10.0,
        step=1.0,
        format="%.0f",
        value=st.session_state.get("exam_pressure", 5.0),
        help="How much pressure do you feel from upcoming exams? 0 = none, 10 = extreme.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Family Expectation
    family_expectation = st.number_input(
        label='How much is your "Harapan Keluarga"? (0–10)',
        min_value=0.0,
        max_value=10.0,
        step=1.0,
        format="%.0f",
        value=st.session_state.get("family_expectation", 5.0),
        help="How much academic pressure do you feel from your family? 0 = none, 10 = extremely high.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Financial Stress
    financial_stress = st.number_input(
        label="How worry you are over your financial condition? (0–10)",
        min_value=0.0,
        max_value=10.0,
        step=1.0,
        format="%.0f",
        value=st.session_state.get("financial_stress", 5.0),
        help="How worried are you about financial matters? 0 = not at all, 10 = extremely.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Social Support
    social_support = st.number_input(
        label="How often your surrounding support you? (0–10)",
        min_value=0.0,
        max_value=10.0,
        step=1.0,
        format="%.0f",
        value=st.session_state.get("social_support", 5.0),
        help="How supported do you feel by friends, family, or peers? 0 = no support, 10 = fully supported.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Anxiety Score
    anxiety_score = st.number_input(
        label="How anxious are you? (0–10)",
        min_value=0.0,
        max_value=10.0,
        step=1.0,
        format="%.0f",
        value=st.session_state.get("anxiety_score", 5.0),
        help="How anxious do you feel on a daily basis? 0 = not anxious, 10 = extremely anxious.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Depression Score
    depression_score = st.number_input(
        label="How depressed you are recently? (0–10)",
        min_value=0.0,
        max_value=10.0,
        step=1.0,
        format="%.0f",
        value=st.session_state.get("depression_score", 5.0),
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
    if st.button("Back", use_container_width=True, key="back_btn"):
        st.switch_page("Page_1.py")
