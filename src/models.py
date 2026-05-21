"""Model loading and prediction logic."""

import streamlit as st
import pandas as pd
import joblib
import numpy as np

from src.features import patch_main
from src.config import (
    STRESS_MAPPING_A,
    MODEL_A_BASE_FEATURES,
    BURNOUT_CLASSES,
    BURNOUT_SCORE_WEIGHTS,
    MODEL_B_BASE_FEATURES,
    GPA_LABELS,
)


@st.cache_resource
def load_models():
    """Load all model artifacts from models/ directory. Cached across reruns."""
    try:
        patch_main()
        return {
            "model_a": joblib.load("models/modelA.pkl"),
            "model_b": joblib.load("models/modelB.pkl"),
            "pipeline_a": joblib.load("models/pipeline_a.pkl"),
            "burnout_class_map": joblib.load("models/burnout_class_mapping.pkl"),
            "stress_encoder_b": joblib.load("models/stress_level_encoder_modelB.pkl"),
        }
    except Exception as e:
        st.error(f"Failed to load models: {e}")
        return None


def predict_burnout(inputs: dict, models: dict) -> dict:
    """Run Model A burnout classification.

    Parameters
    ----------
    inputs : dict with keys matching session state (study_hours, stress_level_category, …)
    models : dict returned by load_models()

    Returns
    -------
    dict with keys: class_id, class_name, probabilities, score (0-100)
    """
    stress_val = STRESS_MAPPING_A[inputs["stress_level_category"]]

    row = {
        "study_hours_per_day": inputs["study_hours"],
        "sleep_hours": inputs["sleep_hours"],
        "exam_pressure": inputs["exam_pressure"],
        "stress_level": stress_val,
        "financial_stress": inputs["financial_stress"],
        "social_support": inputs["social_support"],
        "anxiety_score": inputs["anxiety_score"],
        "depression_score": inputs["depression_score"],
        "family_expectation": inputs["family_expectation"],
        "physical_activity": inputs["physical_hours"],
    }
    df = pd.DataFrame([row], columns=MODEL_A_BASE_FEATURES)

    engineered = models["pipeline_a"](df)
    class_id = int(models["model_a"].predict(engineered)[0])
    proba = models["model_a"].predict_proba(engineered)[0]

    weights = np.array(BURNOUT_SCORE_WEIGHTS, dtype=float)
    score = float(np.dot(proba, weights))
    score = round(max(0.0, min(100.0, score)), 1)

    return {
        "class_id": class_id,
        "class_name": BURNOUT_CLASSES.get(class_id, "Unknown"),
        "probabilities": proba.tolist(),
        "score": score,
    }


def predict_gpa(inputs: dict, models: dict) -> dict:
    """Run Model B GPA regression.

    Returns
    -------
    dict with keys: gpa, label
    """
    stress_val = models["stress_encoder_b"][inputs["stress_level_category"]]

    # Clamp out-of-range inputs to training mean (silent fallback)
    B_RANGES = {
        "study_hours":   (5.0, 10.0, 7.48),
        "sleep_hours":   (5.0, 10.0, 7.50),
        "eca_hours":     (0.0,  4.0, 1.99),
        "social_hours":  (0.0,  6.0, 2.70),
        "physical_hours":(0.0, 11.0, 4.33),
    }

    def clamp(key):
        lo, hi, mean = B_RANGES[key]
        val = inputs[key]
        return mean if (val < lo or val > hi) else val

    row = {
        "study_hours":    clamp("study_hours"),
        "eca_hours":      clamp("eca_hours"),
        "sleep_hours":    clamp("sleep_hours"),
        "social_hours":   clamp("social_hours"),
        "physical_hours": clamp("physical_hours"),
        "stress_level":   stress_val,
    }
    df = pd.DataFrame([row], columns=MODEL_B_BASE_FEATURES)

    gpa = round(float(models["model_b"].predict(df)[0]), 2)
    gpa = max(0.0, min(4.0, gpa))

    label = GPA_LABELS[-1][1]
    for threshold, lbl in GPA_LABELS:
        if gpa >= threshold:
            label = lbl
            break

    return {"gpa": gpa, "label": label}
