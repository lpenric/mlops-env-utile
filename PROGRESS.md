# PROGRESS.md — Suivi MLOps (S1→S16)

## Session du 9 octobre 2025

### ✅ S1 — Mini-labo "Hello MLOps" (VALIDÉE)

**Actions réalisées** :
1. Création structure `services/uhi_service/`
2. Implémentation `train.py` (données synthétiques + RandomForest)
3. Implémentation `main.py` (FastAPI + endpoints `/predict`, `/healthz`)
4. Test complet : `make train` → `make serve` → `make smoke`

**Commandes lancées** :
```bash
make train SERVICE=uhi_service
make serve SERVICE=uhi_service  # Terminal 1
make smoke SERVICE=uhi_service  # Terminal 2
```

**Résultat** :
- ✅ Modèle entraîné (MAE ~8.5, R² ~0.85)
- ✅ API répond correctement : `{"uhi_score": 78.06}`
- ✅ Documentation auto sur http://localhost:8000/docs

**Captures** :
- Screenshot `/docs` (Swagger UI)
- Screenshot terminal `make smoke`

**Prochain pas** : S2 (Git/GitHub & README propre)

---

## Session du 14 octobre 2025

### ✅ S2 — Git/GitHub & README propre (VALIDÉE)

**Actions réalisées** :
1. Initialisation repo Git + configuration `.gitignore`
2. Résolution problème `EOF` (typo pattern gitignore)
3. Renommage artefacts S1 (uniformisation : lowercase, sans `_final`)
4. Génération 5 artefacts S2 (Anki, Quiz, Contexte, Compréhension, Portfolio)
5. Premier commit + push GitHub

**Commandes lancées** :
```bash
git init
git branch -M main
# Création .gitignore (exclusion *.pkl, mlruns/, docs/contexte_s*.md)
git add .
git commit -m "docs: ajout S2 + renommage S1 (lowercase, sans _final) + exclusion notes perso"
git remote add origin https://github.com/lpenric/mlops-env-utile.git
git push -u origin main
```

**Résultat** :
- ✅ Repo public accessible : https://github.com/lpenric/mlops-env-utile
- ✅ Artefacts pédagogiques versionnés (Anki, Quiz, Portfolio)
- ✅ Notes personnelles (Contexte) exclues du versioning
- ✅ Nomenclature uniformisée (S1 + S2)

**Captures** :
- Screenshot page GitHub (arborescence `docs/`)
- Vérification absence `contexte_s*.md` sur GitHub

**Prochain pas** : S3 (tests pytest + validation Pydantic stricte)
