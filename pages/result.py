import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import joblib
import os

# ⬇ Ngeload tiga file .pkl dari folder models, terus langsung disimpen di cache biar tiap kali
# user mencet tombol "Analyze!", ga perlu ngeload lagi dari disk, cukup dari memory makanya
# latencynya bisa low
@st.cache_resource
def load_models():
    try:
        model_a             = joblib.load("models/modelA.pkl")
        model_b             = joblib.load("models/modelB.pkl")
        stress_mapping      = joblib.load("models/stress_level_encoder_modelB.pkl")
        pipeline_a          = joblib.load("models/pipeline_a.pkl")
        pipeline_b          = joblib.load("models/pipeline_b.pkl")
        burnout_class_map   = joblib.load("models/burnout_class_mapping.pkl")
        return model_a, model_b, stress_mapping, pipeline_a, pipeline_b, burnout_class_map
    except Exception as e:
        st.error(f"Failed to load models: {e}")
        return None, None, None, None, None, None

model_a, model_b, stress_mapping, pipeline_a, pipeline_b, burnout_class_map = load_models()

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    * { font-family: 'Inter', sans-serif !important; }
    .stApp { background-color: #3d8ef0; }
    header { visibility: hidden; }

    [data-testid="stForm"] {
        border: none !important;
        box-shadow: none !important;
        padding: 0 !important;
        background-color: transparent !important;
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
    }

    [data-testid="stFormSubmitButton"] button p {
        font-weight: 700 !important;
        font-size: 1.1rem !important;
    }

    .stButton > button {
        border-radius: 50px !important;
        background-color: #000000 !important;
        border: none !important;
    }
    .stButton > button p {
        font-weight: 700 !important;
        color: white !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

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
    <h1 style='text-align: center; margin-top: -60px; margin-bottom: -55px;'>MEASURE YOUR BURNOUT</h1>
    <h1 style='text-align: center; margin-bottom: 20px;'>& PREDICT YOUR GRADE</h1>
    """,
    unsafe_allow_html=True,
)

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
    "physical_activity":   physical_hours,
}])

input_model_b = pd.DataFrame([{
    "study_hours":    study_hours,
    "eca_hours":      eca_hours,
    "sleep_hours":    sleep_hours,
    "social_hours":   social_hours,
    "physical_hours": physical_hours,
    "stress_level":   stress_for_model_b,
}])

if model_a is not None and model_b is not None and pipeline_a is not None and pipeline_b is not None and burnout_class_map is not None:
    # Model A — Classification with predict_proba for gauge
    input_a_engineered = pipeline_a(input_model_a)
    burnout_class  = int(model_a.predict(input_a_engineered)[0])          # 0, 1, or 2
    burnout_proba  = model_a.predict_proba(input_a_engineered)[0]         # [p_healthy, p_mild, p_burnout]
    # Weighted pseudo-score mapped to 0-100 for the gauge display
    burnout_score  = float(burnout_proba[0] * 20 + burnout_proba[1] * 55 + burnout_proba[2] * 85)
    burnout_score  = round(max(0.0, min(100.0, burnout_score)), 1)

    # Model B — Regression (unchanged)
    input_b_engineered = pipeline_b["engineer_fn"](input_model_b)
    input_b_final = input_b_engineered[pipeline_b["important_features"]]
    predicted_gpa  = round(float(model_b.predict(input_b_final)[0]), 2)
    predicted_gpa  = max(0.0, min(4.0, predicted_gpa))
else:
    st.error("Models failed to load. Please contact the administrator.")
    st.stop()

# Burnout label derived from classifier prediction (not score thresholds)
if burnout_class == 2:
    burnout_label = "BURNOUT."
    burnout_color = "#e74c3c"
elif burnout_class == 1:
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

st.plotly_chart(fig, use_container_width=True)

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
            <p style='font-size: 1.5rem; font-weight: 600;'>Your Predicted GPA</p>
            <p style='font-size: 3.0rem; font-weight: 650; margin-top: -30px;'>{predicted_gpa:.2f}/4.0</p>
            <p style='font-size: 1.0rem; margin-top: -28px;'>(<i>{gpa_label}</i>)</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Insight message based on classifier prediction
if burnout_class == 2:
    insight_text = "Your burnout level is high! Try increasing your sleep to at least 7 hours and reduce study time slightly."
elif burnout_class == 1:
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
        margin-top: 60px;
        margin-bottom: 70px;
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
    rating = st.radio(
        "Rate your experience",
        options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
        horizontal=True,
    )
    comment = st.text_area("Any comments?", placeholder="Write your thoughts here...")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        feedback_submitted = st.form_submit_button(
            "Submit Feedback", type="primary", use_container_width=True
        )

if feedback_submitted:
    if rating is None:
        st.warning("Please give a star rating first!")
    else:
        # Simpan feedback ke CSV
        os.makedirs("feedback", exist_ok=True) # Buat folder feedback kalau belum ada. Kalau sudah ada, skip
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
            "rating":               rating.count("⭐"),
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
    if st.button("Back to Form", use_container_width=True):
        st.switch_page("Page_1.py")
