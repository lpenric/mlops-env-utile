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

---

## Session du 19 octobre 2025 

### ✅ S3 - Test fumigène (pytest) & schéma Pydantic (VALIDÉE)

**Actions réalisées** :
- Création tests/test_smoke.py (3 tests)
- Validation Pydantic stricte (Field ge/le)
- Tests pytest : 3 passed in 0.11s
- Alias `mlops` créé

**Résultat** :
- ✅ 3 passed in 0.11s → API testée automatiquement.

**Apprentissages clés** :
- pytest découvre test_*.py automatiquement
- Pydantic Field(ge=, le=) = validation auto
- lsof -ti:8000 | xargs kill -9 = tuer processus
- Git : chemins relatifs vs absolus
- git reflog = récupérer commits "perdus"

**Obstacles résolus** :
- Rebase accidentel → git rebase --abort + git reset --hard
- Commit incomplet → git commit --amend

**Prochaine pas** : S4 (MLflow **Tracking**)

---

## Session du 24 octobre 2025

### ✅ S4 — MLflow Tracking

**Artefacts créés** :
- `services/uhi_service/src/train.py` (intégration MLflow)
- `docs/screenshots/s4_mlflow_runs.png`
- Dossier `./mlruns/0/` avec 4 runs

**Commandes clés** :
```bash
make train SERVICE=uhi_service  # Runs multiples
mlflow ui --port 5000           # Interface web
http://127.0.0.1:5000           # URL fonctionnelle
```

**ésultats** :
- **4 runs** enregistrés (2 complets, 2 tests)
- **Params loggués** : max_depth (10 vs 15), n_estimators (50), test_size (0.2)
- **Metrics loggués** : mae (~4.74-4.75), r2_score (~0.746-0.749)
- **Interface MLflow UI** : accessible et fonctionnelle

**Leçons apprises** :
- Reset MLflow : `rm -rf mlruns` puis `make train` (recréation auto)
- URL MLflow : utiliser `127.0.0.1` au lieu de `localhost`
- Runs persistants : MLflow garde tout l'historique

**Prochain pas** : S5 — **Model Registry** (Staging/Prod)

---

