# CONTEXTE_CHAT.md — État du parcours MLOps

**Dernière mise à jour** : 10 octobre 2025  
**Semaines validées** : S1 ✅  
**Prochaine semaine** : S2 (Git/GitHub & README propre)  
**Objectif final** : Freelance MLOps anti-commodité (environnement/GIS/geoIA) en 16 semaines

---

## 🎯 Profil de l'apprenant

- **Nom/Pseudo** : enriclapa
- **Matériel** : Mac mini M1, 16 Go RAM
- **OS** : macOS (architecture arm64)
- **Environnement** : 
  - Miniforge (conda-forge ARM natif)
  - Environnement conda : `mlops` (Python 3.10.18)
  - Dossier projet : `~/mlops_env_utile`
- **Niveau de départ** : Débutant total en MLOps
- **Rythme** : 10-12h/semaine (4-5 jours, 25-45 min/jour)
- **Objectif** : Missions freelance orientées environnement/prévention/utilité publique

---

## ✅ Semaines complétées

### S1 — Mini-labo "Hello MLOps" (✅ Validée le 10 octobre 2025)

**Objectif** : Entraîner un modèle simple + exposer une API `/predict` + test fumigène.

#### Artefacts créés

```
mlops_env_utile/
├── services/
│   └── uhi_service/                    # Service Îlots de Chaleur Urbains
│       ├── src/
│       │   ├── __init__.py
│       │   └── train.py                # Entraînement RandomForest (données synthétiques)
│       ├── app/
│       │   ├── __init__.py
│       │   └── main.py                 # API FastAPI (endpoints /predict, /healthz, /)
│       └── models/
│           └── uhi_model_v1.pkl        # Modèle sauvegardé (joblib)
├── docs/
│   ├── screenshots/                    # Preuves visuelles ✅
│   │   ├── s1_api_overview.png
│   │   ├── s1_predict_schema.png
│   │   └── s1_predict_response.png
│   ├── PROMPT_COMBO_5_LIVRABLES.md    # Template réutilisable S2-S16
│   └── CONTEXTE_CHAT_S1.md            # Ce fichier
├── environment.yml                      # Dépendances conda + pip
├── Makefile                             # Commandes train/serve/smoke/check-env
├── README.md                            # Documentation + captures
└── PROGRESS.md                          # Suivi session par session
```

#### Commandes clés maîtrisées

```bash
conda activate mlops                    # Activer l'environnement
make check-env                          # Vérifier setup (ML + GEO)
make train SERVICE=uhi_service          # Entraîner le modèle
make serve SERVICE=uhi_service          # Lancer API (port 8000)
make smoke SERVICE=uhi_service          # Test curl automatique
```

#### Modèle UHI v1 (Îlots de Chaleur Urbains)

**Type** : Régression (RandomForestRegressor)  
**Features** : 
- `ndvi` (float 0-1) : indice de végétation
- `building_density` (float 0-1) : densité bâtie
- `water_distance` (float mètres) : distance à l'eau

**Target** : `uhi_score` (0-100, score de chaleur urbaine)

**Métriques (données synthétiques)** :
- MAE : ~8.5
- R² : ~0.85
- Latence : <50ms/requête

**Exemple de prédiction validée** :
```json
POST /predict
{
  "ndvi": 0.5,
  "building_density": 0.7,
  "water_distance": 1000
}

→ Response 200
{
  "uhi_score": 78.06
}
```

#### API FastAPI

**Endpoints disponibles** :
- `GET /` : Message de bienvenue + statut
- `GET /healthz` : Health check (vérifie modèle chargé)
- `POST /predict` : Prédiction UHI (body JSON validé par Pydantic)

**Documentation auto** : http://localhost:8000/docs (Swagger UI)

**Schéma Pydantic** :
```python
class UHIInput(BaseModel):
    ndvi: float
    building_density: float
    water_distance: float

class UHIOutput(BaseModel):
    uhi_score: float
```

#### Preuves visuelles (screenshots documentés)

✅ **3 captures d'écran intégrées dans README** :
- `s1_api_overview.png` : Vue d'ensemble `/docs`
- `s1_predict_schema.png` : Schéma Pydantic (Input/Output)
- `s1_predict_response.png` : Réponse JSON live

**Différenciateur** : Preuve sociale immédiate (client voit directement ce qu'il recevra)

#### Points d'attention S1

✅ **Ce qui fonctionne** :
- Environnement conda stable (ML + GEO OK)
- Pipeline train → serve → smoke complet
- API répond correctement, latence acceptable
- Documentation Swagger UI accessible
- Screenshots documentés et versionnés

⚠️ **Warning mineur** (non bloquant) :
```
UserWarning: X does not have valid feature names, but RandomForestRegressor was fitted with feature names
```
**Cause** : Features passées comme liste (`[[...]]`) au lieu de DataFrame avec noms de colonnes.  
**Impact** : Aucun (prédiction fonctionne).  
**Correction prévue** : S3 (tests + validation stricte).

---

## 🔧 Écarts vs PLAN_MAITRE.md

| Élément | Plan initial | Réalisé | Raison | Impact |
|---------|--------------|---------|--------|--------|
| **TiTiler** | v0.14.2 | Pas installé | Version inexistante sur PyPI (dernière = 0.24.0) | ⚠️ Aucun (utilisé en S9-S12 seulement) |
| **MLflow** | Activé S4 | Pas encore activé | Ordre du plan respecté (S1 → API d'abord) | ✅ Normal |
| **Docker/K8s** | Jamais avant S8 | Non abordé | Conformité au plan (infra locale d'abord) | ✅ Normal |
| **Tests pytest** | S3 | Pas encore implémenté | Ordre respecté (S1 = smoke curl seulement) | ✅ Normal |
| **Screenshots** | Suggéré, pas obligatoire | ✅ Implémenté (3 captures) | Initiative personnelle (preuve sociale) | ✅ Bonus ++ |

**Décisions techniques validées** :
- ✅ Utilisation exclusive de **conda-forge** pour GDAL/Rasterio (ARM natif)
- ✅ Makefile comme interface unique (évite commandes uvicorn/python complexes)
- ✅ Données synthétiques pour valider le workflow (vraies données en S9+)
- ✅ Un seul service pour l'instant (2e service prévu en S13)
- ✅ Documentation visuelle (screenshots) = différenciateur portfolio

---

## 🚧 Blocages rencontrés & solutions

### Blocage #1 : `make check-env` → "No rule to make target"
**Cause** : Commande lancée hors du dossier projet (Makefile absent).  
**Solution** : `cd ~/mlops_env_utile` avant toute commande `make`.  
**Prévention** : Toujours vérifier `pwd` si erreur Make.

### Blocage #2 : `conda env update` échoue sur `titiler==0.14.2`
**Cause** : Version inexistante (0.14.2 n'a jamais été publiée sur PyPI).  
**Solution** : Ignoré pour S1-S8 (TiTiler pas nécessaire avant S9).  
**Action future** : Installer `titiler==0.24.0` en S9 si besoin de tiles.

### Blocage #3 (potentiel, non rencontré) : Port 8000 déjà utilisé
**Symptôme** : `uvicorn` échoue au démarrage.  
**Solution** : 
```bash
# Changer de port
make serve PORT=8001

# Ou tuer le processus existant
lsof -ti:8000 | xargs kill
```

---

## 📊 KPIs & Portes GO/NO-GO

### ✅ Porte #1 (S4) — Conditions

| Critère | Statut | Validation |
|---------|--------|------------|
| API `/predict` fonctionnelle | ✅ | Test smoke OK (78.06) |
| Test fumigène passe | ✅ | `make smoke` retourne JSON |
| 1 run MLflow loggué | ⏳ | Prévu S4 (normal) |
| README clair | ✅ | Instructions + screenshots |

**Verdict** : **S1 validée**, sur les rails pour S2-S4.

---

## 🗣️ Vocabulaire technique acquis

| Terme | Définition courte | Contexte d'usage S1 |
|-------|-------------------|---------------------|
| **Artifact** | Fichier produit par un processus ML (modèle, rapport, graphique) | `uhi_model_v1.pkl` est un artifact |
| **Endpoint** | URL d'une API exposant une fonction (GET/POST/etc.) | `/predict`, `/healthz` sont des endpoints |
| **Pydantic** | Bibliothèque Python de validation de données via classes typées | `UHIInput` valide le JSON reçu |
| **Joblib** | Outil de sérialisation Python optimisé pour objets scientifiques | `joblib.dump(model, path)` sauvegarde le RF |
| **Uvicorn** | Serveur ASGI pour exécuter FastAPI (asynchrone, performant) | Lance l'API via `python -m uvicorn ...` |
| **Swagger UI** | Interface web auto-générée pour tester une API REST | Accessible sur `/docs` |
| **MAE** | Mean Absolute Error (erreur absolue moyenne), métrique de régression | Mesure la précision du modèle UHI |
| **conda-forge** | Canal conda communautaire avec packages scientifiques ARM64 | Seul moyen fiable d'installer GDAL sur Mac M1 |

---

## 🚀 Prochaines actions (S2)

### Objectif S2 : Git/GitHub & README propre

**Livrables** :
1. Repo Git initialisé (`.git/`)
2. `.gitignore` configuré (exclut `.pkl`, `__pycache__`, `mlruns/`)
3. Premier commit ("S1: Premier service MLOps UHI")
4. Repo GitHub public créé
5. Code pushé, README visible en ligne

**Durée estimée** : 15 min  
**Difficulté** : Facile (commandes Git de base)

**Checklist S2** :
```bash
cd ~/mlops_env_utile
git init
git branch -M main

# Créer .gitignore (exclut modèles lourds, MAIS PAS screenshots)
cat > .gitignore << 'EOF'
__pycache__/
*.py[cod]
*.pkl
*.h5
mlruns/
services/*/models/
services/*/data/
.DS_Store
.pytest_cache/
EOF

git add .
git commit -m "S1: Premier service MLOps (UHI prediction API + screenshots)"

# Créer repo GitHub
# Option A: Interface web https://github.com/new
# Option B: CLI (si gh installé): gh repo create mlops-env-utile --public --source=. --remote=origin

# Push
git remote add origin https://github.com/enriclapa/mlops-env-utile.git
git push -u origin main
```

**Validation S2** :
- ✅ README.md s'affiche sur la page d'accueil GitHub
- ✅ Fichiers `.pkl` ne sont PAS versionnés (vérifier sur GitHub)
- ✅ Screenshots SONT versionnés (docs/screenshots/ visible)
- ✅ Structure de dossiers visible et claire

---

## 🧠 Points à retenir pour l'assistant

### Règles strictes (non-négociables)

1. **Conda-forge obligatoire** : JAMAIS `pip install gdal/rasterio` sur Mac M1 (binaires incompatibles).
2. **Pas de Docker/K8s** avant S8 : focus sur API locale stable d'abord.
3. **Commandes runnable** : tout code doit pouvoir être copié/collé et exécuté immédiatement.
4. **Conformité PLAN_MAITRE.md** : signaler tout écart, expliquer pourquoi, proposer correction.
5. **Format réponse standard** : Résumé → Checklist → Test & Validation → À retenir → Prochaines actions.

### Préférences pédagogiques

- **Langage clair** : éviter jargon, utiliser images mentales courtes.
- **Ancrage valeur client** : toujours relier technique à bénéfice métier (fiabilité, rollback, carte lisible).
- **Pas de "on verra plus tard"** : donner un plan exécutable maintenant, même si simplifié.
- **Protocole SOS** : si blocage >10 min, demander log complet + OS + commande exacte.

### Contexte matériel critique

- **Architecture** : arm64 (Apple Silicon M1)
- **Conda** : Miniforge (`/Users/enriclapa/miniforge3`)
- **Python** : 3.10.18 (dans env `mlops`)
- **Répertoire de travail** : `~/mlops_env_utile`

### Packages critiques installés

**ML/API** :
- numpy, pandas, scikit-learn, mlflow
- fastapi, uvicorn, pydantic
- pytest, requests, joblib

**GIS** (ARM64 via conda-forge) :
- gdal, rasterio, rioxarray
- shapely, pyproj, geopandas

**Monitoring** :
- evidently (0.4.33)
- great_expectations (1.0.3)

**Manquants (prévus plus tard)** :
- titiler (S9, installer v0.24.0)
- MLflow UI activé (S4)
- Tests pytest structurés (S3)

---

## 🎯 Indicateurs de réussite globale

| Indicateur | Valeur actuelle | Cible S16 |
|------------|-----------------|-----------|
| **Semaines validées** | 1/16 (6.25%) | 16/16 (100%) |
| **Services ML en prod** | 1 (UHI) | 2 (UHI + flood/autre) |
| **Tests automatisés** | 0 | 5+ (smoke, unit, integration) |
| **Artefacts MLflow** | 0 runs | 10+ runs loggués |
| **Cartes GIS livrables** | 0 | 2+ (raster + vector + interactives) |
| **PoC geoIA fonctionnel** | 0 | 1 (tiles → infer → vector → carte) |
| **Offres packagées** | 0 | 3 (MLOps Starter, Carte citoyenne, geoIA PoC) |
| **Prospects contactés** | 0 | 5+ (emails envoyés) |

---

## 💼 Portfolio & Go-to-Market (état actuel)

### Services à développer (roadmap)

1. **ML#1 : UHI Service** (S1 ✅)
   - Prédiction score îlots de chaleur urbains
   - Features : NDVI, densité bâtie, distance eau
   - Statut : API fonctionnelle, données synthétiques

2. **ML#2 : Flood Service** (S13)
   - Score d'exposition aux inondations
   - Features : MNT/élévation, distance rivière, imperméabilisation
   - Statut : À développer

3. **geoIA PoC : Toitures solaires** (S11-S12)
   - Segmentation orthophoto → surfaces propices
   - Pipeline : tiles → U-Net → vectorisation → carte
   - Statut : À développer

### Offres commerciales (à créer S15-S16)

| Offre | Durée | Prix indicatif | Contenu |
|-------|-------|----------------|---------|
| MLOps Starter | 5 jours | 3-4,5k€ | API + Registry + Monitoring + SLO |
| Carte citoyenne | 10 jours | 5-7k€ | Analyse spatial + viz Leaflet + rapport |
| geoIA PoC | 15-21j | 9-12k€ | Segmentation custom + métriques + carte |
| Rétention mensuelle | - | 1,2-1,8k€/mois | Monitoring, rapports, ajustements |

**Positionnement différenciant** :
- Anti-commodité (pas de templates génériques)
- Focus environnement/prévention/utilité publique
- Livraison rapide (1-3 semaines)
- Preuve visuelle (cartes, vidéos 90s, runbooks, screenshots)

---

## 📝 Notes de session (historique)

### Session du 10 octobre 2025

**Durée** : ~2h (setup + dev + doc + consolidation)  
**Énergie** : ⭐⭐⭐⭐⭐ (excellente)  
**Obstacles** : Aucun blocage majeur

**Progression** :
1. Vérification environnement existant (conda, mlops) ✅
2. Création structure projet (environment.yml, Makefile, README) ✅
3. Développement service UHI (train.py, main.py) ✅
4. Tests complets (train → serve → smoke) ✅
5. Screenshots documentés (3 captures dans README) ✅
6. Mise en place système de révision (Anki, Quiz, Compréhension, Portfolio, Contexte) ✅

**Apprentissages clés** :
- Importance du Makefile (abstraction des commandes complexes)
- Pydantic pour validation automatique des entrées API
- Données synthétiques = gain de temps énorme pour valider workflow
- `/docs` Swagger UI = outil de debug incontournable
- **Screenshots = différenciateur portfolio** (preuve sociale immédiate)

**Réflexions** :
> "La mise en place du système 5 livrables (Anki + Quiz + Compréhension + Portfolio + Contexte) est un investissement qui va payer sur les 15 semaines restantes. C'est la différence entre 'faire des TPs' et 'construire un portfolio vendable'."

**Décisions** :
- Poursuivre avec S2 (Git/GitHub) prochaine session
- Maintenir le rythme 4-5 sessions/semaine (25-45 min)
- Utiliser le prompt combo 5-en-1 systématiquement après chaque semaine validée
- Révision Anki quotidienne (5 min/jour minimum)

---

## 🔮 Anticipation des risques (semaines à venir)

| Risque | Probabilité | Impact | Parade |
|--------|-------------|--------|--------|
| Sur-ingénierie infra (Docker/K8s trop tôt) | Moyenne | ⚠️⚠️⚠️ | Suivre strictement ordre du PLAN_MAITRE |
| Blocage GDAL/Rasterio (S9) | Faible | ⚠️⚠️ | conda-forge uniquement, tests anticipés |
| Données GIS lourdes (S10-S12) | Moyenne | ⚠️⚠️ | Petites zones test, COG, mesure latence |
| Perfectionnisme (bloquer sur détails) | Élevée | ⚠️⚠️⚠️ | "Shipping > perfection", livrables min viable |
| Perte de motivation (S8-S12) | Moyenne | ⚠️⚠️⚠️ | Preuves visuelles (cartes), vidéos 90s |
| Cycle de vente long (S16+) | Élevée | ⚠️⚠️ | Maintenir missions courtes (monitoring) |

**Stratégie de mitigation générale** :
- Livrables visibles chaque semaine (pas de travail invisible)
- Validation par tests (pas "ça a l'air de marcher")
- Portfolio incrémenté semaine par semaine
- Une technologie à la fois (éviter paralysie du choix)

---

## 🛠️ Commandes de secours (anti-blocage)

### Environnement corrompu
```bash
conda deactivate
conda env remove -n mlops
conda env create -f environment.yml
conda activate mlops
make check-env
```

### API ne démarre pas
```bash
# Vérifier si port occupé
lsof -ti:8000

# Tuer le processus
lsof -ti:8000 | xargs kill -9

# Relancer sur autre port
make serve PORT=8001
```

### Modèle introuvable
```bash
# Vérifier existence
ls -lh services/uhi_service/models/

# Réentraîner
make train SERVICE=uhi_service

# Vérifier chemin dans main.py
grep MODEL_PATH services/uhi_service/app/main.py
```

### Git : conflit ou erreur
```bash
# Annuler dernier commit (avant push)
git reset --soft HEAD~1

# Ignorer changements fichier spécifique
git checkout -- services/uhi_service/models/uhi_model_v1.pkl

# Forcer push (ATTENTION : destructif)
git push -f origin main
```

---

## 📚 Ressources de référence (à consulter si besoin)

### Documentation officielle
- **FastAPI** : https://fastapi.tiangolo.com
- **MLflow** : https://mlflow.org/docs/latest/index.html
- **Scikit-learn** : https://scikit-learn.org/stable/
- **GDAL** : https://gdal.org/
- **Rasterio** : https://rasterio.readthedocs.io/
- **Leaflet** : https://leafletjs.com/

### Conda-forge (Mac M1)
- **GDAL ARM64** : https://anaconda.org/conda-forge/gdal
- **Rasterio ARM64** : https://anaconda.org/conda-forge/rasterio

### Standards MLOps
- **Model Cards** : https://arxiv.org/abs/1810.03993
- **SLO/SLA** : https://sre.google/sre-book/service-level-objectives/

---

## ✅ Checklist de fin de session

Avant de fermer ce chat, l'apprenant devrait avoir :

- [x] Exécuté et validé tous les tests S1 (`make check-env`, `train`, `serve`, `smoke`)
- [x] Pris 3 screenshots (API overview, schema, response)
- [x] Documenté les captures dans README
- [x] Téléchargé/copié les 5 artefacts (Anki CSV, Quiz, Compréhension, Portfolio, CONTEXTE)
- [ ] Importé les cartes Anki et planifié première révision
- [ ] Fait le quiz S1 (optionnel mais recommandé)
- [ ] Fait le test compréhension S1 (validation anti-cargo cult)
- [x] Sauvegardé CONTEXTE_CHAT.md pour la prochaine session
- [ ] Noté dans PROGRESS.md les apprentissages de la session
- [ ] Identifié le créneau de la prochaine session (S2)

---

## 🎯 Message pour le prochain assistant

**Contexte** : L'apprenant a validé S1 (API MLOps fonctionnelle + screenshots). Il démarre S2 (Git/GitHub).

**Attentes** :
1. Lire intégralement ce CONTEXTE_CHAT.md avant toute réponse
2. Respecter le format de réponse (Résumé → Checklist → Test → À retenir → Prochaines actions)
3. Maintenir conformité stricte au PLAN_MAITRE.md
4. Privilégier commandes runnable (copier/coller direct)
5. Signaler tout écart ou ambiguïté

**Prérequis S2** :
- Environnement `mlops` fonctionnel ✅
- Service UHI opérationnel (train/serve/smoke OK) ✅
- Arborescence projet stable ✅
- Screenshots documentés ✅

**Objectif S2** : Repo Git + GitHub public + .gitignore + README visible en ligne.

**Durée estimée** : 15 min

---

**Fin du CONTEXTE_CHAT.md**  
Version : 1.0 (post-S1)  
Prochain update : après validation S2