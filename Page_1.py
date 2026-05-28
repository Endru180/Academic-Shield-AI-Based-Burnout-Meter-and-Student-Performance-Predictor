import streamlit as st

from src.ui import inject_css, render_animated_header, render_progress_bar, render_neural_background, render_hamburger_menu

st.set_page_config(page_title="Academic Shield", layout="centered", initial_sidebar_state="collapsed")
inject_css()
render_neural_background()
render_hamburger_menu()

render_animated_header(
    "Measure Your Burnout & Predict Your Grade",
    "Chronic <b>burnout</b> reduces focus, memory, and motivation — directly lowering your GPA.<br>"
    "Track your daily habits to see where you stand.",
)

render_progress_bar(1, 2, "Lifestyle &amp; Habits")

_study    = st.session_state.get("study_hours",    4.0)
_sleep    = st.session_state.get("sleep_hours",    8.0)
_eca      = st.session_state.get("eca_hours",      1.0)
_social   = st.session_state.get("social_hours",   3.0)
_physical = st.session_state.get("physical_hours", 2.0)

study_max = max(0.0, round(24.0 - _sleep - _eca - _social - _physical, 1))
study_hours = st.slider(
    "How many hours do you study per day?",
    min_value=0.0,
    max_value=max(study_max, 0.5),
    step=0.5,
    value=min(_study, study_max) if study_max >= 0.5 else 0.0,
    help="Average study hours per day including assignments and self-study.",
)

sleep_max = max(0.0, round(24.0 - study_hours - _eca - _social - _physical, 1))
sleep_hours = st.slider(
    "How many hours do you sleep per day?",
    min_value=0.0,
    max_value=max(sleep_max, 0.5),
    step=0.5,
    value=min(_sleep, sleep_max) if sleep_max >= 0.5 else 0.0,
    help="Average hours of sleep per night. Naps count too.",
)

eca_max = max(0.0, round(24.0 - study_hours - sleep_hours - _social - _physical, 1))
eca_hours = st.slider(
    "Extracurricular activities (hours/day)?",
    min_value=0.0,
    max_value=max(eca_max, 0.5),
    step=0.5,
    value=min(_eca, eca_max) if eca_max >= 0.5 else 0.0,
    help="Time spent on clubs, organizations, or extracurricular activities per day.",
)

social_max = max(0.0, round(24.0 - study_hours - sleep_hours - eca_hours - _physical, 1))
social_hours = st.slider(
    "How many hours do you socialize per day?",
    min_value=0.0,
    max_value=max(social_max, 0.5),
    step=0.5,
    value=min(_social, social_max) if social_max >= 0.5 else 0.0,
    help="Time spent hanging out with friends or family per day.",
)

physical_max = max(0.0, round(24.0 - study_hours - sleep_hours - eca_hours - social_hours, 1))
physical_hours = st.slider(
    "How many hours do you exercise per day?",
    min_value=0.0,
    max_value=max(physical_max, 0.5),
    step=0.5,
    value=min(_physical, physical_max) if physical_max >= 0.5 else 0.0,
    help="Time spent on exercise, sports, or any physical activity per day.",
)

remaining = round(24.0 - study_hours - sleep_hours - eca_hours - social_hours - physical_hours, 1)
st.markdown(
    f'<p style="text-align:center; color:#9B9B9B; font-size:0.85rem; margin-top:8px;">'
    f'{remaining}h unallocated of 24h</p>',
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Next →", type="primary", use_container_width=True):
        st.session_state.study_hours    = study_hours
        st.session_state.sleep_hours    = sleep_hours
        st.session_state.eca_hours      = eca_hours
        st.session_state.social_hours   = social_hours
        st.session_state.physical_hours = physical_hours
        st.switch_page("pages/Page_2.py")
