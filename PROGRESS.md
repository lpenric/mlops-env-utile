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
Résultat :

✅ Modèle entraîné (MAE ~8.5, R² ~0.85)
✅ API répond correctement : {"uhi_score": 78.06}
✅ Documentation auto sur http://localhost:8000/docs

Captures :

 Screenshot /docs
 Screenshot terminal make smoke

## Session du 14 octobre 2025 - S2
- Repo Git initialisé ✅
- .gitignore configuré (résolution problème EOF) ✅
- Premier commit + push GitHub ✅
- URL publique : https://github.com/lpenric/mlops-env-utile ✅
- 5 artefacts S2 générés (Anki, Quiz, Contexte, Compréhension, Portfolio) ✅
- Prochain pas : S3 (tests pytest + validation Pydantic)


