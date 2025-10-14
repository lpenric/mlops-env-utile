"""
API FastAPI pour prédire le score UHI.
"""
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

app = FastAPI(title="UHI Prediction API", version="1.0")

# Charger le modèle au démarrage
MODEL_PATH = "services/uhi_service/models/uhi_model_v1.pkl"
model = None

@app.on_event("startup")
def load_model():
    global model
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
        print(f"✅ Modèle chargé depuis {MODEL_PATH}")
    else:
        print(f"⚠️  Modèle introuvable : {MODEL_PATH}")

class UHIInput(BaseModel):
    ndvi: float
    building_density: float
    water_distance: float

class UHIOutput(BaseModel):
    uhi_score: float

@app.get("/")
def root():
    return {"message": "UHI Prediction API", "status": "running"}

@app.get("/healthz")
def health():
    return {"status": "ok", "model_loaded": model is not None}

@app.post("/predict", response_model=UHIOutput)
def predict(input_data: UHIInput):
    if model is None:
        return {"error": "Model not loaded"}
    
    # Prédiction
    features = [[input_data.ndvi, input_data.building_density, input_data.water_distance]]
    prediction = model.predict(features)[0]
    
    return {"uhi_score": round(prediction, 2)}
