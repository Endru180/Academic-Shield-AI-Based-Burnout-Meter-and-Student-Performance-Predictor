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
    # Case-insensitive check for Burnout to apply the wave effect
    target_word = "BURNOUT" if "BURNOUT" in title else "Burnout"
    if target_word in title:
        wave = (
            f'<span style="position:relative;display:inline-block;">'
            f"{target_word}"
            '<svg style="position:absolute;bottom:-5px;left:0;width:100%;height:12px;overflow:visible;"'
            ' viewBox="0 0 200 12" preserveAspectRatio="none">'
            '<path d="M0,8 Q50,2 100,8 Q150,14 200,8"'
            ' stroke="#D97757" stroke-width="2.5" fill="none" stroke-linecap="round"'
            ' stroke-dasharray="210" stroke-dashoffset="210"'
            ' style="animation:drawBurnout 1.2s ease-out 0.6s forwards;"/>'
            "</svg>"
            "</span>"
        )
        title = title.replace(target_word, wave)
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


def fix_page_title(title: str = "Academic Shield"):
    import streamlit.components.v1 as components

    components.html(
        f"""
<script>
(function() {{
    var t = {json.dumps(title)};
    var pd = window.parent.document;
    function enforce() {{ if (pd.title !== t) pd.title = t; }}
    enforce();
    var el = pd.querySelector('title');
    if (el) {{
        var obs = new MutationObserver(enforce);
        obs.observe(el, {{ childList: true, subtree: true, characterData: true }});
    }}
}})();
</script>
""",
        height=0,
        scrolling=False,
    )


def render_hamburger_menu():
    import streamlit.components.v1 as components
    components.html(
        """
<script>
(function(){
  var doc = window.parent.document;
  if (doc.getElementById('as-hamburger-btn')) return;

  // ── Define functions on parent window FIRST ──
  window.parent.asToggleDrawer = function(){
    var d = doc.getElementById('as-drawer');
    var o = doc.getElementById('as-overlay');
    if (d.classList.contains('as-open')){
      d.classList.remove('as-open'); o.classList.remove('as-open');
    } else {
      d.classList.add('as-open'); o.classList.add('as-open');
    }
  };
  window.parent.asCloseDrawer = function(){
    doc.getElementById('as-drawer').classList.remove('as-open');
    doc.getElementById('as-overlay').classList.remove('as-open');
  };

  // ── Styles ──
  var style = doc.createElement('style');
  style.id = 'as-hamburger-style';
  style.textContent = [
    '#as-hamburger-btn{position:fixed;top:18px;right:18px;z-index:9999;width:40px;height:40px;border-radius:10px;background:#FAF6F1;border:1px solid rgba(0,0,0,0.08);box-shadow:0 2px 8px rgba(0,0,0,0.08);cursor:pointer;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:5px;transition:box-shadow 0.2s;}',
    '#as-hamburger-btn:hover{box-shadow:0 4px 16px rgba(217,119,87,0.2);}',
    '#as-hamburger-btn .as-bar{width:18px;height:2px;background:#2D2D2D;border-radius:2px;}',
    '#as-drawer{position:fixed;top:0;right:-320px;width:300px;height:100%;background:#FAF6F1;z-index:9998;box-shadow:-4px 0 24px rgba(0,0,0,0.10);transition:right 0.35s cubic-bezier(0.4,0,0.2,1);overflow-y:auto;padding:64px 28px 40px;font-family:Newsreader,Georgia,serif;}',
    '#as-drawer.as-open{right:0;}',
    '#as-overlay{position:fixed;inset:0;background:rgba(0,0,0,0);z-index:9997;pointer-events:none;transition:background 0.35s;}',
    '#as-overlay.as-open{background:rgba(0,0,0,0.18);pointer-events:all;}',
    '#as-drawer .as-close{position:absolute;top:16px;right:16px;background:none;border:none;cursor:pointer;font-size:1.2rem;color:#9B9B9B;padding:4px 8px;border-radius:6px;}',
    '#as-drawer .as-close:hover{color:#2D2D2D;}',
    '#as-drawer .as-sec{font-size:0.65rem;font-weight:700;letter-spacing:2.5px;text-transform:uppercase;color:#D97757;margin-bottom:16px;padding-bottom:8px;border-bottom:1px solid rgba(217,119,87,0.15);}',
    '#as-drawer .as-tip{display:flex;gap:12px;align-items:flex-start;margin-bottom:14px;}',
    '#as-drawer .as-tip-icon{flex-shrink:0;width:28px;height:28px;border-radius:8px;background:rgba(217,119,87,0.08);display:flex;align-items:center;justify-content:center;font-size:0.85rem;}',
    '#as-drawer .as-tip-text{font-size:0.85rem;color:#4B4B4B;line-height:1.6;}',
    '#as-drawer .as-tip-text b{color:#2D2D2D;}',
    '#as-drawer .as-about{background:#fff;border:1px solid rgba(0,0,0,0.06);border-radius:12px;padding:16px 18px;margin-bottom:12px;font-size:0.85rem;color:#4B4B4B;line-height:1.65;}',
    '#as-drawer .as-about b{color:#2D2D2D;}',
    '#as-drawer .as-div{height:1px;background:rgba(0,0,0,0.06);margin:24px 0;}',
  ].join('');
  doc.head.appendChild(style);

  // ── Overlay ──
  var overlay = doc.createElement('div');
  overlay.id = 'as-overlay';
  overlay.setAttribute('onclick', 'asCloseDrawer()');
  doc.body.appendChild(overlay);

  // ── Hamburger button ──
  var btn = doc.createElement('div');
  btn.id = 'as-hamburger-btn';
  btn.title = 'Menu';
  btn.innerHTML = '<div class="as-bar"></div><div class="as-bar"></div><div class="as-bar"></div>';
  btn.setAttribute('onclick', 'asToggleDrawer()');
  doc.body.appendChild(btn);

  // ── Drawer ──
  var drawer = doc.createElement('div');
  drawer.id = 'as-drawer';
  drawer.innerHTML = [
    '<button class="as-close" onclick="asCloseDrawer()">&#x2715;</button>',
    '<div class="as-sec">Tips</div>',
    '<div class="as-tip"><div class="as-tip-icon">&#128564;</div><div class="as-tip-text"><b>Sleep 7&#8211;9 hours.</b> Sleep is the single biggest predictor of academic performance and burnout recovery.</div></div>',
    '<div class="as-tip"><div class="as-tip-icon">&#128218;</div><div class="as-tip-text"><b>Study in focused blocks.</b> 4&#8211;6 hours of deep work beats 10 hours of distracted studying.</div></div>',
    '<div class="as-tip"><div class="as-tip-icon">&#127939;</div><div class="as-tip-text"><b>Move daily.</b> Even 30 minutes of exercise reduces anxiety and improves memory consolidation.</div></div>',
    '<div class="as-tip"><div class="as-tip-icon">&#129309;</div><div class="as-tip-text"><b>Lean on your support network.</b> Social connection is a strong buffer against burnout.</div></div>',
    '<div class="as-tip"><div class="as-tip-icon">&#9878;</div><div class="as-tip-text"><b>Balance your day.</b> Allocate time across study, rest, social, and physical activity.</div></div>',
    '<div class="as-tip"><div class="as-tip-icon">&#129496;</div><div class="as-tip-text"><b>Notice early signs.</b> Persistent fatigue, low motivation, and difficulty concentrating are early burnout signals.</div></div>',
    '<div class="as-div"></div>',
    '<div class="as-sec">About</div>',
    '<div class="as-about"><b>Academic Shield</b> is an AI-powered tool that estimates your burnout risk and predicts your GPA based on your daily lifestyle and mental health habits.</div>',
    '<div class="as-about"><b>How it works:</b> Two machine learning models analyze your inputs &#8212; one classifies burnout level (Healthy / Mildly Burnout / Burnout), the other predicts your GPA on a 0&#8211;4.0 scale.</div>',
    '<div class="as-about"><b>Privacy:</b> All inputs are processed locally and are never stored or transmitted. Your data stays on your device.</div>',
    '<div class="as-about" style="font-size:0.78rem;color:#9B9B9B;">Built for educational purposes. Results are estimates and should not replace professional mental health advice.</div>',
  ].join('');
  doc.body.appendChild(drawer);
})();
</script>
""",
        height=0,
        scrolling=False,
    )
