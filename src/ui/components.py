"""HTML/SVG UI components — header, progress bar, cards, etc."""

import json
import streamlit as st


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


def render_animated_header(title: str, subtitle: str = ""):
    render_shield_logo()
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


def render_probability_bars(probabilities: list):
    from src.config import COLORS

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


def render_insight_card_animated(text: str, color: str):
    import streamlit.components.v1 as components

    escaped = json.dumps(text)
    html = f"""<!DOCTYPE html><html><head>
<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{background:#FAF6F1;overflow:hidden;font-family:'Newsreader',Georgia,'Times New Roman',serif;padding:4px 0;}}
@keyframes blink{{0%,100%{{opacity:1}}50%{{opacity:0}}}}
@keyframes fadeIn{{from{{opacity:0;transform:translateY(6px)}}to{{opacity:1;transform:none}}}}
.wrap{{
  display:flex;gap:16px;align-items:flex-start;
  animation:fadeIn 0.5s ease-out;
}}
.accent-bar{{
  flex-shrink:0;width:2px;border-radius:2px;
  background:{color};opacity:0.5;align-self:stretch;min-height:40px;
}}
.body{{flex:1;}}
.label{{
  font-size:0.68rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;
  color:{color};opacity:0.8;margin-bottom:8px;
}}
.text{{line-height:1.78;color:#4B4B4B;font-size:0.93rem;min-height:1.5em;}}
.cur{{color:{color};opacity:0.6;animation:blink 1s step-end infinite;font-weight:300;}}
</style></head><body>
<div class="wrap">
  <div class="accent-bar"></div>
  <div class="body">
    <div class="label">Insight</div>
    <div class="text" id="p"><span class="cur" id="cur">|</span></div>
  </div>
</div>
<script>
var t={escaped},i=0,p=document.getElementById('p'),c=document.getElementById('cur');
function go(){{
  if(i<t.length){{p.insertBefore(document.createTextNode(t[i++]),c);setTimeout(go,13);}}
  else{{setTimeout(function(){{c.style.display='none';}},2000);}}
}}
setTimeout(go,60);
</script>
</body></html>"""
    components.html(html, height=120, scrolling=False)


def render_divider():
    st.markdown('<div class="warm-divider"></div>', unsafe_allow_html=True)
