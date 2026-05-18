"""Shared UI — Claude-style warm, elegant design."""

import json
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



# ---------------------------------------------------------------------------
# Shield logo — warm terracotta SVG
# ---------------------------------------------------------------------------

def render_shield_logo():
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 16px; animation: fadeIn 0.8s ease-out;">
            <svg width="180" height="64" viewBox="0 0 180 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- Shield icon -->
                <path d="M22 4L6 12V26C6 36.5 13 45.5 22 48C31 45.5 38 36.5 38 26V12L22 4Z"
                      fill="#D97757" opacity="0.18"/>
                <path d="M22 4L6 12V26C6 36.5 13 45.5 22 48C31 45.5 38 36.5 38 26V12L22 4Z"
                      fill="none" stroke="#D97757" stroke-width="1.8" opacity="0.7"/>
                <path d="M22 8L10 15V26C10 34 16 41.5 22 44C28 41.5 34 34 34 26V15L22 8Z"
                      fill="none" stroke="#D97757" stroke-width="0.8" opacity="0.25"/>
                <!-- Checkmark -->
                <path d="M19.5 28.5L16 25L14.5 26.5L19.5 31.5L30 21L28.5 19.5L19.5 28.5Z"
                      fill="#D97757" opacity="0.85"/>
                <!-- Wordmark: Academic Shield -->
                <text x="46" y="24" font-family="'Newsreader', Georgia, serif" font-size="14"
                      font-weight="600" fill="#2D2D2D" letter-spacing="0.5">Academic</text>
                <text x="46" y="42" font-family="'Newsreader', Georgia, serif" font-size="14"
                      font-weight="400" fill="#D97757" letter-spacing="1">Shield</text>
                <!-- Accent line -->
                <line x1="46" y1="47" x2="148" y2="47" stroke="#D97757" stroke-width="1" opacity="0.25"/>
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
    # Wrap BURNOUT with animated SVG wave underline if present
    if "BURNOUT" in title:
        wave = (
            '<span style="position:relative;display:inline-block;">'
            "BURNOUT"
            '<svg style="position:absolute;bottom:-5px;left:0;width:100%;height:12px;overflow:visible;"'
            ' viewBox="0 0 200 12" preserveAspectRatio="none">'
            '<path d="M0,8 Q50,2 100,8 Q150,14 200,8"'
            ' stroke="#D97757" stroke-width="2.5" fill="none" stroke-linecap="round"'
            ' stroke-dasharray="210" stroke-dashoffset="210"'
            ' style="animation:drawBurnout 1.2s ease-out 0.6s forwards;"/>'
            "</svg>"
            "</span>"
        )
        title = title.replace("BURNOUT", wave)
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
# Typewriter insight card
# ---------------------------------------------------------------------------

def render_insight_card_animated(text: str, color: str):
    import streamlit.components.v1 as components

    escaped = json.dumps(text)
    html = f"""<!DOCTYPE html><html><head>
<style>
@import url('https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,600&display=swap');
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{background:#FAF6F1;overflow:hidden;font-family:'Newsreader',Georgia,serif;}}
@keyframes blink{{0%,100%{{opacity:1}}50%{{opacity:0}}}}
.card{{background:#fff;border:1px solid rgba(0,0,0,0.06);border-left:4px solid {color};
       border-radius:12px;padding:20px 24px;box-shadow:0 1px 3px rgba(0,0,0,0.04);}}
.label{{font-weight:700;color:{color};font-size:0.9rem;letter-spacing:0.2px;}}
.text{{margin-top:8px;line-height:1.75;color:#4B4B4B;font-size:0.93rem;min-height:2em;}}
.cur{{color:{color};animation:blink 1s step-end infinite;font-weight:300;}}
</style></head><body>
<div class="card">
  <div class="label">Insight</div>
  <div class="text" id="p"><span class="cur" id="cur">|</span></div>
</div>
<script>
var t={escaped},i=0,p=document.getElementById('p'),c=document.getElementById('cur');
function go(){{
  if(i<t.length){{p.insertBefore(document.createTextNode(t[i++]),c);setTimeout(go,14);}}
  else{{setTimeout(function(){{c.style.display='none';}},2000);}}
}}
setTimeout(go,420);
</script>
</body></html>"""
    components.html(html, height=130, scrolling=False)


# ---------------------------------------------------------------------------
# Divider
# ---------------------------------------------------------------------------

def render_divider():
    st.markdown('<div class="warm-divider"></div>', unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Neural background + SVG favicon — injected into parent document
# ---------------------------------------------------------------------------

def render_neural_background():
    import streamlit.components.v1 as components

    components.html(
        """
<script>
(function() {
    var doc = window.parent.document;
    var win = window.parent;

    // ── Persistent hide CSS — survives Streamlit page transitions ──
    if (!doc.getElementById('as-global-hide')) {
        var hide = doc.createElement('style');
        hide.id = 'as-global-hide';
        hide.textContent = [
            '[data-testid="stSidebar"]{display:none!important;}',
            '[data-testid="stSidebarCollapsedControl"]{display:none!important;}',
            '[data-testid="stSidebarCollapseButton"]{display:none!important;}',
            '[data-testid="stExpandSidebarButton"]{display:none!important;}',
            'section[data-testid="stSidebarContent"]{display:none!important;}',
            'header[data-testid="stHeader"]{display:none!important;}',
        ].join('');
        doc.head.appendChild(hide);
    }

    // ── SVG favicon ──
    doc.querySelectorAll('link[rel*="icon"]').forEach(function(l) { l.remove(); });
    var fav = doc.createElement('link');
    fav.rel = 'icon';
    fav.type = 'image/svg+xml';
    fav.href = 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"%3E%3Cpath d="M16 2L4 8v10c0 8 5.5 13.5 12 16 6.5-2.5 12-8 12-16V8L16 2z" fill="%23D97757" opacity="0.9"/%3E%3Cpath d="M13.5 17.5l-3-3-1.5 1.5 4.5 4.5 9-9-1.5-1.5z" fill="white"/%3E%3C/svg%3E';
    doc.head.appendChild(fav);

    // ── Neural animation — inject as native <script> in parent <head> ──
    // Code runs in parent window scope, no iframe lifetime dependency.
    if (doc.getElementById('as-neural-script')) return;

    // Create canvas before script executes so it exists immediately
    var canvas = doc.createElement('canvas');
    canvas.id = 'as-neural-canvas';
    canvas.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;z-index:0;pointer-events:none;';
    doc.body.insertBefore(canvas, doc.body.firstChild);

    var script = doc.createElement('script');
    script.id = 'as-neural-script';
    script.textContent = '(function(){'
        + 'var CW=730,N=30,MD=190,SP=0.22,nodes=[];'
        + 'function mkCanvas(){'
        + '  var c=document.getElementById("as-neural-canvas");'
        + '  if(!c){c=document.createElement("canvas");c.id="as-neural-canvas";'
        + '    c.style.cssText="position:fixed;top:0;left:0;width:100%;height:100%;z-index:0;pointer-events:none;";'
        + '    document.body.insertBefore(c,document.body.firstChild);}'
        + '  c.width=window.innerWidth;c.height=window.innerHeight;return c;'
        + '}'
        + 'var c0=mkCanvas();'
        + 'window.addEventListener("resize",function(){var c=document.getElementById("as-neural-canvas");if(c){c.width=window.innerWidth;c.height=window.innerHeight;}});'
        + 'for(var i=0;i<N;i++){'
        + '  var s=i<N/2?"left":"right",sw=Math.max((c0.width-CW)/2,80);'
        + '  nodes.push({x:s==="left"?Math.random()*sw:c0.width-Math.random()*sw,'
        + '    y:Math.random()*c0.height,vx:(Math.random()-0.5)*SP,vy:(Math.random()-0.5)*SP,'
        + '    r:2+Math.random()*2.5,pulse:Math.random()*Math.PI*2,side:s});'
        + '}'
        + 'function draw(){'
        + '  var c=document.getElementById("as-neural-canvas");'
        + '  if(!c)c=mkCanvas();'
        + '  var ctx=c.getContext("2d");'
        + '  ctx.clearRect(0,0,c.width,c.height);'
        + '  var lm=(c.width-CW)/2+24,rm=(c.width+CW)/2-24;'
        + '  for(var k=0;k<nodes.length;k++){'
        + '    var n=nodes[k];n.x+=n.vx;n.y+=n.vy;n.pulse+=0.012;'
        + '    if(n.y<0){n.y=0;n.vy=Math.abs(n.vy);}if(n.y>c.height){n.y=c.height;n.vy=-Math.abs(n.vy);}'
        + '    if(n.x<0){n.x=0;n.vx=Math.abs(n.vx);}if(n.x>c.width){n.x=c.width;n.vx=-Math.abs(n.vx);}'
        + '    if(n.side==="left"&&n.x>lm)n.vx=-Math.abs(n.vx);'
        + '    if(n.side==="right"&&n.x<rm)n.vx=Math.abs(n.vx);'
        + '  }'
        + '  for(var i=0;i<nodes.length;i++){for(var j=i+1;j<nodes.length;j++){'
        + '    var dx=nodes[i].x-nodes[j].x,dy=nodes[i].y-nodes[j].y,d=Math.sqrt(dx*dx+dy*dy);'
        + '    if(d<MD){ctx.beginPath();ctx.moveTo(nodes[i].x,nodes[i].y);ctx.lineTo(nodes[j].x,nodes[j].y);'
        + '      ctx.strokeStyle="rgba(217,119,87,"+((1-d/MD)*0.22)+")";ctx.lineWidth=1;ctx.stroke();}'
        + '  }}'
        + '  for(var m=0;m<nodes.length;m++){'
        + '    var nd=nodes[m],p=0.5+0.5*Math.sin(nd.pulse);'
        + '    ctx.beginPath();ctx.arc(nd.x,nd.y,nd.r+p*0.8,0,Math.PI*2);'
        + '    ctx.fillStyle="rgba(217,119,87,"+(0.38+0.18*p)+")";ctx.fill();'
        + '  }'
        + '  requestAnimationFrame(draw);'
        + '}'
        + 'requestAnimationFrame(draw);'
        + '})();';
    doc.head.appendChild(script);
})();
</script>
""",
        height=0,
        scrolling=False,
    )
