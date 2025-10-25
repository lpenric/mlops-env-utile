# Portfolio MLOps — Artefacts livrables

**Dernière mise à jour** : 24 octobre 2025  
**Semaines complétées** : 4/16

---

## Artefacts techniques (preuve sociale)

| # | Artefact | Semaine | Statut | Lien/Capture | Pitch client (1 phrase) |
|---|----------|---------|--------|--------------|--------------------------|
| 1 | API ML (UHI) | S1 | ✅ | docs/screenshots/s1_api_predict.png | API prédiction îlots chaleur, <50ms, doc auto Swagger |
| 2 | Repo GitHub | S2 | ✅ | github.com/[user]/mlops_env_utile | Code versionné, README pro, instructions claires |
| 3 | Tests pytest | S3 | ✅ | docs/screenshots/s3_pytest_success.png | 3 tests automatisés (health, predict valide/invalide), validation Pydantic |
| 4 | MLflow Tracking | S4 | ✅ | docs/screenshots/s4_mlflow_runs.png | Traçabilité complète des expérimentations, comparaison runs, rollback possible |

---

## Compétences démontrées (par catégorie)

### MLOps (S1-S8)
- [x] API REST (FastAPI) + validation Pydantic — S1, S3
- [x] Entraînement modèle (scikit-learn RandomForest) — S1
- [x] Persistence (joblib, .pkl) — S1
- [x] Tests automatisés (pytest) — S3
- [x] **MLflow Tracking (runs, params, metrics, artifacts)** — S4 ✅
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
| Services ML en prod | 1 (API UHI) | 2 |
| Tests automatisés | 3 (pytest) | 5+ |
| Runs MLflow | 4 | 10+ |
| Modèles en Registry | 0 | 2 |
| Cartes GIS livrables | 0 | 2+ |
| PoC geoIA | 0 | 1 |
| Offres commerciales | 0 | 3 |
| Commits GitHub | ~20 | 50+ |

---

## Pitch 30 secondes (évolutif)

**Version S4** :

"Je suis Enric Lapa, spécialisé MLOps environnement/GIS. J'ai livré 4 artefacts majeurs : une API de prédiction (îlots de chaleur urbains), des tests automatisés, et un système de traçabilité MLflow qui enregistre toutes les expérimentations. Mon approche : anti-commodité, focus production rapide (mise en prod en 5 jours), preuves visuelles. Actuellement disponible pour missions MLOps courtes (monitoring, runbooks, API ML)."

**Points clés à ajuster selon l'audience** :
- **Clients environnement/collectivités** : Insister sur "îlots de chaleur", "données géographiques", "cartes interactives" (à venir S9-S12)
- **Clients tech/startups** : Insister sur "rollback 1-click", "monitoring de dérive", "SLO documentés" (à venir S6-S8)
- **Freelance généraliste** : Insister sur "livraison rapide", "documentation complète", "tests automatisés"

---

## Prochains jalons portfolio

### S8 (fin phase MLOps Ops)
**Artefacts à ajouter** :
- Vidéo 60-90s (promotion/rollback modèle)
- SLO.md + RUNBOOK_ROLLBACK.md
- Rapport drift HTML (Evidently)

**Nouveau pitch S8** : Ajouter "système de rollback 1-click en cas de régression" + "monitoring automatique de dérive de données"

### S12 (fin phase GIS)
**Artefacts à ajouter** :
- Carte Leaflet interactive (raster + vecteur)
- Pipeline tiles→infer→vector fonctionnel

**Nouveau pitch S12** : Ajouter "cartes web interactives pour visualiser les prédictions" + "pipeline géospatial automatisé"

### S16 (fin parcours)
**Artefacts à ajouter** :
- 2 MODEL_CARD.md (UHI + flood/solar)
- 2 études de cas client
- 3 offres packagées

**Pitch final S16** : Version complète incluant "geoIA pour détection automatique sur images satellites" + "portfolio de 10+ artefacts livrables"

---

## Différenciation (anti-commodité)

**Ce qui te distingue déjà (S4)** :
- ✅ **Pas de Docker/K8s prématuré** : API locale solide avant infra complexe
- ✅ **Tests dès S3** : validation automatique avant commit (pas de "on teste à la main")
- ✅ **MLflow dès S4** : traçabilité dès le début (pas "on verra plus tard")
- ✅ **Focus environnement** : pas de e-commerce générique, domaine à impact social

**À développer (S5-S16)** :
- Preuves visuelles (cartes GIS, vidéos démo)
- SLO documentés (contrats de service clairs)
- Runbooks opérationnels (pas juste du code, mode d'emploi pour clients)

---

**Fin du portfolio S4**  
Prochain update : après S8 (porte GO/NO-GO #2)