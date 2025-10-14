"""
Entraînement d'un modèle simple (régression) pour prédire un score UHI.
Utilise des données synthétiques pour démarrer.
"""
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os

def generate_synthetic_data(n_samples=1000):
    """Génère des données synthétiques pour UHI (Îlots de chaleur)."""
    np.random.seed(42)
    
    # Features : NDVI, densité bâtie, distance eau
    ndvi = np.random.uniform(0.1, 0.8, n_samples)  # Végétation
    building_density = np.random.uniform(0.0, 1.0, n_samples)  # Bâti
    water_distance = np.random.uniform(0, 5000, n_samples)  # Distance eau (m)
    
    # Target : score UHI (0-100) - plus de bâti + moins de végétation = chaleur
    uhi_score = (
        50 +
        building_density * 30 +
        (1 - ndvi) * 20 +
        np.random.normal(0, 5, n_samples)  # Bruit
    )
    uhi_score = np.clip(uhi_score, 0, 100)
    
    df = pd.DataFrame({
        'ndvi': ndvi,
        'building_density': building_density,
        'water_distance': water_distance,
        'uhi_score': uhi_score
    })
    
    return df

def train_model():
    """Entraîne un modèle de régression."""
    print("📊 Génération des données synthétiques...")
    df = generate_synthetic_data(n_samples=1000)
    
    X = df[['ndvi', 'building_density', 'water_distance']]
    y = df['uhi_score']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print("🤖 Entraînement du modèle...")
    model = RandomForestRegressor(n_estimators=50, random_state=42, max_depth=10)
    model.fit(X_train, y_train)
    
    # Évaluation
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"✅ Entraînement terminé !")
    print(f"   MAE : {mae:.2f}")
    print(f"   R² : {r2:.3f}")
    
    # Sauvegarde
    os.makedirs('services/uhi_service/models', exist_ok=True)
    model_path = 'services/uhi_service/models/uhi_model_v1.pkl'
    joblib.dump(model, model_path)
    print(f"💾 Modèle sauvegardé : {model_path}")
    
    return model

if __name__ == '__main__':
    train_model()
