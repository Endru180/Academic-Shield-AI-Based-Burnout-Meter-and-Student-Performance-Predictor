import streamlit as st

from src.config import PAGE1_KEYS
from src.ui import inject_css, render_animated_header, render_progress_bar, render_privacy_notice

st.set_page_config(page_title="Academic Shield — Step 2", layout="centered", initial_sidebar_state="collapsed")
inject_css()

render_animated_header(
    "MEASURE YOUR BURNOUT & PREDICT YOUR GRADE",
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

    exam_pressure = st.slider(
        "Exam pressure level",
        min_value=0,
        max_value=10,
        value=int(st.session_state.get("exam_pressure", 5)),
        help="How much pressure do you feel from upcoming exams? 0 = none, 10 = extreme.",
    )

    family_expectation = st.slider(
        "Family expectation level",
        min_value=0,
        max_value=10,
        value=int(st.session_state.get("family_expectation", 5)),
        help="How much academic pressure do you feel from your family? 0 = none, 10 = extreme.",
    )

    financial_stress = st.slider(
        "Financial stress level",
        min_value=0,
        max_value=10,
        value=int(st.session_state.get("financial_stress", 5)),
        help="How worried are you about financial matters? 0 = not at all, 10 = extremely.",
    )

    social_support = st.slider(
        "Social support level",
        min_value=0,
        max_value=10,
        value=int(st.session_state.get("social_support", 5)),
        help="How supported do you feel by friends, family, or peers? 0 = none, 10 = fully supported.",
    )

    anxiety_score = st.slider(
        "Anxiety level",
        min_value=0,
        max_value=10,
        value=int(st.session_state.get("anxiety_score", 5)),
        help="How anxious do you feel on a daily basis? 0 = calm, 10 = extremely anxious.",
    )

    depression_score = st.slider(
        "Depression level",
        min_value=0,
        max_value=10,
        value=int(st.session_state.get("depression_score", 5)),
        help="How low or hopeless do you feel lately? 0 = not at all, 10 = severely.",
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        submitted = st.form_submit_button(
            "Analyze! →", type="primary", use_container_width=True
        )

if submitted:
    st.session_state.stress_level_category = stress_level_category
    st.session_state.exam_pressure = float(exam_pressure)
    st.session_state.family_expectation = float(family_expectation)
    st.session_state.financial_stress = float(financial_stress)
    st.session_state.social_support = float(social_support)
    st.session_state.anxiety_score = float(anxiety_score)
    st.session_state.depression_score = float(depression_score)
    st.switch_page("pages/result.py")

# Back button outside form
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("← Back", use_container_width=True, type="secondary"):
        st.switch_page("Page_1.py")
