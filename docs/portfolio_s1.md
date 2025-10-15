# Portfolio MLOps — Artefacts livrables

**Dernière mise à jour** : 10 octobre 2025  
**Semaines complétées** : 1/16

---

## Artefacts techniques (preuve sociale)

| # | Artefact | Semaine | Statut | Lien/Capture | Pitch client (1 phrase) |
|---|----------|---------|--------|--------------|--------------------------|
| 1 | API ML (UHI) | S1 | ✅ | docs/screenshots/s1_api_overview.png | API prédiction îlots chaleur, <50ms, documentation interactive |

---

## Compétences démontrées (par catégorie)

### MLOps (S1-S8)
- [x] API REST (FastAPI) + validation Pydantic
- [x] Entraînement modèle (scikit-learn)
- [x] Persistence (joblib, .pkl)
- [x] Documentation visuelle (screenshots)
- [ ] Tests automatisés (pytest) — S3
- [ ] MLflow Tracking — S4
- [ ] Model Registry + promotion — S5
- [ ] Rollback opérationnel — S6
- [ ] Monitoring (Evidently) + data quality (GX) — S7
- [ ] SLO + Runbooks — S8

### GIS (S9-S12)
- [ ] Conversion raster → COG
- [ ] Tiles XYZ (TiTiler)
- [ ] Cartes Leaflet interactives
- [ ] Pipeline tiles → infer → vector

### geoIA (S13-S16)
- [ ] Segmentation (U-Net)
- [ ] Métriques spatiales (IoU, F1)
- [ ] Optimisation latence/coût
- [ ] Vectorisation masques

### Business (S15-S16)
- [ ] MODEL_CARD.md (2+)
- [ ] Études de cas (2+)
- [ ] Vidéos démo (promo/rollback, carte)
- [ ] Offres packagées (3)

---

## Métriques clés (à jour)

| Métrique | Valeur actuelle | Cible S16 |
|----------|-----------------|-----------|
| Services ML en prod | 1 (UHI) | 2 |
| Tests automatisés | 0 | 5+ |
| Cartes GIS livrables | 0 | 2+ |
| PoC geoIA | 0 | 1 |
| Offres commerciales | 0 | 3 |

---

## Pitch 30 secondes (évolutif)

**Version S1** :

"Je suis Enric, spécialisé MLOps environnement/GIS. J'ai livré une API de prédiction des îlots de chaleur urbains avec FastAPI : temps de réponse <50ms, documentation interactive automatique, et preuves visuelles (screenshots). Mon approche : anti-commodité, focus production rapide (5 jours), livrables concrets. Actuellement en formation accélérée vers missions freelance MLOps."

---

## Détail des artefacts S1

### 1. API ML UHI (Îlots de Chaleur Urbains)

**Valeur client** : Identification rapide des zones urbaines à risque de surchauffe

**Composants livrés** :
- Modèle RandomForest entraîné (MAE ~8.5, R² ~0.85)
- API REST 3 endpoints : `/`, `/healthz`, `/predict`
- Schéma Pydantic pour validation automatique
- Documentation Swagger UI (http://localhost:8000/docs)
- Makefile automation (train, serve, smoke)
- Screenshots documentés (overview, schema, response)

**Stack technique** : Python 3.10, FastAPI, scikit-learn, joblib, Pydantic

**Temps de développement** : ~2h (setup + code + tests + documentation)

**Preuve** : 
- Capture d'écran Swagger UI
- Test fumigène OK : `{"uhi_score": 78.06}`
- README avec instructions claires

---

**Fin du portfolio — Version 1.0 (post-S1)**  
Prochain update : après validation S2 (Git/GitHub)