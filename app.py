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

with st.form("my form"):
    # Input Study Time
    study_time = st.number_input(
        label="Input your study time",
        min_value=0.0,
        max_value=15.0,
        step=0.5,
        value=6.0,
        format="%.1f",
        help="Enter your average study hours per day over the past week. Include self-study, assignments, and reading materials.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Sleep Time
    sleep_time = st.number_input(
        label="Input your sleep time",
        min_value=0.0,
        max_value=12.0,
        step=0.5,
        value=7.0,
        format="%.1f",
        help="Your average hours of sleep per night. Naps count too.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Social/Free Time
    social_free_time = st.number_input(
        label="Input your social/free time",
        min_value=0.0,
        max_value=10.0,
        step=0.5,
        value=3.0,
        format="%.1f",
        help="Time spent on hanging out, hobbies, gaming, or any non-academic activities per day.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input GPA
    current_gpa = st.number_input(
        label="Input your current GPA",
        min_value=0.0,
        max_value=4.0,
        value=2.5,
        help="Your latest GPA or midterm grade on a 0.0 - 4.0 scale.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Study Environment
    environment = st.selectbox(
        "Your study environment",
        ["Quiet", "Moderate", "Noisy"],
        help="Quiet = library or silent room. Moderate = cafe or co-working space. Noisy = crowded dorm or loud area.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Coping Strategy
    coping = st.selectbox(
        "Your coping strategy",
        ["Intellect/Coping Well", "Emotional/Stressed"],
        help="Intellect = you stay calm and structured under pressure. Emotional = you tend to feel anxious or overwhelmed easily.",
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Analyze Button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        submitted = st.form_submit_button(
            "Analyze!", type="primary", use_container_width=True
        )

if submitted:
    st.session_state.study_time = study_time
    st.session_state.sleep_time = sleep_time
    st.session_state.social_free_time = social_free_time
    st.session_state.current_gpa = current_gpa
    st.session_state.environment = environment
    st.session_state.coping = coping

    st.switch_page("pages/result.py")
