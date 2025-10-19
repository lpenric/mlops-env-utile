"""
tests/test_smoke.py — Tests fumigènes pour l'API UHI Service
3 tests : healthz, predict valide, predict invalide
"""
import pytest
import requests
from time import sleep

# Configuration
API_BASE_URL = "http://127.0.0.1:8000"

@pytest.fixture(scope="module")
def api_url():
    """Fixture : URL de base de l'API (réutilisable dans tous les tests)"""
    return API_BASE_URL

def test_healthz(api_url):
    """
    Test 1 : Vérifier que l'endpoint /healthz répond 200 OK
    """
    response = requests.get(f"{api_url}/healthz")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "service" in data
    print(f"✅ /healthz OK : {data}")

def test_predict_valid_input(api_url):
    """
    Test 2 : Prédiction avec input VALIDE → doit retourner 200 + uhi_score
    """
    payload = {
        "ndvi": 0.35,
        "building_density": 0.62,
        "water_distance": 450.0
    }
    response = requests.post(f"{api_url}/predict", json=payload)
    
    # Vérifications
    assert response.status_code == 200
    data = response.json()
    assert "uhi_score" in data
    assert isinstance(data["uhi_score"], (int, float))
    assert 0 <= data["uhi_score"] <= 100  # Score UHI dans range attendu
    print(f"✅ /predict valide OK : score={data['uhi_score']:.2f}")

def test_predict_invalid_input(api_url):
    """
    Test 3 : Prédiction avec input INVALIDE → doit retourner 422 Validation Error
    """
    # Input invalide : ndvi hors range [-1, 1]
    payload = {
        "ndvi": 99.9,  # ❌ Invalide (NDVI doit être entre -1 et 1)
        "building_density": 0.5,
        "water_distance": 300.0
    }
    response = requests.post(f"{api_url}/predict", json=payload)
    
    # Pydantic doit rejeter avec 422 Unprocessable Entity
    assert response.status_code == 422
    data = response.json()
    assert "detail" in data  # Message d'erreur de validation
    print(f"✅ /predict invalide OK : rejeté avec 422 (attendu)")
