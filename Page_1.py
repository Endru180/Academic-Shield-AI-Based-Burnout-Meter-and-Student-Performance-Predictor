import streamlit as st

from src.ui import (
    inject_css,
    fix_page_title,
    render_animated_header,
    render_progress_bar,
    render_neural_background,
    render_hamburger_menu,
)

st.set_page_config(
    page_title="Academic Shield",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed",
)
inject_css()
fix_page_title()
render_neural_background()
render_hamburger_menu()

render_animated_header(
    "Measure Your Burnout & Predict Your Grade",
    "Chronic <b>burnout</b> reduces focus, memory, and motivation — directly lowering your GPA.<br>"
    "Track your daily habits to see where you stand.",
)

render_progress_bar(1, 2, "Lifestyle &amp; Habits")

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
    max_value=6.0,
    step=0.5,
    value=st.session_state.get("eca_hours", 1.0),
    help="Time spent on clubs, organizations, or extracurricular activities per day.",
)

social_hours = st.slider(
    "How many hours do you socialize per day?",
    min_value=0.0,
    max_value=9.0,
    step=0.5,
    value=st.session_state.get("social_hours", 3.0),
    help="Time spent hanging out with friends or family per day.",
)

physical_hours = st.slider(
    "How many hours do you exercise per day?",
    min_value=0.0,
    max_value=6.0,
    step=0.5,
    value=st.session_state.get("physical_hours", 2.0),
    help="Time spent on exercise, sports, or any physical activity per day.",
)

remaining = round(
    24.0 - study_hours - sleep_hours - eca_hours - social_hours - physical_hours, 1
)
st.markdown(
    f'<p style="text-align:center; color:#9B9B9B; font-size:0.85rem; margin-top:8px;">'
    f"{remaining}h unallocated of 24h</p>",
    unsafe_allow_html=True,
)
if remaining < 0:
    st.warning("Your total exceeds 24 hours. Please adjust your inputs.")
else:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Next →", type="primary", use_container_width=True):
            st.session_state.study_hours = study_hours
            st.session_state.sleep_hours = sleep_hours
            st.session_state.eca_hours = eca_hours
            st.session_state.social_hours = social_hours
            st.session_state.physical_hours = physical_hours
            st.switch_page("pages/Page_2.py")
