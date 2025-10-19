from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import numpy as np
from pathlib import Path

app = FastAPI(title="UHI Service API", version="1.0.0")

# Chargement du modèle
MODEL_PATH = Path(__file__).parent.parent / "models" / "uhi_model_v1.pkl"
model = joblib.load(MODEL_PATH)

class UHIInput(BaseModel):
    """Schéma d'entrée pour prédiction UHI avec validations strictes"""
    ndvi: float = Field(..., ge=-1.0, le=1.0, description="NDVI (Normalized Difference Vegetation Index)")
    building_density: float = Field(..., ge=0.0, le=1.0, description="Densité bâtie [0-1]")
    water_distance: float = Field(..., ge=0.0, description="Distance à l'eau en mètres")

class UHIOutput(BaseModel):
    """Schéma de sortie pour prédiction UHI"""
    uhi_score: float = Field(..., description="Score UHI prédit [0-100]")

@app.get("/")
def root():
    return {"message": "UHI Service API — Prédiction Îlots de Chaleur Urbains"}

@app.get("/healthz")
def healthz():
    return {"status": "healthy", "service": "uhi_service", "version": "1.0.0"}

@app.post("/predict", response_model=UHIOutput)
def predict(input_data: UHIInput):
    """
    Prédire le score UHI à partir des features
    """
    # Conversion en array numpy
    features = np.array([[
        input_data.ndvi,
        input_data.building_density,
        input_data.water_distance
    ]])
    
    # Prédiction
    prediction = model.predict(features)[0]
    
    return {"uhi_score": float(prediction)}
