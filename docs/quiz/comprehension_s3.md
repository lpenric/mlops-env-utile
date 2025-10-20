# Test Compréhension Opérationnelle S3

**Durée** : 10 minutes  
**Format** : Réponses courtes (3-5 phrases), langage naturel (pas de code)

---

## Question 1 — Flux de bout en bout

**Décris en 4-5 étapes ce qui se passe entre `pytest -q tests/test_smoke.py` et `3 passed in 0.11s`.**

<details>
<summary>Voir la réponse</summary>

**Réponse attendue** :
1. **Découverte** : pytest analyse `test_smoke.py`, trouve les fonctions `test_*` (3 fonctions)
2. **Setup** : pytest injecte les fixtures (ex: `api_url`) automatiquement
3. **Exécution** : Chaque test fait des appels HTTP à l'API, vérifie les `assert`
4. **Validation** : Si tous les asserts OK → `passed`, sinon affiche erreur détaillée
5. **Rapport** : Affiche `3 passed in 0.11s`

**Validation** : Mention découverte auto, fixtures, assertions, vraies requêtes HTTP.
</details>

---

## Question 2 — Modification simple

**Un client veut l'API sur port 8080 au lieu de 8000. Que fais-tu ?**

<details>
<summary>Voir la réponse</summary>

**Action** : `make serve SERVICE=uhi_service PORT=8080`

**Explication** : Le Makefile a une variable `PORT ?= 8000`. Passer `PORT=8080` en ligne de commande surcharge la valeur par défaut. Uvicorn utilise `--port $(PORT)` donc démarre sur 8080.

**Pourquoi c'est mieux** : Pas besoin de modifier le code, configuration externe, permet plusieurs instances (dev:8000, staging:8080).
</details>

---

## Question 3 — Debugging

**L'API retourne 500 sur `/predict`. Ton processus de debugging en 3 étapes ?**

<details>
<summary>Voir la réponse</summary>

**Étape 1** : Lire les logs terminal `make serve` → traceback indique ligne + type d'erreur

**Étape 2** : Identifier cause dans traceback :
- `FileNotFoundError: uhi_model_v1.pkl` → `make train`
- `KeyError: 'ndvi'` → JSON incomplet
- `ValueError: string to float` → types incorrects

**Étape 3** : Tester correction avec `make smoke` ou `pytest -q`

**Validation** : Méthodologie structurée, pas "j'essaie au hasard".
</details>

---

## Question 4 — Dépendances

**Pourquoi les tests pytest avant commit ? Conséquence si absent ?**

<details>
<summary>Voir la réponse</summary>

**Raison** : Vérifient automatiquement que l'API fonctionne après chaque modif. Sans tests, commit possible avec code cassé.

**Conséquence** :
- Dev : Bug découvert tard (perte temps)
- Prod : Code cassé déployé → API retourne 500 → perte confiance client

**Lien workflow** : Prépare CI/CD (GitHub Actions lance pytest auto, bloque merge si échec).

**Valeur client** : "90% bugs détectés avant prod, réduction risque pannes."
</details>

---

## Question 5 — Pitch client

**Client : "Qu'as-tu livré en S3 ?" Réponds en 2-3 phrases (valeur métier).**

<details>
<summary>Voir la réponse</summary>

**Exemple** : "J'ai mis en place des tests automatiques qui vérifient que votre API refuse les données aberrantes (NDVI négatif, etc.) et retourne toujours des prédictions cohérentes. Ça élimine 90% des bugs avant production et garantit que vos agents terrain reçoivent des alertes fiables. Plus besoin de tester manuellement : ça divise par 5 le temps de validation."

**Validation** : Pas de jargon (pytest, Pydantic), focus conséquence (fiabilité, gain temps), lien métier (agents terrain, îlots chaleur).
</details>

---

## Barème

| Score | Niveau | Action |
|-------|--------|--------|
| 5/5 ✅ | Compréhension solide | Prêt S4 |
| 3-4 ⚠️ | Partielle | Refaire TP S3 |
| 0-2 ❌ | Cargo cult | Consolider S3 |

**Critère** : Explication en langage naturel, pas récitation de code.