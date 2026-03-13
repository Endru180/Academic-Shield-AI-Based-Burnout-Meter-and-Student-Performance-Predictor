import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import joblib

# ⬇ Ngeload tiga file .pkl dari folder models, terus langsung disimpen di cache biar tiap kali
# user mencet tombol "Analyze!", ga perlu ngeload lagi dari disk, cukup dari memory makanya
# latencynya bisa low
@st.cache_resource # Ini yg jadi pemain utama urusan caching
def load_models():
    try:
        model_burnout = joblib.load("models/burnout_model.pkl") # Model pertama, namanya burnout_model, ngepredict skor burnoutnya
        model_grade = joblib.load("models/grade_model.pkl") # Model kedua, namanya grade_model, ngepredict future GPA-nya
        encoder = joblib.load("models/encoder.pkl") # Label Encoder buat input yang kategorical kayak lingkungan belajarnya ama strategi copingnya
        return model_burnout, model_grade, encoder
    except:
        return None, None, None

model_burnout, model_grade, encoder = load_models() # Assign model_burnout yang direturn load_models ke variabel model_burnout. Sama juga buat yang duanya lagi (model_grade & encoder)

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

if "study_time" not in st.session_state:
    st.warning("Please fill out the form first!")
    if st.button("Back to Form"):
        st.switch_page("app.py")
    st.stop()

study_time = st.session_state.study_time
sleep_time = st.session_state.sleep_time
social_free_time = st.session_state.social_free_time
current_gpa = st.session_state.current_gpa
environment = st.session_state.environment
coping = st.session_state.coping

st.markdown(
    """
    <h1 style='text-align: center; margin-top: -60px; margin-bottom: -55px;'>MEASURE YOUR BURNOUT</h1>
    <h1 style='text-align: center; margin-bottom: 20px;'>& PREDICT YOUR GRADE</h1>
    """,
    unsafe_allow_html=True,
)

if encoder is not None:
    input_data = pd.DataFrame([{
        "study_time":       study_time,
        "sleep_time":       sleep_time,
        "social_free_time": social_free_time,
        "current_gpa":      current_gpa,
        "environment":      encoder.transform([environment])[0],
        "coping":           encoder.transform([coping])[0],
    }])

# To Do 1: Replace this with Burnout Score model (model_burnout)
burnout_score = round(
    100 - (sleep_time * 4) - (social_free_time * 2) + (study_time * 2), 1
)
burnout_score = max(0, min(100, burnout_score))

# To Do 2: Replace this with GPA Predictor model (model_grade)
predicted_grade = current_gpa

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

st.plotly_chart(fig, use_container_width=True)

if predicted_grade >= 3.5:
    gpa_label = "Excellent! Keep it up."
elif predicted_grade >= 3.0:
    gpa_label = "Good job!"
elif predicted_grade >= 2.5:
    gpa_label = "Not so great."
else:
    gpa_label = "Needs improvement."

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown(
        f"""
        <div style='text-align: center;'>
            <p style='font-size: 1.5rem; font-weight: 600;'>Your Predicted GPA</p>
            <p style='font-size: 3.0rem; font-weight: 650; margin-top: -30px;'>{predicted_grade:.1f}/4.0</p>
            <p style='font-size: 1.0rem; margin-top: -28px;'>(<i>{gpa_label}</i>)</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

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
        margin-top: 60px;
        margin-bottom: 70px;
    '>
        <span style='font-weight: 700;'>Insight Message:</span> {insight_text}
    </div>
""",
    unsafe_allow_html=True,
)

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
        feedback_data = pd.DataFrame(
            [
                {
                    "study_time": study_time,
                    "sleep_time": sleep_time,
                    "social_free_time": social_free_time,
                    "current_gpa": current_gpa,
                    "environment": environment,
                    "coping": coping,
                    "burnout_score": burnout_score,
                    "predicted_grade": predicted_grade,
                    "rating": rating.count("⭐"),
                    "comment": comment,
                }
            ]
        )

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
        st.switch_page("app.py")
