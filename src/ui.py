"""Shared UI — Claude-style warm, elegant design."""

import streamlit as st
import plotly.graph_objects as go

from src.config import COLORS


def inject_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400&family=Instrument+Serif&display=swap');

        * { font-family: 'Newsreader', Georgia, serif !important; }
        [data-testid="stIconMaterial"] span,
        [data-testid="stIconMaterial"] span span {
            font-family: 'Material Symbols Rounded' !important;
        }

        .stApp {
            background-color: #FAF6F1;
        }

        /* Hide all Streamlit chrome */
        header[data-testid="stHeader"] { display: none !important; }
        [data-testid="stSidebarCollapsedControl"] { display: none !important; }
        [data-testid="stSidebarCollapseButton"] { visibility: hidden !important; height: 0 !important; overflow: hidden !important; }

        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #FAF6F1 !important;
            border-right: 1px solid rgba(0,0,0,0.06) !important;
        }
        [data-testid="stSidebar"] [data-testid="stSidebarNavItems"] a {
            color: #2D2D2D !important;
            font-weight: 500 !important;
            font-family: 'Newsreader', Georgia, serif !important;
        }
        [data-testid="stSidebar"] [data-testid="stSidebarNavItems"] a:hover {
            background-color: rgba(217, 119, 87, 0.08) !important;
        }

        /* Ensure sidebar toggle iframe doesn't take space */
        iframe[title="streamlit_html.iframe"] {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            width: 72px !important;
            height: 72px !important;
            border: none !important;
            z-index: 999998 !important;
            pointer-events: auto !important;
            background: transparent !important;
        }

        /* ── Animations ── */
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(16px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to   { opacity: 1; }
        }
        @keyframes gentlePulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.02); }
        }
        @keyframes slideIn {
            from { opacity: 0; transform: translateX(-12px); }
            to   { opacity: 1; transform: translateX(0); }
        }
        @keyframes breathe {
            0%, 100% { opacity: 0.7; }
            50% { opacity: 1; }
        }

        /* ── Serif display headings ── */
        .display-title {
            font-family: 'Instrument Serif', Georgia, serif !important;
            font-size: 2.6rem;
            font-weight: 400;
            color: #2D2D2D;
            text-align: center;
            line-height: 1.15;
            margin-bottom: 4px;
            animation: fadeInUp 0.6s ease-out;
        }

        /* ── Warm card ── */
        .warm-card {
            background: #FFFFFF;
            border: 1px solid rgba(0,0,0,0.06);
            border-radius: 16px;
            padding: 28px 32px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04), 0 4px 12px rgba(0,0,0,0.03);
            animation: fadeInUp 0.5s ease-out;
        }

        /* ── Slider ── */
        .stSlider > div > div > div > div {
            background: linear-gradient(90deg, #D97757, #E8956F) !important;
        }
        .stSlider label p {
            font-size: 0.95rem !important;
            font-weight: 500 !important;
            color: #2D2D2D !important;
        }

        .stSelectbox label p {
            font-size: 0.95rem !important;
            font-weight: 500 !important;
            color: #2D2D2D !important;
        }

        label[data-testid="stWidgetLabel"] p {
            font-size: 0.95rem !important;
            font-weight: 500 !important;
            color: #2D2D2D !important;
        }

        /* ── Form ── */
        [data-testid="stForm"] {
            border: none !important;
            padding: 0 !important;
            box-shadow: none !important;
            background-color: transparent !important;
        }

        /* ── Primary button — terracotta ── */
        [data-testid="stFormSubmitButton"] {
            display: flex;
            justify-content: center;
            margin-top: 24px;
        }
        [data-testid="stFormSubmitButton"] button {
            border-radius: 12px !important;
            background-color: #D97757 !important;
            border: none !important;
            padding: 10px 36px !important;
            transition: all 0.25s ease !important;
            box-shadow: 0 2px 8px rgba(217, 119, 87, 0.25) !important;
        }
        [data-testid="stFormSubmitButton"] button:hover {
            background-color: #C4684A !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 4px 16px rgba(217, 119, 87, 0.35) !important;
        }
        [data-testid="stFormSubmitButton"] button p {
            font-weight: 600 !important;
            font-size: 1rem !important;
            color: white !important;
        }

        /* ── Secondary button ── */
        [data-testid="stBaseButton-secondary"] {
            border-radius: 12px !important;
            background-color: transparent !important;
            border: 1px solid rgba(0,0,0,0.12) !important;
            width: 100% !important;
            transition: all 0.25s ease !important;
        }
        [data-testid="stBaseButton-secondary"] p {
            font-weight: 500 !important;
            font-size: 0.95rem !important;
            color: #6B6B6B !important;
        }
        [data-testid="stBaseButton-secondary"]:hover {
            background-color: rgba(0,0,0,0.03) !important;
            border-color: rgba(0,0,0,0.2) !important;
        }

        /* ── Regular button ── */
        .stButton > button {
            border-radius: 12px !important;
            background-color: #D97757 !important;
            border: none !important;
            transition: all 0.25s ease !important;
            box-shadow: 0 2px 8px rgba(217, 119, 87, 0.2) !important;
        }
        .stButton > button:hover {
            background-color: #C4684A !important;
            transform: translateY(-1px) !important;
        }
        .stButton > button p {
            font-weight: 600 !important;
            color: white !important;
        }

        /* ── Radio ── */
        [data-testid="stRadio"] > div {
            justify-content: center !important;
        }

        /* ── Divider ── */
        .warm-divider {
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(0,0,0,0.08), transparent);
            margin: 28px 0;
        }

        /* ── Metric card ── */
        .metric-card {
            background: #FFFFFF;
            border: 1px solid rgba(0,0,0,0.06);
            border-radius: 16px;
            padding: 28px;
            text-align: center;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04), 0 4px 12px rgba(0,0,0,0.03);
            animation: fadeInUp 0.6s ease-out;
        }

        /* ── Insight card ── */
        .insight-card {
            background: #FFFFFF;
            border: 1px solid rgba(0,0,0,0.06);
            border-left: 4px solid;
            border-radius: 12px;
            padding: 20px 24px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
            animation: slideIn 0.6s ease-out;
            transition: all 0.2s ease;
        }
        .insight-card:hover {
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }

        /* ── Probability bars ── */
        .prob-track {
            height: 6px;
            background: rgba(0,0,0,0.05);
            border-radius: 3px;
            overflow: hidden;
        }
        .prob-fill {
            height: 100%;
            border-radius: 3px;
            transition: width 1.2s ease-out;
        }

        /* ── Step pill — sans-serif for UI elements ── */
        .step-pill {
            display: inline-block;
            background: rgba(217, 119, 87, 0.08);
            color: #D97757;
            font-family: 'Newsreader', Georgia, serif !important;
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            padding: 6px 20px;
            border-radius: 50px;
            border: 1px solid rgba(217, 119, 87, 0.15);
        }

        /* ── Progress bar ── */
        .progress-track {
            width: 160px;
            height: 3px;
            background: rgba(0,0,0,0.06);
            border-radius: 3px;
            margin: 10px auto 0;
            overflow: hidden;
        }
        .progress-fill {
            height: 100%;
            background: #D97757;
            border-radius: 3px;
            transition: width 0.6s ease;
        }

        /* ── Privacy notice ── */
        .privacy-notice {
            background: rgba(217, 119, 87, 0.06);
            border: 1px solid rgba(217, 119, 87, 0.12);
            border-left: 3px solid #D97757;
            padding: 14px 18px;
            border-radius: 10px;
            margin-bottom: 24px;
            font-size: 0.85rem;
            color: #6B6B6B;
            animation: fadeIn 0.5s ease-out;
        }

        /* ── Section label ── */
        .section-label {
            text-align: center;
            font-size: 0.7rem;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: #9B9B9B;
            font-weight: 600;
            margin-bottom: 6px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.html(
        """
        <div id="sidebarToggle" style="
            position: fixed; top: 16px; left: 16px; z-index: 999999;
            width: 40px; height: 40px; border-radius: 10px;
            background: #FFFFFF; border: 1px solid rgba(0,0,0,0.08);
            box-shadow: 0 1px 4px rgba(0,0,0,0.06);
            cursor: pointer; display: flex; align-items: center; justify-content: center;
            transition: all 0.2s ease;
        " title="Navigate pages">
            <svg width="20" height="22" viewBox="0 0 64 72" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M32 2L4 16V36C4 52 16 66 32 70C48 66 60 52 60 36V16L32 2Z"
                      fill="#D97757" opacity="0.25"/>
                <path d="M32 2L4 16V36C4 52 16 66 32 70C48 66 60 52 60 36V16L32 2Z"
                      fill="none" stroke="#D97757" stroke-width="3" opacity="0.6"/>
            </svg>
        </div>
        <script>
        document.getElementById('sidebarToggle').addEventListener('click', function() {
            const doc = window.parent.document;
            const collapse = doc.querySelector('[data-testid="stSidebarCollapseButton"]');
            const expand = doc.querySelector('button[data-testid="stExpandSidebarButton"]') ||
                           doc.querySelector('[data-testid="stSidebarCollapsedControl"] button');
            if (collapse) { collapse.click(); }
            else if (expand) { expand.click(); }
        });
        document.getElementById('sidebarToggle').addEventListener('mouseenter', function() {
            this.style.boxShadow = '0 2px 8px rgba(0,0,0,0.12)';
            this.style.transform = 'scale(1.05)';
        });
        document.getElementById('sidebarToggle').addEventListener('mouseleave', function() {
            this.style.boxShadow = '0 1px 4px rgba(0,0,0,0.06)';
            this.style.transform = 'scale(1)';
        });
        </script>
        """
    )


# ---------------------------------------------------------------------------
# Shield logo — warm terracotta SVG
# ---------------------------------------------------------------------------

def render_shield_logo():
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 12px; animation: fadeIn 0.8s ease-out;">
            <svg width="52" height="60" viewBox="0 0 64 72" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M32 2L4 16V36C4 52 16 66 32 70C48 66 60 52 60 36V16L32 2Z"
                      fill="#D97757" opacity="0.12"/>
                <path d="M32 2L4 16V36C4 52 16 66 32 70C48 66 60 52 60 36V16L32 2Z"
                      fill="none" stroke="#D97757" stroke-width="2" opacity="0.4"/>
                <path d="M32 8L10 20V36C10 49 20 61 32 64C44 61 54 49 54 36V20L32 8Z"
                      fill="none" stroke="#D97757" stroke-width="1" opacity="0.15"/>
                <path d="M28 38L22 32L20 34L28 42L44 26L42 24L28 38Z"
                      fill="#D97757" opacity="0.7"/>
            </svg>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Animated header — serif title
# ---------------------------------------------------------------------------

def render_animated_header(title: str, subtitle: str = ""):
    render_shield_logo()
    st.markdown(
        f'<h1 class="display-title">{title}</h1>',
        unsafe_allow_html=True,
    )
    if subtitle:
        st.markdown(
            f"""<p style="text-align: center; color: #6B6B6B; font-size: 0.92rem;
                          line-height: 1.65; margin-bottom: 12px; animation: fadeIn 0.7s ease-out;">
                {subtitle}
            </p>""",
            unsafe_allow_html=True,
        )


# ---------------------------------------------------------------------------
# Step indicator — pill + progress bar
# ---------------------------------------------------------------------------

def render_progress_bar(current: int, total: int, label: str = ""):
    pct = int((current / total) * 100)
    text = f"Step {current} of {total}"
    if label:
        text += f" &mdash; {label}"

    st.markdown(
        f"""
        <div style="text-align: center; margin-bottom: 24px; animation: fadeIn 0.5s ease-out;">
            <span class="step-pill">{text}</span>
            <div class="progress-track">
                <div class="progress-fill" style="width: {pct}%;"></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Burnout gauge — warm theme
# ---------------------------------------------------------------------------

def build_burnout_gauge(score: float, class_name: str, class_id: int) -> go.Figure:
    color_map = {0: COLORS["healthy"], 1: COLORS["mild"], 2: COLORS["burnout"]}
    label_color = color_map.get(class_id, COLORS["text"])

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            number={"suffix": "", "font": {"size": 44, "color": COLORS["text"], "family": "Inter"}},
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
        height=280,
        margin=dict(l=30, r=30, t=60, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color=COLORS["text"],
        title={
            "text": "Burnout Level",
            "x": 0.5,
            "y": 0.97,
            "xanchor": "center",
            "font": {"size": 14, "color": "#9B9B9B", "family": "Inter"},
        },
        annotations=[
            {
                "text": f"<b>{class_name}</b>",
                "x": 0.5,
                "y": 0.22,
                "showarrow": False,
                "font": {"size": 20, "color": label_color, "family": "Inter"},
                "xanchor": "center",
            }
        ],
    )
    return fig


# ---------------------------------------------------------------------------
# GPA ring — SVG
# ---------------------------------------------------------------------------

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
        <div class="metric-card">
            <p style="font-size: 0.7rem; font-weight: 600; letter-spacing: 2px;
                      text-transform: uppercase; color: #9B9B9B; margin-bottom: 16px;">
                Predicted GPA
            </p>
            <div style="position: relative; width: 130px; height: 130px; margin: 0 auto;">
                <svg width="130" height="130" viewBox="0 0 120 120" style="transform: rotate(-90deg);">
                    <circle cx="60" cy="60" r="54" fill="none"
                            stroke="#F0EBE4" stroke-width="7"/>
                    <circle cx="60" cy="60" r="54" fill="none"
                            stroke="{color}" stroke-width="7"
                            stroke-linecap="round"
                            stroke-dasharray="{circumference}"
                            stroke-dashoffset="{offset}"
                            opacity="0.8">
                        <animate attributeName="stroke-dashoffset"
                                 from="{circumference}" to="{offset}" dur="1.2s"
                                 fill="freeze" calcMode="spline"
                                 keySplines="0.4 0 0.2 1"/>
                    </circle>
                </svg>
                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center;">
                    <span style="font-size: 1.8rem; font-weight: 700; color: {color};">{gpa:.2f}</span>
                    <span style="font-size: 0.75rem; color: #9B9B9B;">/4.0</span>
                </div>
            </div>
            <p style="font-size: 0.9rem; margin-top: 14px; color: #6B6B6B; font-style: italic;">
                {label}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Probability bars
# ---------------------------------------------------------------------------

def render_probability_bars(probabilities: list):
    labels = ["Healthy", "Mildly Burnout", "Burnout"]
    colors = [COLORS["healthy"], COLORS["mild"], COLORS["burnout"]]

    html = '<div style="animation: fadeInUp 0.7s ease-out;">'
    for lbl, prob, clr in zip(labels, probabilities, colors):
        pct = prob * 100
        html += (
            f'<div style="margin-bottom: 12px;">'
            f'<div style="display: flex; justify-content: space-between; font-size: 0.8rem; margin-bottom: 4px;">'
            f'<span style="color: #6B6B6B;">{lbl}</span>'
            f'<span style="color: {clr}; font-weight: 600;">{pct:.1f}%</span>'
            f'</div>'
            f'<div class="prob-track">'
            f'<div class="prob-fill" style="width: {pct}%; background: {clr}; opacity: 0.75;"></div>'
            f'</div>'
            f'</div>'
        )
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Privacy notice
# ---------------------------------------------------------------------------

def render_privacy_notice():
    st.markdown(
        """
        <div class="privacy-notice">
            <b>Privacy Notice:</b> Your responses below are sensitive in nature.
            All inputs are used solely for prediction and are <b>never stored or shared</b>.
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Divider
# ---------------------------------------------------------------------------

def render_divider():
    st.markdown('<div class="warm-divider"></div>', unsafe_allow_html=True)
