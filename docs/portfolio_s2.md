# Portfolio MLOps — Artefacts livrables

**Dernière mise à jour** : 14 octobre 2025  
**Semaines complétées** : 2/16 (12.5%)

---

## Artefacts techniques (preuve sociale)

| # | Artefact | Semaine | Statut | Lien/Capture | Pitch client (1 phrase) |
|---|----------|---------|--------|--------------|--------------------------|
| 1 | API ML (UHI) | S1 | ✅ | [screenshot /docs] | API prédiction îlots chaleur, <50ms, doc auto (Swagger UI) |
| 2 | Repo GitHub public | S2 | ✅ | [github.com/lpenric/mlops-env-utile](https://github.com/lpenric/mlops-env-utile) | Code versionné, README pro, instructions claires, clonable en 10s |

---

## Compétences démontrées (par catégorie)

### MLOps (S1-S8)
- [x] API REST (FastAPI) + validation Pydantic
- [x] Entraînement modèle (scikit-learn)
- [x] Persistence (joblib, .pkl)
- [x] **Versioning Git + repo GitHub public**
- [x] **Configuration .gitignore (exclusion fichiers lourds)**
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
| **Repo GitHub public** | **✅ 1** | **1** |
| **Commits versionnés** | **2** | **50+** |

---

## Pitch 30 secondes (évolutif)

**Version S2** :

"Je suis Enric, spécialisé MLOps environnement/GIS. J'ai livré une API de prédiction (îlots de chaleur urbains) avec validation automatique des données, documentation Swagger intégrée, et repo GitHub public avec historique versionné. Mon approche : anti-commodité, focus production rapide, preuves visuelles (screenshots, README professionnel). Actuellement disponible pour missions MLOps courtes (API, monitoring, setup infrastructure légère)."

**Éléments clés à ajuster en S4** :
- Ajouter "MLflow Tracking + Model Registry"
- Ajouter "rollback 1-click en cas de régression"
- Ajouter "monitoring de dérive des données"

**Éléments clés à ajuster en S8** :
- Ajouter "SLO documentés (P95 latence, MAE cible)"
- Ajouter "runbooks opérationnels"
- Changer disponibilité : "missions 5-10 jours"

**Éléments clés à ajuster en S12** :
- Ajouter "cartes Leaflet interactives (raster + vecteur)"
- Ajouter "pipeline tiles → analyse → vectorisation"
- Changer focus : "environnement + géomatique"

**Éléments clés à ajuster en S16** :
- Ajouter "PoC geoIA (segmentation U-Net, IoU >0.5)"
- Changer disponibilité : "missions 15-21 jours ou rétention mensuelle"
- Ajouter chiffres : "X missions livrées, Y€ générés"

---

## Différenciateurs portfolio (mise à jour S2)

### 🎯 Ce qui te distingue (déjà acquis)

1. **Repo public = vitrine vivante**
   - N'importe qui peut voir ton code (transparence)
   - README avec screenshots (pas besoin d'installer pour comprendre)
   - Historique Git propre (commits clairs, pas de pollution)

2. **Documentation visuelle**
   - 3 screenshots Swagger UI (aperçu, schéma, réponse)
   - Instructions claires (copier/coller direct)
   - Pas de jargon inutile

3. **Code runnable immédiatement**
   - `make check-env` → validation setup
   - `make train && make serve && make smoke` → workflow complet en 3 commandes
   - Pas de "ça marche sur ma machine" (conda-forge ARM64, .gitignore configuré)

### 🚀 À venir (S3-S16)

4. **Tests automatisés** (S3)
   - pytest intégré (pas besoin de tester manuellement)
   - CI/CD préparé (GitHub Actions en S4+)

5. **MLOps complet** (S4-S8)
   - Tracking + Registry + Monitoring + SLO
   - Rollback 1-click (pas de panique si régression)
   - Runbooks opérationnels (pas de "je sais pas comment réparer")

6. **GIS/geoIA** (S9-S16)
   - Cartes interactives (Leaflet + GeoJSON)
   - Pipeline tiles → inférence → vectorisation
   - Métriques spatiales (IoU, F1)

---

## Prochains jalons (roadmap)

| Jalon | Semaine | Livrable principal | Impact portfolio |
|-------|---------|-------------------|------------------|
| **Tests pytest** | S3 | 3 tests automatisés (healthz, predict valide, predict invalide) | Professionnalisme (code testé) |
| **MLflow Tracking** | S4 | 1 run loggué avec métriques + artefacts | Traçabilité (historique expériences) |
| **Model Registry** | S5 | v1 en Staging, promotion possible | Ops (versioning modèles) |
| **Rollback** | S6 | Vidéo 90s (promo → rollback) | Fiabilité (récupération erreur) |
| **Monitoring** | S7 | Rapport HTML drift (Evidently) | Qualité (détection dérive) |
| **SLO + Runbook** | S8 | 2 fichiers (SLO.md + RUNBOOK_ROLLBACK.md) | Contrat (garanties client) |
| **Carte Leaflet** | S9-S10 | HTML carte interactive (raster + vecteur) | Visuel (client voit le résultat) |
| **geoIA PoC** | S11-S12 | Pipeline tiles → U-Net → vector + IoU | Innovation (détection auto) |
| **2e service ML** | S13 | Flood service (même recette MLOps) | Scalabilité (process réplicable) |
| **Portfolio complet** | S15 | 2 MODEL_CARD + 2 études de cas + vidéos | Go-to-market (prêt prospection) |
| **Offres + Prospection** | S16 | 3 offres packagées + 5 envois | Business (premiers RDV) |

---

## Checklist pre-prospection (S16)

**Avant de contacter des clients, tu devras avoir** :

### Technique (preuve de compétence)
- [ ] 2 services ML en prod (UHI + flood/autre)
- [ ] Tests automatisés (pytest + CI/CD)
- [ ] MLflow Tracking + Registry + Monitoring
- [ ] Rollback opérationnel (vidéo démo)
- [ ] 2 cartes GIS (raster + vecteur)
- [ ] 1 PoC geoIA (segmentation + métriques)

### Business (preuve de sérieux)
- [ ] README professionnel (structure claire, screenshots)
- [ ] 2 MODEL_CARD.md (documentation modèles)
- [ ] 2 études de cas (problème → solution → impact)
- [ ] 2 vidéos démo (promo/rollback 90s + carte interactive)
- [ ] SLO.md + RUNBOOK_ROLLBACK.md (contrat opérationnel)

### Commercial (offres packagées)
- [ ] MLOps Starter (5 jours, 3-4,5k€)
- [ ] Carte citoyenne (10 jours, 5-7k€)
- [ ] geoIA PoC (15-21 jours, 9-12k€)
- [ ] Rétention mensuelle (1,2-1,8k€/mois)

---

## État actuel vs cible S16

| Catégorie | État actuel (S2) | Cible S16 | Progression |
|-----------|------------------|-----------|-------------|
| **Services ML** | 1 (UHI) | 2 | 50% |
| **Tests** | 0 | 5+ | 0% |
| **MLflow runs** | 0 | 10+ | 0% |
| **Cartes GIS** | 0 | 2+ | 0% |
| **PoC geoIA** | 0 | 1 | 0% |
| **Offres** | 0 | 3 | 0% |
| **Prospects** | 0 | 5+ | 0% |
| **Repo GitHub** | ✅ 1 | 1 | 100% |
| **Documentation** | README + screenshots | +MODEL_CARD +études cas | 30% |

**Prochaine grande étape** : S4 (porte GO/NO-GO #1) → doit avoir API + tests + 1 run MLflow + README clair.

---

## Auto-évaluation S2

**Questions à se poser** :

1. **Puis-je cloner mon repo sur une autre machine et faire `make check-env && make train && make serve` sans erreur ?**
   → Si oui : ton repo est reproductible ✅

2. **Puis-je montrer mon repo GitHub à un recruteur/client sans honte ?**
   → Si oui : ton portfolio est présentable ✅

3. **Puis-je expliquer en 30 secondes ce que j'ai livré en S1-S2 (sans jargon) ?**
   → Si oui : tu peux pitcher ✅

Si 3 × oui → **S2 solidement acquise, prêt pour S3** 🎉

---

**Fin du portfolio S2**  
Prochain update : après validation S3