import streamlit as st


def render_nav():
    st.markdown(
        """
        <style>
        /* Hide default sidebar and nav */
        [data-testid="stSidebarNav"]   { display: none !important; }
        section[data-testid="stSidebar"] { display: none !important; }
        [data-testid="collapsedControl"] { display: none !important; }

        /* Hamburger wrapper — fixed top-right */
        .hb-menu {
            position: fixed;
            top: 1rem;
            right: 1rem;
            z-index: 9999;
        }

        /* Hide the checkbox */
        .hb-toggle {
            display: none;
        }

        /* The three-line icon */
        .hb-icon {
            cursor: pointer;
            display: flex;
            flex-direction: column;
            justify-content: center;
            gap: 5px;
            padding: 10px 12px;
            background: rgba(0, 15, 35, 0.85);
            border: 1px solid rgba(0, 212, 255, 0.3);
            border-radius: 10px;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            box-shadow: 0 0 12px rgba(0, 212, 255, 0.1);
            transition: background 0.25s, border-color 0.25s, box-shadow 0.25s;
        }

        .hb-icon:hover {
            background: rgba(0, 212, 255, 0.12);
            border-color: rgba(0, 212, 255, 0.65);
            box-shadow: 0 0 20px rgba(0, 212, 255, 0.3);
        }

        .hb-icon span {
            display: block;
            width: 22px;
            height: 2px;
            background: #00d4ff;
            border-radius: 2px;
            transition: all 0.3s;
        }

        /* Animate to X when open */
        .hb-toggle:checked + .hb-icon span:nth-child(1) {
            transform: translateY(7px) rotate(45deg);
        }
        .hb-toggle:checked + .hb-icon span:nth-child(2) {
            opacity: 0;
        }
        .hb-toggle:checked + .hb-icon span:nth-child(3) {
            transform: translateY(-7px) rotate(-45deg);
        }

        /* Dropdown */
        .hb-dropdown {
            display: none;
            position: absolute;
            right: 0;
            top: calc(100% + 8px);
            background: rgba(1, 8, 18, 0.97);
            border: 1px solid rgba(0, 212, 255, 0.2);
            border-radius: 14px;
            padding: 0.5rem;
            min-width: 190px;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.8), 0 0 20px rgba(0, 212, 255, 0.08);
        }

        .hb-toggle:checked ~ .hb-dropdown {
            display: block;
        }

        .hb-dropdown a {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 0.65rem 1rem;
            color: rgba(255, 255, 255, 0.85);
            text-decoration: none;
            border-radius: 8px;
            font-size: 0.95rem;
            font-weight: 500;
            transition: background 0.15s, color 0.15s;
        }

        .hb-dropdown a:hover {
            background: rgba(0, 212, 255, 0.12);
            color: #00d4ff;
        }

        .hb-dropdown hr {
            border: none;
            border-top: 1px solid rgba(0, 212, 255, 0.1);
            margin: 0.3rem 0.5rem;
        }

        /* Stepper button base */
        [data-baseweb="input-container"] button {
            background: rgba(0, 10, 25, 0.8) !important;
            border: 1px solid rgba(0, 212, 255, 0.3) !important;
            border-radius: 6px !important;
            color: #00d4ff !important;
            font-size: 1.1rem !important;
            font-weight: 700 !important;
            width: 32px !important;
            height: 32px !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            transition: background 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease !important;
            cursor: pointer !important;
        }

        /* Stepper button hover */
        [data-baseweb="input-container"] button:hover {
            background: rgba(0, 212, 255, 0.12) !important;
            border-color: rgba(0, 212, 255, 0.7) !important;
            box-shadow: 0 0 10px rgba(0, 212, 255, 0.3) !important;
        }

        /* Stepper button active/press */
        [data-baseweb="input-container"] button:active {
            background: rgba(0, 212, 255, 0.22) !important;
            box-shadow: 0 0 16px rgba(0, 212, 255, 0.5) !important;
        }

        /* Stepper button SVG icons — make them cyan */
        [data-baseweb="input-container"] button svg {
            fill: #00d4ff !important;
            stroke: #00d4ff !important;
        }

        /* Alternating wave curve background lines with shimmer */
        .stApp::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 0;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 900' preserveAspectRatio='xMidYMid slice'%3E%3Cdefs%3E%3Cfilter id='glow' x='-50%25' y='-50%25' width='200%25' height='200%25'%3E%3CfeGaussianBlur stdDeviation='3.5' result='blur'/%3E%3CfeMerge%3E%3CfeMergeNode in='blur'/%3E%3CfeMergeNode in='SourceGraphic'/%3E%3C/feMerge%3E%3C/filter%3E%3C/defs%3E%3Cpath d='M -10,0 C 200,500 1200,400 1450,900' fill='none' stroke='rgba(0,212,255,0.50)' stroke-width='2.5' filter='url(%23glow)'/%3E%3Cpath d='M -10,150 C 300,600 1100,300 1450,750' fill='none' stroke='rgba(0,212,255,0.35)' stroke-width='2' filter='url(%23glow)'/%3E%3Cpath d='M -10,-50 C 150,450 1300,500 1450,1000' fill='none' stroke='rgba(0,212,255,0.25)' stroke-width='2'/%3E%3Cpath d='M 200,-10 C 500,400 1000,500 1450,850' fill='none' stroke='rgba(0,212,255,0.15)' stroke-width='1.5'/%3E%3Cpath d='M -10,0 C 200,500 1200,400 1450,900' fill='none' stroke='white' stroke-width='2.5' stroke-dasharray='150 1500'%3E%3Canimate attributeName='stroke-dashoffset' from='1200' to='-1200' dur='4s' repeatCount='indefinite' begin='0s'/%3E%3C/path%3E%3Cpath d='M -10,150 C 300,600 1100,300 1450,750' fill='none' stroke='white' stroke-width='2' stroke-dasharray='150 1500'%3E%3Canimate attributeName='stroke-dashoffset' from='1200' to='-1200' dur='4s' repeatCount='indefinite' begin='1s'/%3E%3C/path%3E%3Cpath d='M -10,-50 C 150,450 1300,500 1450,1000' fill='none' stroke='white' stroke-width='2' stroke-dasharray='150 1500'%3E%3Canimate attributeName='stroke-dashoffset' from='1200' to='-1200' dur='4s' repeatCount='indefinite' begin='2s'/%3E%3C/path%3E%3Cpath d='M 200,-10 C 500,400 1000,500 1450,850' fill='none' stroke='white' stroke-width='1.5' stroke-dasharray='150 1500'%3E%3Canimate attributeName='stroke-dashoffset' from='1200' to='-1200' dur='4s' repeatCount='indefinite' begin='3s'/%3E%3C/path%3E%3C/svg%3E");
            background-size: 100% 100%;
            background-repeat: no-repeat;
        }
        </style>

        <div class="hb-menu">
            <input type="checkbox" id="hb-toggle" class="hb-toggle">
            <label for="hb-toggle" class="hb-icon">
                <span></span>
                <span></span>
                <span></span>
            </label>
            <div class="hb-dropdown">
                <a href="/">🏠 Home</a>
                <hr>
                <a href="/Tips">💡 Tips</a>
                <a href="/About">ℹ️ About</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
