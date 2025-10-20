# CONTEXTE_CHAT.md — État du parcours MLOps
**Dernière mise à jour** : 19 octobre 2025  
**Semaines validées** : S1 ✅ S2 ✅ S3 ✅  
**Prochaine semaine** : S4 (MLflow Tracking — Logger runs d'entraînement)

---

## ✅ S3 — Tests fumigène (pytest) & Validation Pydantic (✅ 19 oct 2025)

### Artefacts créés
```
tests/
├── __init__.py
└── test_smoke.py  # 3 tests
services/uhi_service/app/main.py  # Field(ge=, le=)
docs/screenshots/s3_pytest_success.png
```

### Commandes clés
```bash
pytest -q tests/test_smoke.py  # 3 passed in 0.11s
pytest -v  # Mode verbose
lsof -ti:8000 | xargs kill -9
git reflog -10
git commit --amend --no-edit
git push --force
```

### Tests pytest
- **3 tests** : healthz (200), predict valide (200 + score), predict invalide (422)
- **Résultat** : `3 passed in 0.11s` ✅

### Validation Pydantic
```python
ndvi: float = Field(..., ge=-1.0, le=1.0)
building_density: float = Field(..., ge=0.0, le=1.0)
water_distance: float = Field(..., ge=0.0)
```
→ FastAPI retourne 422 automatiquement si contraintes non respectées

### Blocages résolus
- Mauvais dossier → `cd ~/mlops_env_utile`
- Port occupé → `lsof -ti:8000 | xargs kill -9`
- Rebase Git → `git rebase --abort` + `git reflog` + `git reset --hard`
- Commit incomplet → `git commit --amend`
- Chemin absolu → `docs/` pas `/docs/`

---

## 🚀 Prochaines actions (S4)

### Objectif S4 : MLflow Tracking

**Livrables** :
1. Modifier `train.py` (ajout `mlflow.start_run()`)
2. 2+ runs loggués dans `./mlruns/`
3. MLflow UI sur http://localhost:5000
4. Screenshot comparaison runs
5. Commit Git

**Durée** : 25-30 min

**Checklist S4** :
```bash
# Modifier train.py : ajouter mlflow.log_param/metric/model
make train SERVICE=uhi_service  # Run #1
# Modifier hyperparams
make train SERVICE=uhi_service  # Run #2
mlflow ui  # Port 5000
# Screenshot
git add services/uhi_service/src/train.py docs/screenshots/s4_*.png
git commit -m "S4: MLflow Tracking"
git push
```

**Validation S4** :
- ✅ `mlflow ui` démarre
- ✅ 2+ runs visibles
- ✅ Params + metrics affichés
- ✅ Artefact "model" téléchargeable

---

## 📊 Indicateurs

| Métrique | Actuel | Cible S16 |
|----------|--------|-----------|
| Semaines | 3/16 | 16/16 |
| Tests auto | 3 | 5+ |
| Runs MLflow | 0 | 10+ |
| Commits GitHub | 12+ | 50+ |

---

## 🗣️ Vocabulaire S3

| Terme | Définition |
|-------|------------|
| **pytest** | Framework test Python (découverte auto test_*.py) |
| **Fixture** | Setup réutilisable (@pytest.fixture) |
| **Field** | Contraintes Pydantic (ge=, le=) |
| **422** | Unprocessable Entity (données invalides) |
| **lsof** | List Open Files (processus sur port) |
| **git reflog** | Historique complet HEAD (récup commits) |
| **git amend** | Modifier dernier commit |

---

**Fin CONTEXTE**  
Version 3.0 (post-S3)  
Prochain update : après S4