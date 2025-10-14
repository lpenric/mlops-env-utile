SHELL := /bin/zsh
CONDA_ENV := mlops
PY := python
PORT ?= 8000
SERVICE ?= uhi_service

.PHONY: check-env train serve smoke test clean

## Vérification environnement
check-env:
	@echo "🔎 Vérification env..."
	$(PY) -c "import platform; print('Python:', platform.python_version(), 'arch:', platform.machine())"
	$(PY) -c "import numpy, sklearn, mlflow, fastapi; print('✅ OK ML: numpy/sklearn/mlflow/fastapi')"
	$(PY) -c "import geopandas, rasterio, osgeo; print('✅ OK GEO: geopandas/rasterio/gdal')"

## Entraînement
train:
	@echo "🚀 Entraînement du modèle $(SERVICE)..."
	$(PY) services/$(SERVICE)/src/train.py

## Servir l'API
serve:
	@echo "🌐 Démarrage de l'API $(SERVICE) sur http://localhost:$(PORT)"
	$(PY) -m uvicorn services.$(SERVICE).app.main:app --host 0.0.0.0 --port $(PORT) --reload

## Test fumigène
smoke:
	@echo "🚬 Test fumigène sur http://127.0.0.1:$(PORT)/predict"
	@sleep 2
	curl -s -X POST http://127.0.0.1:$(PORT)/predict \
	 -H "Content-Type: application/json" \
	 -d '{"ndvi": 0.5, "building_density": 0.7, "water_distance": 1000}' | python -m json.tool

## Tests pytest
test:
	$(PY) -m pytest -q

## Nettoyage
clean:
	rm -rf **/__pycache__ **/*.pyc .pytest_cache
	@echo "🧹 Clean OK."
