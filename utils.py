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

        /* Floating particles */
        .stApp::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 0;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 900'%3E%3Ccircle cx='80' cy='800' r='4' fill='rgba(0,212,255,0.8)'%3E%3Canimate attributeName='cy' from='800' to='-20' dur='9s' repeatCount='indefinite' begin='0s'/%3E%3Canimate attributeName='opacity' values='0;0.85;0' dur='9s' repeatCount='indefinite' begin='0s'/%3E%3C/circle%3E%3Ccircle cx='200' cy='850' r='3' fill='rgba(0,212,255,0.75)'%3E%3Canimate attributeName='cy' from='850' to='-20' dur='11s' repeatCount='indefinite' begin='1.5s'/%3E%3Canimate attributeName='opacity' values='0;0.8;0' dur='11s' repeatCount='indefinite' begin='1.5s'/%3E%3C/circle%3E%3Ccircle cx='340' cy='820' r='5' fill='rgba(0,212,255,0.65)'%3E%3Canimate attributeName='cy' from='820' to='-20' dur='13s' repeatCount='indefinite' begin='3s'/%3E%3Canimate attributeName='opacity' values='0;0.7;0' dur='13s' repeatCount='indefinite' begin='3s'/%3E%3C/circle%3E%3Ccircle cx='480' cy='870' r='3' fill='rgba(0,212,255,0.8)'%3E%3Canimate attributeName='cy' from='870' to='-20' dur='8s' repeatCount='indefinite' begin='0.5s'/%3E%3Canimate attributeName='opacity' values='0;0.85;0' dur='8s' repeatCount='indefinite' begin='0.5s'/%3E%3C/circle%3E%3Ccircle cx='620' cy='810' r='4' fill='rgba(0,212,255,0.7)'%3E%3Canimate attributeName='cy' from='810' to='-20' dur='10s' repeatCount='indefinite' begin='2s'/%3E%3Canimate attributeName='opacity' values='0;0.75;0' dur='10s' repeatCount='indefinite' begin='2s'/%3E%3C/circle%3E%3Ccircle cx='760' cy='860' r='3' fill='rgba(0,212,255,0.75)'%3E%3Canimate attributeName='cy' from='860' to='-20' dur='12s' repeatCount='indefinite' begin='4s'/%3E%3Canimate attributeName='opacity' values='0;0.8;0' dur='12s' repeatCount='indefinite' begin='4s'/%3E%3C/circle%3E%3Ccircle cx='900' cy='830' r='5' fill='rgba(0,212,255,0.65)'%3E%3Canimate attributeName='cy' from='830' to='-20' dur='9.5s' repeatCount='indefinite' begin='1s'/%3E%3Canimate attributeName='opacity' values='0;0.7;0' dur='9.5s' repeatCount='indefinite' begin='1s'/%3E%3C/circle%3E%3Ccircle cx='1040' cy='880' r='3' fill='rgba(0,212,255,0.8)'%3E%3Canimate attributeName='cy' from='880' to='-20' dur='7.5s' repeatCount='indefinite' begin='2.5s'/%3E%3Canimate attributeName='opacity' values='0;0.85;0' dur='7.5s' repeatCount='indefinite' begin='2.5s'/%3E%3C/circle%3E%3Ccircle cx='1180' cy='840' r='4' fill='rgba(0,212,255,0.7)'%3E%3Canimate attributeName='cy' from='840' to='-20' dur='11.5s' repeatCount='indefinite' begin='3.5s'/%3E%3Canimate attributeName='opacity' values='0;0.75;0' dur='11.5s' repeatCount='indefinite' begin='3.5s'/%3E%3C/circle%3E%3Ccircle cx='1320' cy='800' r='3' fill='rgba(0,212,255,0.75)'%3E%3Canimate attributeName='cy' from='800' to='-20' dur='10.5s' repeatCount='indefinite' begin='5s'/%3E%3Canimate attributeName='opacity' values='0;0.8;0' dur='10.5s' repeatCount='indefinite' begin='5s'/%3E%3C/circle%3E%3Ccircle cx='140' cy='900' r='6' fill='rgba(0,212,255,0.55)'%3E%3Canimate attributeName='cy' from='900' to='-20' dur='14s' repeatCount='indefinite' begin='6s'/%3E%3Canimate attributeName='opacity' values='0;0.65;0' dur='14s' repeatCount='indefinite' begin='6s'/%3E%3C/circle%3E%3Ccircle cx='280' cy='780' r='3' fill='rgba(0,212,255,0.8)'%3E%3Canimate attributeName='cy' from='780' to='-20' dur='8.5s' repeatCount='indefinite' begin='0.8s'/%3E%3Canimate attributeName='opacity' values='0;0.85;0' dur='8.5s' repeatCount='indefinite' begin='0.8s'/%3E%3C/circle%3E%3Ccircle cx='420' cy='860' r='4' fill='rgba(0,212,255,0.7)'%3E%3Canimate attributeName='cy' from='860' to='-20' dur='12.5s' repeatCount='indefinite' begin='4.5s'/%3E%3Canimate attributeName='opacity' values='0;0.75;0' dur='12.5s' repeatCount='indefinite' begin='4.5s'/%3E%3C/circle%3E%3Ccircle cx='560' cy='820' r='3' fill='rgba(0,212,255,0.75)'%3E%3Canimate attributeName='cy' from='820' to='-20' dur='9s' repeatCount='indefinite' begin='7s'/%3E%3Canimate attributeName='opacity' values='0;0.8;0' dur='9s' repeatCount='indefinite' begin='7s'/%3E%3C/circle%3E%3Ccircle cx='700' cy='890' r='5' fill='rgba(0,212,255,0.6)'%3E%3Canimate attributeName='cy' from='890' to='-20' dur='11s' repeatCount='indefinite' begin='2.2s'/%3E%3Canimate attributeName='opacity' values='0;0.7;0' dur='11s' repeatCount='indefinite' begin='2.2s'/%3E%3C/circle%3E%3Ccircle cx='840' cy='760' r='3' fill='rgba(0,212,255,0.8)'%3E%3Canimate attributeName='cy' from='760' to='-20' dur='7s' repeatCount='indefinite' begin='3.8s'/%3E%3Canimate attributeName='opacity' values='0;0.85;0' dur='7s' repeatCount='indefinite' begin='3.8s'/%3E%3C/circle%3E%3Ccircle cx='980' cy='845' r='6' fill='rgba(0,212,255,0.55)'%3E%3Canimate attributeName='cy' from='845' to='-20' dur='13.5s' repeatCount='indefinite' begin='1.2s'/%3E%3Canimate attributeName='opacity' values='0;0.65;0' dur='13.5s' repeatCount='indefinite' begin='1.2s'/%3E%3C/circle%3E%3Ccircle cx='1120' cy='800' r='3' fill='rgba(0,212,255,0.75)'%3E%3Canimate attributeName='cy' from='800' to='-20' dur='10s' repeatCount='indefinite' begin='5.5s'/%3E%3Canimate attributeName='opacity' values='0;0.8;0' dur='10s' repeatCount='indefinite' begin='5.5s'/%3E%3C/circle%3E%3Ccircle cx='1260' cy='870' r='4' fill='rgba(0,212,255,0.7)'%3E%3Canimate attributeName='cy' from='870' to='-20' dur='8s' repeatCount='indefinite' begin='6.5s'/%3E%3Canimate attributeName='opacity' values='0;0.75;0' dur='8s' repeatCount='indefinite' begin='6.5s'/%3E%3C/circle%3E%3Ccircle cx='1400' cy='830' r='3' fill='rgba(0,212,255,0.8)'%3E%3Canimate attributeName='cy' from='830' to='-20' dur='12s' repeatCount='indefinite' begin='8s'/%3E%3Canimate attributeName='opacity' values='0;0.85;0' dur='12s' repeatCount='indefinite' begin='8s'/%3E%3C/circle%3E%3Ccircle cx='40' cy='750' r='4' fill='rgba(0,212,255,0.7)'%3E%3Canimate attributeName='cy' from='750' to='-20' dur='9.8s' repeatCount='indefinite' begin='1.8s'/%3E%3Canimate attributeName='opacity' values='0;0.75;0' dur='9.8s' repeatCount='indefinite' begin='1.8s'/%3E%3C/circle%3E%3Ccircle cx='160' cy='870' r='3' fill='rgba(0,212,255,0.8)'%3E%3Canimate attributeName='cy' from='870' to='-20' dur='8.2s' repeatCount='indefinite' begin='4.2s'/%3E%3Canimate attributeName='opacity' values='0;0.85;0' dur='8.2s' repeatCount='indefinite' begin='4.2s'/%3E%3C/circle%3E%3Ccircle cx='380' cy='840' r='5' fill='rgba(0,212,255,0.65)'%3E%3Canimate attributeName='cy' from='840' to='-20' dur='11.8s' repeatCount='indefinite' begin='6.8s'/%3E%3Canimate attributeName='opacity' values='0;0.7;0' dur='11.8s' repeatCount='indefinite' begin='6.8s'/%3E%3C/circle%3E%3Ccircle cx='540' cy='790' r='3' fill='rgba(0,212,255,0.75)'%3E%3Canimate attributeName='cy' from='790' to='-20' dur='7.8s' repeatCount='indefinite' begin='3.2s'/%3E%3Canimate attributeName='opacity' values='0;0.8;0' dur='7.8s' repeatCount='indefinite' begin='3.2s'/%3E%3C/circle%3E%3Ccircle cx='660' cy='855' r='4' fill='rgba(0,212,255,0.7)'%3E%3Canimate attributeName='cy' from='855' to='-20' dur='10.2s' repeatCount='indefinite' begin='7.5s'/%3E%3Canimate attributeName='opacity' values='0;0.75;0' dur='10.2s' repeatCount='indefinite' begin='7.5s'/%3E%3C/circle%3E%3Ccircle cx='800' cy='810' r='3' fill='rgba(0,212,255,0.8)'%3E%3Canimate attributeName='cy' from='810' to='-20' dur='9.2s' repeatCount='indefinite' begin='0.3s'/%3E%3Canimate attributeName='opacity' values='0;0.85;0' dur='9.2s' repeatCount='indefinite' begin='0.3s'/%3E%3C/circle%3E%3Ccircle cx='1000' cy='875' r='5' fill='rgba(0,212,255,0.6)'%3E%3Canimate attributeName='cy' from='875' to='-20' dur='13.2s' repeatCount='indefinite' begin='5.8s'/%3E%3Canimate attributeName='opacity' values='0;0.7;0' dur='13.2s' repeatCount='indefinite' begin='5.8s'/%3E%3C/circle%3E%3Ccircle cx='1140' cy='825' r='3' fill='rgba(0,212,255,0.75)'%3E%3Canimate attributeName='cy' from='825' to='-20' dur='8.8s' repeatCount='indefinite' begin='2.8s'/%3E%3Canimate attributeName='opacity' values='0;0.8;0' dur='8.8s' repeatCount='indefinite' begin='2.8s'/%3E%3C/circle%3E%3Ccircle cx='1360' cy='860' r='4' fill='rgba(0,212,255,0.7)'%3E%3Canimate attributeName='cy' from='860' to='-20' dur='11.2s' repeatCount='indefinite' begin='4.8s'/%3E%3Canimate attributeName='opacity' values='0;0.75;0' dur='11.2s' repeatCount='indefinite' begin='4.8s'/%3E%3C/circle%3E%3C/svg%3E");
            background-size: 100% 100%;
            background-repeat: no-repeat;
        }

        /* Scanline overlay */
        .stApp::after {
            content: '';
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            pointer-events: none;
            z-index: 0;
            background: repeating-linear-gradient(
                0deg,
                transparent,
                transparent 3px,
                rgba(0, 212, 255, 0.012) 3px,
                rgba(0, 212, 255, 0.012) 4px
            );
        }

        /* Border sweep animation for cards */
        @keyframes border-sweep {
            0%   { box-shadow: 0 8px 40px rgba(0,0,0,0.6), 0 0 0px rgba(0,212,255,0); }
            25%  { box-shadow: 0 8px 40px rgba(0,0,0,0.6), 0 -2px 20px rgba(0,212,255,0.3); }
            50%  { box-shadow: 0 8px 40px rgba(0,0,0,0.6), 2px 0 20px rgba(0,212,255,0.3); }
            75%  { box-shadow: 0 8px 40px rgba(0,0,0,0.6), 0 2px 20px rgba(0,212,255,0.3); }
            100% { box-shadow: 0 8px 40px rgba(0,0,0,0.6), 0 0 0px rgba(0,212,255,0); }
        }

        [data-testid="stForm"] {
            animation: fade-in-up 0.5s ease both, border-sweep 8s ease-in-out infinite !important;
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
