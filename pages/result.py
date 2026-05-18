import streamlit as st
import pandas as pd
import os

from src.config import ALL_INPUT_KEYS, COLORS, INSIGHTS, FEEDBACK_PATH
from src.models import load_models, predict_burnout, predict_gpa
from src.ui import (
    inject_css,
    render_animated_header,
    build_burnout_gauge,
    render_gpa_ring,
    render_probability_bars,
    render_divider,
    render_neural_background,
    render_insight_card_animated,
)

st.set_page_config(page_title="Academic Shield — Results", layout="centered")
inject_css()
render_neural_background()

# ---------------------------------------------------------------------------
# Validate inputs
# ---------------------------------------------------------------------------
if not all(key in st.session_state for key in ALL_INPUT_KEYS):
    st.warning("Please complete both forms first.")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("← Back to Start", use_container_width=True, type="secondary"):
            st.switch_page("Page_1.py")
    st.stop()

# ---------------------------------------------------------------------------
# Load models
# ---------------------------------------------------------------------------
models = load_models()
if models is None:
    st.error("Models failed to load. Please contact the administrator.")
    st.stop()

# ---------------------------------------------------------------------------
# Collect inputs + Run predictions
# ---------------------------------------------------------------------------
inputs = {key: st.session_state[key] for key in ALL_INPUT_KEYS}
burnout = predict_burnout(inputs, models)
gpa = predict_gpa(inputs, models)

# ---------------------------------------------------------------------------
# Page header
# ---------------------------------------------------------------------------
render_animated_header("Your Results")

# ---------------------------------------------------------------------------
# Results: Burnout gauge + GPA ring side by side
# ---------------------------------------------------------------------------
col_burnout, col_gpa = st.columns([3, 2])

with col_burnout:
    fig = build_burnout_gauge(burnout["score"], burnout["class_name"], burnout["class_id"])
    st.plotly_chart(fig, use_container_width=True)

with col_gpa:
    render_gpa_ring(gpa["gpa"], gpa["label"])

# ---------------------------------------------------------------------------
# Probability breakdown
# ---------------------------------------------------------------------------
render_divider()

st.markdown(
    """<p style="text-align: center; font-size: 0.8rem; letter-spacing: 2px;
               text-transform: uppercase; color: rgba(255,255,255,0.4); margin-bottom: 4px;">
        Classification Breakdown
    </p>""",
    unsafe_allow_html=True,
)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    render_probability_bars(burnout["probabilities"])

# ---------------------------------------------------------------------------
# Insight
# ---------------------------------------------------------------------------
render_divider()

insight_text = INSIGHTS.get(burnout["class_id"], INSIGHTS[0])
color_map = {0: COLORS["healthy"], 1: COLORS["mild"], 2: COLORS["burnout"]}
insight_color = color_map.get(burnout["class_id"], COLORS["healthy"])

render_insight_card_animated(insight_text, insight_color)

# ---------------------------------------------------------------------------
# Feedback
# ---------------------------------------------------------------------------
render_divider()

st.markdown(
    """<p style="text-align: center; font-size: 0.8rem; letter-spacing: 2px;
               text-transform: uppercase; color: rgba(255,255,255,0.4); margin-bottom: 4px;">
        Feedback
    </p>
    <p style="text-align: center; color: rgba(255,255,255,0.6); font-size: 0.9rem;
              margin-bottom: 16px;">
        Help us improve Academic Shield!
    </p>""",
    unsafe_allow_html=True,
)

with st.form("feedback_form"):
    rating = st.radio(
        "Rate your experience",
        options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
        horizontal=True,
    )
    comment = st.text_area("Any comments?", placeholder="Write your thoughts here...")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        feedback_submitted = st.form_submit_button(
            "Submit Feedback", type="primary", use_container_width=True
        )

if feedback_submitted:
    if rating is None:
        st.warning("Please give a star rating first!")
    else:
        os.makedirs("feedback", exist_ok=True)
        feedback_data = pd.DataFrame(
            [
                {
                    **inputs,
                    "burnout_score": burnout["score"],
                    "burnout_class": burnout["class_name"],
                    "predicted_gpa": gpa["gpa"],
                    "rating": rating.count("⭐"),
                    "comment": comment,
                }
            ]
        )
        file_exists = os.path.exists(FEEDBACK_PATH)
        feedback_data.to_csv(
            FEEDBACK_PATH, mode="a", header=not file_exists, index=False
        )
        st.success("Thank you for your feedback!")

# ---------------------------------------------------------------------------
# Navigation
# ---------------------------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("← Start Over", use_container_width=True):
        for key in ALL_INPUT_KEYS:
            st.session_state.pop(key, None)
        st.switch_page("Page_1.py")
