import streamlit as st
import plotly.graph_objects as go
from utils import render_nav
import pandas as pd
import joblib
import os

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# ⬇ Ngeload tiga file .pkl dari folder models, terus langsung disimpen di cache biar tiap kali
# user mencet tombol "Analyze!", ga perlu ngeload lagi dari disk, cukup dari memory makanya
# latencynya bisa low
@st.cache_resource # Ini yg jadi pemain utama urusan caching
def load_models():
    try:
        model_a       = joblib.load("models/modelA.pkl") # Model pertama, namanya burnout_model, ngepredict skor burnoutnya
        model_b       = joblib.load("models/modelB.pkl") # Model kedua, namanya grade_model, ngepredict future GPA-nya
        stress_mapping = joblib.load("models/stress_level_encoder_modelB.pkl") # Label Encoder buat input yang kategorical kayak stress levelnya
        return model_a, model_b, stress_mapping
    except Exception as e:
        st.error(f"Failed to load models: {e}")
        return None, None, None

model_a, model_b, stress_mapping = load_models() # Assign model_burnout yang direturn load_models ke variabel model_a. Sama juga buat yang duanya lagi (model_b & stress_mapping)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    * { font-family: 'Inter', sans-serif !important; }
    .stApp {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        min-height: 100vh;
    }
    header { visibility: hidden; }

    [data-testid="stForm"] {
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        padding: 2rem 2.5rem !important;
        border-radius: 16px !important;
        background: rgba(255, 255, 255, 0.07) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3) !important;
    }

   [data-testid="stRadio"] > div {
        justify-content: center !important;
        margin-top: -10px;
    }

    [data-testid="stFormSubmitButton"] {
        display: flex;
        justify-content: center;
        margin-top: 40px;
    }

    [data-testid="stFormSubmitButton"] button {
        border-radius: 50px !important;
        background: linear-gradient(90deg, #00b4d8, #0077b6) !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(0, 180, 216, 0.35) !important;
    }

    [data-testid="stFormSubmitButton"] button p {
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        color: #ffffff !important;
    }

    .stButton > button {
        border-radius: 50px !important;
        background: linear-gradient(90deg, #00b4d8, #0077b6) !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(0, 180, 216, 0.3) !important;
    }
    .stButton > button p {
        font-weight: 700 !important;
        color: white !important;
    }

    [data-testid="stTextArea"] textarea {
        background-color: rgba(255, 255, 255, 0.08) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 8px !important;
    }

    [data-testid="stTextArea"] textarea::placeholder {
        color: rgba(255, 255, 255, 0.4) !important;
    }

    [data-testid="stButton"][key="back_btn"] button,
        div:has(> [data-testid="stBaseButton-secondary"]) button {
        border-radius: 50px !important;
        background: transparent !important;
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
        color: white !important;
        box-shadow: none !important;
        margin-top: 50px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

render_nav()

# Checking jawabannya sebelum proses lebih jauh
required_keys = [
    "study_hours", "sleep_hours", "eca_hours", "social_hours", "physical_hours",
    "stress_level_category", "exam_pressure", "family_expectation",
    "financial_stress", "social_support", "anxiety_score", "depression_score",
]

if not all(key in st.session_state for key in required_keys):
    st.warning("Please complete all the form first.")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Back to Page 1", use_container_width=True, type="secondary"):
            st.switch_page("Page_1.py")
    st.stop()

# Ngeload jawaban-jawaban sebelumnya ke variabel yang akan dipakai
study_hours          = st.session_state.study_hours
sleep_hours          = st.session_state.sleep_hours
eca_hours            = st.session_state.eca_hours
social_hours         = st.session_state.social_hours
physical_hours       = st.session_state.physical_hours
stress_level_category = st.session_state.stress_level_category
exam_pressure        = st.session_state.exam_pressure
family_expectation   = st.session_state.family_expectation
financial_stress     = st.session_state.financial_stress
social_support       = st.session_state.social_support
anxiety_score        = st.session_state.anxiety_score
depression_score     = st.session_state.depression_score

st.markdown(
    """
    <h1 style='text-align: center; margin-top: -60px; margin-bottom: -40px;'>MEASURE YOUR BURNOUT</h1>
    <h1 style='text-align: center; margin-bottom: 20px;'>& PREDICT YOUR GRADE</h1>
    """,
    unsafe_allow_html=True,
)

# Mapping buat stress levelnya, assign value khusus untuk stress levelnya buat model_a
stress_mapping_a = {"Low": 2.29, "Moderate": 4.80, "High": 7.42}
stress_for_model_a = stress_mapping_a[stress_level_category]
stress_for_model_b = stress_mapping[stress_level_category]

input_model_a = pd.DataFrame([{
    "study_hours_per_day": study_hours,
    "sleep_hours":         sleep_hours,
    "exam_pressure":       exam_pressure,
    "stress_level":        stress_for_model_a,
    "financial_stress":    financial_stress,
    "social_support":      social_support,
    "anxiety_score":       anxiety_score,
    "depression_score":    depression_score,
    "family_expectation":  family_expectation,
}])

study_hours_for_b = study_hours if study_hours >= 5.0 else 7.48

input_model_b = pd.DataFrame([{
    "study_hours":    study_hours_for_b,
    "eca_hours":      eca_hours,
    "sleep_hours":    sleep_hours,
    "social_hours":   social_hours,
    "physical_hours": physical_hours,
    "stress_level":   stress_for_model_b,
}])

# Mesin prediktor utamanya
if model_a is not None and model_b is not None:
    burnout_raw    = model_a.predict(input_model_a)[0]
    burnout_score  = round(float(burnout_raw) * 10, 1)
    burnout_score  = max(0.0, min(100.0, burnout_score))
    predicted_gpa  = round(float(model_b.predict(input_model_b)[0]), 2)
    predicted_gpa  = max(0.0, min(4.0, predicted_gpa))
else:
    st.error("Models failed to load. Please contact the administrator.")
    st.stop()

# Prediksi skor burnout saat ini
if burnout_score >= 70:
    burnout_label = "BURNOUT."
    burnout_color = "#e74c3c"
elif burnout_score >= 40:
    burnout_label = "MILDLY BURNOUT."
    burnout_color = "#f39c12"
else:
    burnout_label = "HEALTHY."
    burnout_color = "#2ecc71"

fig = go.Figure(
    go.Indicator(
        mode="gauge+number",
        value=burnout_score,
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "rgba(0,0,0,1.0)"},
            "steps": [
                {"range": [0, 40], "color": "#2ecc71"},
                {"range": [40, 70], "color": "#f39c12"},
                {"range": [70, 100], "color": "#e74c3c"},
            ],
        },
    )
)

fig.update_layout(
    title={
        "text": "Your Burnout Level",
        "x": 0.5,
        "y": 0.94,
        "xanchor": "center",
        "font": {"size": 21, "color": "white"},
    },
    paper_bgcolor="rgba(0,0,0,0)",
    font_color="white",
    annotations=[
        {
            "text": f"<b>{burnout_label}</b>",
            "x": 0.5,  # horizontal center
            "y": 0.40,  # naik turunin angka ini untuk atur posisi vertikal
            "showarrow": False,
            "font": {"size": 28, "color": burnout_color},
            "xanchor": "center",
        }
    ],
)

st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

# Radar chart — lifestyle balance
stress_numeric = {"Low": 8.0, "Moderate": 5.0, "High": 2.0}[stress_level_category]

radar_labels = ["Study", "Sleep", "Extracurricular", "Social", "Physical", "Low Stress"]
radar_values = [
    study_hours,       # max 10
    sleep_hours / 12.0 * 10,       # max 12
    eca_hours / 8.0 * 10,          # max 8
    social_hours / 10.0 * 10,      # max 10
    physical_hours / 8.0 * 10,     # max 8
    stress_numeric,                 # Low=8, Moderate=5, High=2
]
radar_labels_closed = radar_labels + [radar_labels[0]]
radar_values_closed = radar_values + [radar_values[0]]

radar_fig = go.Figure(
    go.Scatterpolar(
        r=radar_values_closed,
        theta=radar_labels_closed,
        fill="toself",
        fillcolor="rgba(0, 180, 216, 0.2)",
        line=dict(color="#00b4d8", width=2),
        customdata=[
            f"{study_hours} hrs/day",
            f"{sleep_hours} hrs/day",
            f"{eca_hours} hrs/day",
            f"{social_hours} hrs/day",
            f"{physical_hours} hrs/day",
            stress_level_category,
            f"{study_hours} hrs/day",  # penutup loop
        ],
        hovertemplate="<b>%{theta}</b><br>%{customdata}<extra></extra>",
    )
)

radar_fig.update_layout(
    polar=dict(
        bgcolor="rgba(255,255,255,0.05)",
        radialaxis=dict(
            visible=True,
            range=[0, 10],
            tickfont=dict(color="rgba(255,255,255,0.5)", size=10),
            gridcolor="rgba(255,255,255,0.1)",
            linecolor="rgba(255,255,255,0.1)",
        ),
        angularaxis=dict(
            tickfont=dict(color="white", size=12),
            gridcolor="rgba(255,255,255,0.1)",
            linecolor="rgba(255,255,255,0.15)",
        ),
    ),
    paper_bgcolor="rgba(0,0,0,0)",
    title={
        "text": "Lifestyle Balance",
        "x": 0.5,
        "y": 0.94,
        "xanchor": "center",
        "font": {"size": 21, "color": "white"},
    },
    margin=dict(t=95, b=0, l=60, r=60),
)
st.plotly_chart(radar_fig, use_container_width=True, config={"displayModeBar": False})

# Prediksi GPA masa depan
if predicted_gpa >= 3.5:
    gpa_label = "Excellent! Keep it up."
elif predicted_gpa >= 3.0:
    gpa_label = "Good job!"
elif predicted_gpa >= 2.5:
    gpa_label = "Not so great."
else:
    gpa_label = "Needs improvement."

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown(
        f"""
        <div style='text-align: center;'>
            <p style='font-size: 1.5rem; font-weight: 600; margin-top: 65px;'>Your Predicted GPA</p>
            <p style='font-size: 3.0rem; font-weight: 650; margin-top: -30px;'>{predicted_gpa:.2f}/4.0</p>
            <p style='font-size: 1.0rem; margin-top: -28px;'>(<i>{gpa_label}</i>)</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Pesan insight yang dihasilkan tergantung skor burnout yang diprediksi
if burnout_score >= 70:
    insight_text = "Your burnout level is high! Try increasing your sleep to at least 7 hours and reduce study time slightly."
elif burnout_score >= 40:
    insight_text = "You're showing early signs of stress. Make sure to schedule breaks and social activities."
else:
    insight_text = "You're in good shape! Keep maintaining this balanced lifestyle."

st.markdown(
    f"""
    <div style='
        background-color: white;
        padding: 16px 20px;
        color: #000000;
        border: 1px solid #000000;
        border-left: 5px solid #000000;
        margin-top: 65px;
        margin-bottom: 65px;
    '>
        <span style='font-weight: 700;'>Insight Message:</span> {insight_text}
    </div>
""",
    unsafe_allow_html=True,
)

# Feedback Section
st.subheader("Feedback")
st.markdown(
    "<p style='color: white; margin-top: -13px; margin-bottom: 20px;'>Help us improve The Academic Shield!</p>",
    unsafe_allow_html=True,
)

with st.form("feedback_form"):
    st.markdown(
        "<p style='color:rgba(255,255,255,0.8); font-size:1rem; font-weight:600; margin-bottom:4px;'>Rate your experience</p>",
        unsafe_allow_html=True,
    )
    rating = st.radio(
        "Rate your experience",
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: "★" * x,
        index=None,
        horizontal=True,
        label_visibility="collapsed",
    )
    comment = st.text_area("Any comments?", placeholder="Write your thoughts here...")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        feedback_submitted = st.form_submit_button(
            "Submit Feedback", type="primary", use_container_width=True
        )

if feedback_submitted:
    if rating is None:
        st.error("Please select a star rating before submitting.")
    else:
        # Simpan feedback ke CSV
        os.makedirs("feedback", exist_ok=True)
        feedback_data = pd.DataFrame([{
            "study_hours":          study_hours,
            "sleep_hours":          sleep_hours,
            "eca_hours":            eca_hours,
            "social_hours":         social_hours,
            "physical_hours":       physical_hours,
            "stress_level":         stress_level_category,
            "exam_pressure":        exam_pressure,
            "family_expectation":   family_expectation,
            "financial_stress":     financial_stress,
            "social_support":       social_support,
            "anxiety_score":        anxiety_score,
            "depression_score":     depression_score,
            "burnout_score":        burnout_score,
            "predicted_gpa":        predicted_gpa,
            "rating":               rating,
            "comment":              comment,
        }])

        feedback_data.to_csv(
            "feedback/responses.csv",
            mode="a",
            header=not pd.io.common.file_exists("feedback/responses.csv"),
            index=False,
        )
        st.success("Thank you for your feedback! :)")


col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Back to Form", use_container_width=True, key="back_btn"):
        st.switch_page("Page_1.py")
