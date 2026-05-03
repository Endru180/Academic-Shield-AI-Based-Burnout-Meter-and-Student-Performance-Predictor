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
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 10px;
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            transition: background 0.2s;
        }

        .hb-icon:hover {
            background: rgba(0, 180, 216, 0.25);
        }

        .hb-icon span {
            display: block;
            width: 22px;
            height: 2px;
            background: white;
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
            background: rgba(15, 32, 39, 0.97);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 14px;
            padding: 0.5rem;
            min-width: 190px;
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.5);
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
            background: rgba(0, 180, 216, 0.2);
            color: #ffffff;
        }

        .hb-dropdown hr {
            border: none;
            border-top: 1px solid rgba(255,255,255,0.08);
            margin: 0.3rem 0.5rem;
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
