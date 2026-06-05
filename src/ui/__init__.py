"""Public API for src.ui — import anything from here, not from sub-modules."""

from src.ui.css import inject_css
from src.ui.background import render_neural_background
from src.ui.charts import build_burnout_gauge, render_gpa_ring, render_radar_chart
from src.ui.components import (
    render_animated_header,
    render_progress_bar,
    render_privacy_notice,
    render_probability_bars,
    render_insight_card_animated,
    render_divider,
    render_hamburger_menu,
)

__all__ = [
    "inject_css",
    "render_neural_background",
    "build_burnout_gauge",
    "render_gpa_ring",
    "render_radar_chart",
    "render_animated_header",
    "render_progress_bar",
    "render_privacy_notice",
    "render_probability_bars",
    "render_insight_card_animated",
    "render_divider",
    "render_hamburger_menu",
]
