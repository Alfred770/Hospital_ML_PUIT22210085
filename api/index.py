import os
import joblib
import pandas as pd

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI(title="Hospital Heart Disease Prediction API")

# Locate project folders
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR, "models", "hospital_heart_disease_model.pkl"
)

PUBLIC_DIR = os.path.join(BASE_DIR, "public")

# Load the trained model and preprocessor
model_package = joblib.load(MODEL_PATH)

model = model_package["model"]
preprocessor = model_package["preprocessor"]
features = model_package["features"]


# Patient input structure
class PatientData(BaseModel):
    age: int
    sex: str
    blood_pressure: float
    cholesterol: float
    bmi: float
    smoker: str
    diabetes: str
    physical_activity: float
    family_history: str
    stress_level: float


# Serve the website
@app.get("/")
def home():
    return FileResponse(os.path.join(PUBLIC_DIR, "index.html"))


@app.get("/style.css")
def get_styles():
    return FileResponse(os.path.join(PUBLIC_DIR, "style.css"))


@app.get("/script.js")
def get_script():
    return FileResponse(os.path.join(PUBLIC_DIR, "script.js"))


# Prediction endpoint
@app.post("/api/predict")
def predict_heart_disease(patient: PatientData):

    patient_data = pd.DataFrame([patient.model_dump()])

    patient_data = patient_data[features]

    processed_data = preprocessor.transform(patient_data)

    prediction = model.predict(processed_data)[0]

    probability = model.predict_proba(processed_data)[0][1]

    return {
        "prediction": int(prediction),
        "result": (
            "Heart disease detected"
            if prediction == 1
            else "No heart disease detected"
        ),
        "probability": round(float(probability) * 100, 2),
        "disclaimer": ("This application is developed solely for academic and educational purposes only.")
    }