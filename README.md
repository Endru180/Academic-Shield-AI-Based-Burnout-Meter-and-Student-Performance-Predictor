# 🛡️ Academic Shield — AI-Based Burnout Meter & Student Performance Predictor

Academic Shield is a **Streamlit** web app that estimates a student's **burnout risk** and predicts their **GPA** from everyday lifestyle and mental-health habits. It combines two independently trained machine-learning models behind a single guided, two-step questionnaire and presents the results through an interactive dashboard (gauge, radar chart, probability breakdown, and a written insight).

> Built for educational purposes. Results are estimates and should **not** replace professional mental-health advice.

---

## ✨ Features

- **Two-step guided form**
  1. *Lifestyle & Habits* — daily study, sleep, extracurricular, social, and physical-activity hours (with a live "hours unallocated of 24h" check).
  2. *Mental Health & Stress* — stress level plus rated sliders for exam pressure, family expectation, financial stress, social support, anxiety, and depression.
- **Burnout classification** — gauge chart + class label (*Healthy / Mildly Burnout / Burnout*) + per-class probability breakdown.
- **GPA prediction** — circular progress ring showing predicted GPA (0.0–4.0) with a contextual label (e.g. "Good job!", "Needs improvement.").
- **Profile radar chart** — visualizes all 12 inputs on a single 0–10 scale.
- **Animated AI-generated insight** — a typewriter-style message tailored to the predicted burnout class.
- **Feedback collection** — star rating + comment, stored in a Supabase table.
- **Custom themed UI** — warm "Claude-style" palette, animated neural-network background, hidden Streamlit chrome, hamburger side-drawer with tips & app info, and a custom favicon — all injected via custom CSS/JS.

---

## 🧠 The two ML models

| | **Model A — Burnout Classifier** | **Model B — GPA Regressor** |
|---|---|---|
| Type | `XGBClassifier` (3-class) | `GradientBoostingRegressor` |
| Target | Burnout class: `0=Healthy`, `1=Mildly Burnout`, `2=Burnout` (binned from a continuous `burnout_score`: `<4`→Healthy, `4–7`→Mild, `≥7`→Burnout) | GPA on a 0.0–4.0 scale |
| Dataset | `academic_stress_level.csv` (~1M rows) | `student_lifestyle_dataset.csv` (~2,000 rows) |
| Base features (10) | `study_hours_per_day`, `sleep_hours`, `exam_pressure`, `stress_level`, `financial_stress`, `social_support`, `anxiety_score`, `depression_score`, `family_expectation`, `physical_activity` | `study_hours`, `eca_hours`, `sleep_hours`, `social_hours`, `physical_hours`, `stress_level` |
| Feature engineering | 10 extra engineered features (interaction terms, ratios, squared terms, threshold flags) — see `src/features.py::engineer_features_a` | None (kept intentionally simple; `engineer_features_b` exists only for experimentation in `v2_improvement/`, **not** used in production) |
| Cleaning / balancing | IQR cleaning on feature columns only (preserves minority classes) → 80/20 stratified split → SMOTE oversampling on the training set only | Z-score (\|z\| < 3) outlier removal → 70/30 split |
| Tuning | Optuna TPE search (150 trials each over LightGBM/XGBoost/CatBoost + a stacking ensemble); **XGBoost won** on the held-out test set | Manually-set `GradientBoostingRegressor` hyperparameters |
| Reported performance | Test Macro-F1 ≈ 0.57, 5-fold CV Macro-F1 ≈ 0.54, CV Accuracy ≈ 0.92 (dummy baseline ≈ 0.31 F1 / 0.89 acc) | Test R² ≈ 0.53, RMSE ≈ 0.20, NRMSE ≈ 12% |
| Stress encoding | `STRESS_MAPPING_A = {"Low": 2.29, "Moderate": 4.80, "High": 7.42}` (means learned from the training data) | `{"Low": 0, "Moderate": 1, "High": 2}` via `models/stress_level_encoder_modelB.pkl` |

Training notebooks live in `notebooks/` (`modelA.ipynb`, `modelB.ipynb`); `v2_improvement/` contains exploratory work (EDA + an experimental Model B v2 with feature engineering) that is **not** wired into the deployed app. `MLflow.ipynb` re-runs both training pipelines through MLflow for experiment tracking (see note below).

### Burnout gauge score

The 0–100 gauge score is a probability-weighted blend:
`score = P(Healthy)·20 + P(Mild)·55 + P(Burnout)·85`
The weights were chosen so a confident prediction for each class lands inside its matching gauge segment (`[0,40]`, `[40,70]`, `[70,100]`).

---

## 🗂️ Project structure

```
.
├── Page_1.py                  # Entry point — Step 1: Lifestyle & Habits
├── pages/
│   ├── Page_2.py              # Step 2: Mental Health & Stress
│   └── result.py              # Predictions, charts, insight, feedback form
├── src/
│   ├── config.py              # Central config: feature lists, mappings, colors, copy
│   ├── models.py              # Model loading + predict_burnout / predict_gpa
│   ├── features.py            # Feature-engineering fns injected for cloudpickle
│   └── ui/
│       ├── css.py             # Theme CSS + favicon injection
│       ├── background.py      # Animated neural-network background + sidebar hiding
│       ├── components.py      # Header, progress bar, cards, hamburger menu, etc.
│       └── charts.py          # Plotly gauge / GPA ring / radar chart
├── models/                    # Serialized model artifacts (joblib/pickle, Git LFS)
│   ├── modelA.pkl             # XGBClassifier (burnout)
│   ├── modelB.pkl             # GradientBoostingRegressor (GPA)
│   ├── pipeline_a.pkl         # cloudpickled engineer_features_a
│   ├── burnout_class_mapping.pkl
│   └── stress_level_encoder_modelB.pkl
├── notebooks/                 # Model training notebooks (source of truth for models/)
├── v2_improvement/            # Exploratory EDA & experimental Model B v2 (not deployed)
├── MLflow.ipynb               # MLflow experiment-tracking pipeline (assignment artifact)
├── performance_test.py        # Standalone load/latency test for the deployed app
├── feedback/, .streamlit/     # Misc. asset/config folders
├── requirements.txt
└── LICENSE                    # MIT
```

---

## 🚀 Getting started

### 1. Prerequisites
- Python 3.10+
- [Git LFS](https://git-lfs.github.com/) (the repo tracks `models/modelA.pkl` via LFS — run `git lfs pull` after cloning if the model files look like small text pointers)

### 2. Install dependencies
```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux
pip install -r requirements.txt
```

### 3. Configure Supabase (optional — only needed for the feedback form)
The feedback form on the results page writes to a Supabase table named `feedback` (see `FEEDBACK_TABLE` in `src/config.py`). Create `.streamlit/secrets.toml`:
```toml
SUPABASE_URL = "https://<your-project>.supabase.co"
SUPABASE_KEY = "<your-anon-or-service-key>"
```
If these secrets are missing, every other part of the app still works — only the "Submit Feedback" button will show an error.

### 4. Run the app
```bash
streamlit run Page_1.py
```
Then open the local URL Streamlit prints (default `http://localhost:8501`).

### 5. (Optional) Run the performance test
```bash
pip install requests
python performance_test.py --url http://localhost:8501
```
Checks connectivity, latency distribution, concurrent/sustained load, and local model-inference speed against the thresholds defined in `TARGETS`.

---

## 🔄 How a request flows through the app

1. **`Page_1.py`** collects the 5 lifestyle sliders into `st.session_state` (keys listed in `PAGE1_KEYS`) and routes to `pages/Page_2.py`.
2. **`pages/Page_2.py`** validates that step 1 was completed, collects the stress/mental-health ratings, converts each `"Very Low"…"Very High"` rating to a `0.0–10.0` score via `RATING_TO_SCORE`, stores everything in session state (`ALL_INPUT_KEYS`), and routes to `pages/result.py`.
3. **`pages/result.py`**:
   - Loads all 5 model artifacts once via `@st.cache_resource` (`src/models.py::load_models`).
   - Calls `predict_burnout()` — maps the categorical stress level through `STRESS_MAPPING_A`, builds a 10-feature row, runs it through the cloudpickled `pipeline_a` (feature engineering) and then `model_a` (XGBoost) to get a class + probabilities + gauge score.
   - Calls `predict_gpa()` — maps stress through `stress_encoder_b`, clamps each lifestyle value to the ranges Model B was trained on (substituting the training mean for out-of-range inputs — see ⚠️ note below), and runs `model_b` (GradientBoosting) to get a GPA.
   - Renders the gauge, GPA ring, radar chart, probability bars, and an animated insight text (`INSIGHTS` in `config.py`, keyed by burnout class).
   - Optionally submits the user's rating/comment + full prediction context to Supabase.

---

## ⚠️ Known quirks & limitations (read before relying on the numbers)

- **GPA-input clamping vs. slider ranges.** Model B was trained on a narrower range of habits than the sliders allow (e.g. `study_hours` trained range is `[5, 10]` but the slider goes `0–12`). Inputs outside the trained range are **silently replaced by the training-set mean** before being sent to Model B (`B_RANGES` in `src/models.py`). This avoids extrapolation errors, but it does mean the predicted GPA can reflect different numbers than what you entered and the radar chart displays — there is currently no UI indication when this substitution happens.
- **Radar chart scaling.** A few axes (`Exercise`, `ECA`, `Social Life`) are normalized against ranges that don't match the corresponding sliders' max values, so the chart can compress or saturate those axes rather than spanning the full 0–10 scale proportionally to what you can actually input.
- **Class imbalance.** The burnout dataset is heavily skewed toward "Healthy" (~89%); SMOTE is used during training to mitigate this, and Macro-F1 (rather than accuracy) is the primary evaluation metric.
- **Small GPA dataset.** Model B is trained on only ~2,000 rows and explains roughly half of GPA variance (R² ≈ 0.53) — treat its output as a rough estimate, not a precise forecast.
- **Privacy.** Per the in-app privacy notice, your habit/stress inputs are used only for prediction; only the optional feedback (rating + comment + prediction summary) is persisted, and only if you explicitly submit it.

---

## 🛠️ Tech stack

- **App / UI:** Streamlit, custom CSS/HTML/JS injection, Plotly
- **ML:** scikit-learn, XGBoost, joblib/cloudpickle
- **Data tracking:** MLflow (see `MLflow.ipynb`)
- **Storage:** Supabase (feedback only)
- **Testing:** a custom `requests`-based performance/load test script

See `requirements.txt` for pinned versions.

---

## 👥 Team

Group 3 — Andrew / Raynald / Adrian

## 📄 License

[MIT](LICENSE) © 2026 Endru180
