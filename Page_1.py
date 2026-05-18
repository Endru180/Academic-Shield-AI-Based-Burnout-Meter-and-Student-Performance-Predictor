import streamlit as st

from src.ui import inject_css, render_animated_header, render_progress_bar

st.set_page_config(page_title="Academic Shield", layout="centered", initial_sidebar_state="collapsed")
inject_css()

render_animated_header(
    "MEASURE YOUR BURNOUT & PREDICT YOUR GRADE",
    "Chronic <b>burnout</b> reduces focus, memory, and motivation — directly lowering your GPA.<br>"
    "Track your daily habits to see where you stand.",
)

render_progress_bar(1, 2, "Lifestyle &amp; Habits")

with st.form("page1_form"):
    study_hours = st.slider(
        "How many hours do you study per day?",
        min_value=0.0,
        max_value=12.0,
        step=0.5,
        value=st.session_state.get("study_hours", 4.0),
        help="Average study hours per day including assignments and self-study.",
    )

    sleep_hours = st.slider(
        "How many hours do you sleep per day?",
        min_value=0.0,
        max_value=12.0,
        step=0.5,
        value=st.session_state.get("sleep_hours", 8.0),
        help="Average hours of sleep per night. Naps count too.",
    )

    eca_hours = st.slider(
        "Extracurricular activities (hours/day)?",
        min_value=0.0,
        max_value=8.0,
        step=0.5,
        value=st.session_state.get("eca_hours", 1.0),
        help="Time spent on clubs, organizations, or extracurricular activities per day.",
    )

    social_hours = st.slider(
        "How many hours do you socialize per day?",
        min_value=0.0,
        max_value=10.0,
        step=0.5,
        value=st.session_state.get("social_hours", 5.0),
        help="Time spent hanging out with friends or family per day.",
    )

    physical_hours = st.slider(
        "How many hours do you exercise per day?",
        min_value=0.0,
        max_value=8.0,
        step=0.5,
        value=st.session_state.get("physical_hours", 2.0),
        help="Time spent on exercise, sports, or any physical activity per day.",
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        submitted = st.form_submit_button(
            "Next →", type="primary", use_container_width=True
        )

if submitted:
    st.session_state.study_hours = study_hours
    st.session_state.sleep_hours = sleep_hours
    st.session_state.eca_hours = eca_hours
    st.session_state.social_hours = social_hours
    st.session_state.physical_hours = physical_hours
    st.switch_page("pages/Page_2.py")
