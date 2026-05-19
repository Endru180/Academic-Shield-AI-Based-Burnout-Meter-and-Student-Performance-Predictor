"""Plotly + SVG chart components."""

import streamlit as st
import plotly.graph_objects as go

from src.config import COLORS


def build_burnout_gauge(score: float, class_name: str, class_id: int) -> go.Figure:
    color_map = {0: COLORS["healthy"], 1: COLORS["mild"], 2: COLORS["burnout"]}
    label_color = color_map.get(class_id, COLORS["text"])

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            number={
                "suffix": "",
                "font": {"size": 40, "color": COLORS["text"], "family": "Newsreader"},
                "valueformat": ".0f",
            },
            gauge={
                "axis": {
                    "range": [0, 100],
                    "tickcolor": "#D0D0D0",
                    "dtick": 20,
                    "tickfont": {"color": "#9B9B9B", "size": 10},
                },
                "bar": {"color": COLORS["text"], "thickness": 0.2},
                "bgcolor": "#F0EBE4",
                "borderwidth": 0,
                "steps": [
                    {"range": [0, 40], "color": "rgba(74, 167, 133, 0.15)"},
                    {"range": [40, 70], "color": "rgba(212, 168, 67, 0.15)"},
                    {"range": [70, 100], "color": "rgba(199, 80, 80, 0.15)"},
                ],
                "threshold": {
                    "line": {"color": label_color, "width": 3},
                    "thickness": 0.85,
                    "value": score,
                },
            },
        )
    )

    fig.update_layout(
        height=300,
        margin=dict(l=30, r=30, t=50, b=60),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color=COLORS["text"],
        title={
            "text": "Burnout Level",
            "x": 0.5,
            "y": 0.98,
            "xanchor": "center",
            "font": {"size": 13, "color": "#9B9B9B", "family": "Newsreader"},
        },
        annotations=[
            {
                "text": f"<b>{class_name}</b>",
                "x": 0.5,
                "y": -0.12,
                "showarrow": False,
                "font": {"size": 18, "color": label_color, "family": "Newsreader"},
                "xanchor": "center",
                "yanchor": "bottom",
                "xref": "paper",
                "yref": "paper",
            }
        ],
    )
    return fig


def render_gpa_ring(gpa: float, label: str):
    pct = (gpa / 4.0) * 100
    circumference = 2 * 3.14159 * 54
    offset = circumference * (1 - pct / 100)

    if gpa >= 3.0:
        color = COLORS["healthy"]
    elif gpa >= 2.5:
        color = COLORS["mild"]
    else:
        color = COLORS["burnout"]

    st.markdown(
        f"""
        <div style="text-align: center; animation: fadeInUp 0.6s ease-out;">
            <p style="font-size: 0.7rem; font-weight: 600; letter-spacing: 2px;
                      text-transform: uppercase; color: #9B9B9B; margin-bottom: 16px;">
                Predicted GPA
            </p>
            <div style="position: relative; width: 140px; height: 140px; margin: 0 auto;">
                <svg width="140" height="140" viewBox="0 0 120 120" style="transform: rotate(-90deg);">
                    <circle cx="60" cy="60" r="54" fill="none"
                            stroke="rgba(0,0,0,0.07)" stroke-width="6"/>
                    <circle cx="60" cy="60" r="54" fill="none"
                            stroke="{color}" stroke-width="6"
                            stroke-linecap="round"
                            stroke-dasharray="{circumference}"
                            stroke-dashoffset="{offset}"
                            opacity="0.9">
                        <animate attributeName="stroke-dashoffset"
                                 from="{circumference}" to="{offset}" dur="1.4s"
                                 fill="freeze" calcMode="spline"
                                 keySplines="0.4 0 0.2 1"/>
                    </circle>
                </svg>
                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; line-height: 1.1;">
                    <span style="font-size: 2rem; font-weight: 700; color: {color}; display: block;">{gpa:.2f}</span>
                    <span style="font-size: 0.72rem; color: #9B9B9B; letter-spacing: 1px;">/ 4.0</span>
                </div>
            </div>
            <p style="font-size: 0.88rem; margin-top: 18px; color: #6B6B6B; font-style: italic;">
                {label}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_radar_chart(inputs: dict):
    stress_map = {"Low": 2.0, "Moderate": 5.0, "High": 8.0}

    categories = [
        "Study", "Sleep", "Exercise", "Social Life", "ECA",
        "Stress", "Exam Pressure", "Family Expect.", "Finance",
        "Social Support", "Anxiety", "Depression",
    ]
    values = [
        float(inputs.get("study_hours", 0)) * 10 / 12,
        float(inputs.get("sleep_hours", 0)) * 10 / 12,
        float(inputs.get("physical_hours", 0)) * 10 / 8,
        float(inputs.get("social_hours", 0)),
        float(inputs.get("eca_hours", 0)) * 10 / 8,
        stress_map.get(inputs.get("stress_level_category", "Moderate"), 5.0),
        float(inputs.get("exam_pressure", 0)),
        float(inputs.get("family_expectation", 0)),
        float(inputs.get("financial_stress", 0)),
        float(inputs.get("social_support", 0)),
        float(inputs.get("anxiety_score", 0)),
        float(inputs.get("depression_score", 0)),
    ]

    fig = go.Figure(go.Scatterpolar(
        r=values + [values[0]],
        theta=categories + [categories[0]],
        fill="toself",
        fillcolor="rgba(217,119,87,0.12)",
        line=dict(color="#D97757", width=2),
        marker=dict(color="#D97757", size=5),
        name="Your Profile",
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10],
                tickfont=dict(size=9, color="#9B9B9B", family="Newsreader"),
                gridcolor="rgba(0,0,0,0.06)",
                linecolor="rgba(0,0,0,0.06)",
                tickvals=[2, 4, 6, 8, 10],
            ),
            angularaxis=dict(
                tickfont=dict(size=11, color="#6B6B6B", family="Newsreader"),
                gridcolor="rgba(0,0,0,0.06)",
                linecolor="rgba(0,0,0,0.08)",
            ),
            bgcolor="rgba(255,255,255,0)",
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        height=400,
        margin=dict(l=70, r=70, t=20, b=20),
        font=dict(family="Newsreader", color="#2D2D2D"),
    )

    st.plotly_chart(fig, use_container_width=True)
