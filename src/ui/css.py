"""CSS injection — Claude-style warm palette."""

import streamlit as st


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

        body {
            background-color: #FAF6F1 !important;
        }
        .stApp {
            background-color: transparent !important;
        }

        /* Hide all Streamlit chrome + sidebar entirely */
        header[data-testid="stHeader"] { display: none !important; }
        [data-testid="stSidebar"] { display: none !important; }
        [data-testid="stSidebarCollapsedControl"] { display: none !important; }
        [data-testid="stSidebarCollapseButton"] { display: none !important; }
        [data-testid="stExpandSidebarButton"] { display: none !important; }
        section[data-testid="stSidebarContent"] { display: none !important; }

        /* Give the main container more breathing room */
        [data-testid="stMainBlockContainer"] {
            padding-top: 5rem !important;
            padding-bottom: 6rem !important;
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
        @keyframes drawBurnout {
            to { stroke-dashoffset: 0; }
        }

        /* ── Serif display headings ── */
        .display-title {
            font-family: 'Newsreader', Georgia, serif !important;
            font-size: 2.8rem;
            font-weight: 600;
            color: #2D2D2D;
            text-align: center;
            line-height: 1.25;
            letter-spacing: 0.02rem;
            margin-bottom: 24px;
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
            height: 12px;
            background: rgba(0,0,0,0.05);
            border-radius: 6px;
            overflow: hidden;
        }
        .prob-fill {
            height: 100%;
            border-radius: 6px;
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
