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
    </style>
    """,
    unsafe_allow_html=True,
)

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
