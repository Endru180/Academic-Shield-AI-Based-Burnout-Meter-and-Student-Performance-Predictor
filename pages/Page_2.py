import streamlit as st

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    * {
        font-family: 'Inter', sans-serif !important;
    }
            
    .stApp {
        background-color: #3d8ef0;
    }

    /* Sembunyikan header bawaan Streamlit */
    header {visibility: hidden;}

    .stNumberInput input {
        border-radius: 50px;
        text-align: center;
        font-size: 1.0rem;
        font-weight: 600;
    }

    label[data-testid="stWidgetLabel"] p {
        font-size: 1.1rem !important;
        font-weight: 400 !important;
    }
            
    [data-testid="stForm"] {
        border: none;
        padding: 0;
        box-shadow: none;
        background-color: transparent;
    }

    [data-testid="stFormSubmitButton"] {
        display: flex;
        justify-content: center;
        margin-top: 40px;
    }

    [data-testid="stFormSubmitButton"] button {
        border-radius: 50px !important;
    }

    [data-testid="stFormSubmitButton"] button p {
        font-weight: 700 !important;
        font-size: 1.1rem !important;
    }

    [data-testid="stBaseButton-secondary"] {
        border-radius: 50px !important;
        background-color: rgba(0,0,0,0.5) !important;
        border: none !important;
        width: 100% !important;
    }

    [data-testid="stBaseButton-secondary"] p {
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        color: white !important;
    }

    [data-testid="stBaseButton-secondary"]:hover {
        background-color: rgba(0,0,0,0.7) !important;
        transition: background-color 0.2s ease;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# The Main Title
st.markdown(
    """
    <h1 style='text-align: center; margin-top: -60px; margin-bottom: -55px;'>MEASURE YOUR BURNOUT</h1>
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
    if st.button("Back", use_container_width=True, type="secondary"):
        st.switch_page("Page_1.py")
