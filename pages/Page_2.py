import streamlit as st

from src.config import PAGE1_KEYS
from src.ui import inject_css, render_animated_header, render_progress_bar, render_privacy_notice, render_neural_background, render_hamburger_menu

st.set_page_config(page_title="Academic Shield — Step 2", layout="centered", initial_sidebar_state="collapsed")
inject_css()
render_neural_background()
render_hamburger_menu()

render_animated_header(
    "Measure Your Burnout & Predict Your Grade",
)

render_progress_bar(2, 2, "Mental Health &amp; Stress")

# Validate Page 1 completion
if not all(key in st.session_state for key in PAGE1_KEYS):
    st.warning("Please complete the lifestyle form first.")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("← Back to Step 1", use_container_width=True, type="secondary"):
            st.switch_page("Page_1.py")
    st.stop()

render_privacy_notice()

RATING_OPTIONS = ["Very Low", "Low", "Moderate", "High", "Very High"]
RATING_TO_SCORE = {"Very Low": 0.0, "Low": 2.5, "Moderate": 5.0, "High": 7.5, "Very High": 10.0}

def get_rating(key, default):
    val = st.session_state.get(key, default)
    return val if val in RATING_OPTIONS else default

with st.form("page2_form"):
    stress_level_category = st.selectbox(
        "How is your stress condition recently?",
        options=["Low", "Moderate", "High"],
        index=["Low", "Moderate", "High"].index(
            st.session_state.get("stress_level_category", "Moderate")
        ),
        help="Low = rarely stressed, Moderate = sometimes stressed, High = frequently stressed.",
    )

    st.markdown("---")

    exam_pressure = st.select_slider(
        "Exam pressure level",
        options=RATING_OPTIONS,
        value=get_rating("exam_pressure_rating", "High"),
        help="How much pressure do you feel from upcoming exams?",
    )

    family_expectation = st.select_slider(
        "Family expectation level",
        options=RATING_OPTIONS,
        value=get_rating("family_expectation_rating", "Moderate"),
        help="How much academic pressure do you feel from your family?",
    )

    financial_stress = st.select_slider(
        "Financial stress level",
        options=RATING_OPTIONS,
        value=get_rating("financial_stress_rating", "Low"),
        help="How worried are you about financial matters?",
    )

    social_support = st.select_slider(
        "Social support level",
        options=RATING_OPTIONS,
        value=get_rating("social_support_rating", "High"),
        help="How supported do you feel by friends, family, or peers?",
    )

    anxiety_score = st.select_slider(
        "Anxiety level",
        options=RATING_OPTIONS,
        value=get_rating("anxiety_score_rating", "Moderate"),
        help="How anxious do you feel on a daily basis?",
    )

    depression_score = st.select_slider(
        "Depression level",
        options=RATING_OPTIONS,
        value=get_rating("depression_score_rating", "Very Low"),
        help="How low or hopeless do you feel lately?",
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        submitted = st.form_submit_button(
            "Analyze! →", type="primary", use_container_width=True
        )

if submitted:
    st.session_state.stress_level_category = stress_level_category
    st.session_state.exam_pressure_rating = exam_pressure
    st.session_state.family_expectation_rating = family_expectation
    st.session_state.financial_stress_rating = financial_stress
    st.session_state.social_support_rating = social_support
    st.session_state.anxiety_score_rating = anxiety_score
    st.session_state.depression_score_rating = depression_score
    st.session_state.exam_pressure = RATING_TO_SCORE[exam_pressure]
    st.session_state.family_expectation = RATING_TO_SCORE[family_expectation]
    st.session_state.financial_stress = RATING_TO_SCORE[financial_stress]
    st.session_state.social_support = RATING_TO_SCORE[social_support]
    st.session_state.anxiety_score = RATING_TO_SCORE[anxiety_score]
    st.session_state.depression_score = RATING_TO_SCORE[depression_score]
    st.switch_page("pages/result.py")

# Back button outside form
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("← Back", use_container_width=True, type="secondary"):
        st.switch_page("Page_1.py")
