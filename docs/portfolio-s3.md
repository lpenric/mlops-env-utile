# Portfolio MLOps — Artefacts livrables

**Dernière mise à jour** : 19 octobre 2025  
**Semaines complétées** : 3/16

---

## Artefacts techniques

| # | Artefact | Semaine | Statut | Lien | Pitch client (1 phrase) |
|---|----------|---------|--------|------|--------------------------|
| 1 | API ML (UHI) | S1 | ✅ | docs/screenshots/s1_*.png | API prédiction îlots chaleur, <50ms, validation auto, doc Swagger |
| 2 | Repo GitHub | S2 | ✅ | github.com/lpenric/mlops-env-utile | Code versionné, README pro, clone en 2 min |
| 3 | Tests automatisés | S3 | ✅ | docs/screenshots/s3_*.png | 3 tests détectent régressions en 0.11s, Pydantic rejette données aberrantes |
| 4 | MLflow Tracking | S4 | ⏳ | - | (À venir) Historique entraînements, comparaison modèles |
| 5 | Model Registry | S5 | ⏳ | - | (À venir) Versions Staging/Production, promotion/rollback |
| 6 | Vidéo promo/rollback | S6 | ⏳ | - | (À venir) Démo 90s : promotion + rollback N-1 |
| 7 | Monitoring drift | S7 | ⏳ | - | (À venir) Rapport HTML dérive, alertes auto |
| 8 | SLO + Runbook | S8 | ⏳ | - | (À venir) Contrats service + procédure rollback |

---

## Compétences démontrées

### MLOps (S1-S8)
- [x] API REST (FastAPI) + validation Pydantic
- [x] Entraînement modèle (scikit-learn)
- [x] Persistence (joblib, .pkl)
- [x] **Tests automatisés (pytest) — S3**
- [x] **Validation input stricte (Pydantic Field) — S3**
- [ ] MLflow Tracking — S4
- [ ] Model Registry + promotion — S5
- [ ] Rollback opérationnel — S6
- [ ] Monitoring (Evidently) + data quality (GX) — S7
- [ ] SLO + Runbooks — S8

### Git & DevOps
- [x] Versioning Git (commit, push, branches)
- [x] Repo public GitHub + README pro
- [x] .gitignore configuré
- [x] **Git recovery (reflog, reset, amend, force push) — S3**
- [ ] CI/CD (GitHub Actions) — S4+

---

## Métriques clés

| Métrique | Actuel | Cible S16 |
|----------|--------|-----------|
| Services ML | 1 (UHI) | 2 |
| Tests auto | **3 (smoke)** | 5+ |
| Runs MLflow | 0 | 10+ |
| Cartes GIS | 0 | 2+ |
| PoC geoIA | 0 | 1 |
| Offres | 0 | 3 |
| Commits | **12+** | 50+ |

---

## Pitch 30 secondes (version S3)

"Je suis Enric, spécialisé MLOps environnement. J'ai livré une API de prédiction d'îlots de chaleur avec validation automatique des données et tests automatisés (détection régressions en 0.11s). Mon approche : anti-commodité, focus production rapide (5 jours), preuves visuelles (code GitHub public, screenshots). Prochaines étapes : MLflow pour traçabilité complète. Actuellement disponible pour missions MLOps courtes (API, monitoring, tests)."

**Évolution attendue** :
- **Post-S4** : Ajout "traçabilité MLflow (historique entraînements)"
- **Post-S8** : Ajout "rollback 1-click, SLO documentés"
- **Post-S12** : Ajout "cartes GIS interactives"
- **Post-S16** : Ajout "PoC geoIA, 3 offres packagées"

---

## Différenciation

**Ce qui distingue ce portfolio** :
1. **Repo public** : Code visible, preuve sociale immédiate
2. **Focus production** : Pas Kaggle, tout déployable
3. **Niche environnement** : Climat/prévention, pas e-commerce
4. **Preuves visuelles** : Screenshots, vidéos 90s, cartes
5. **Progression documentée** : PROGRESS.md montre parcours

**Phrase d'accroche** : "Mon portfolio est mon terrain de jeu en production : code ouvert, tests automatisés, déploiements documentés."

---

## Actions immédiates (post-S3)

- [ ] Importer cartes Anki S3
- [ ] Faire quiz S3 (7+/10)
- [ ] Faire test compréhension S3 (4+/5)
- [ ] Planifier session S4 (3 jours max)
- [ ] Optionnel : Section "Portfolio" LinkedIn avec lien GitHub

---

**Fin portfolio**  
Version 3.0 (post-S3)  
Prochain update : après S4