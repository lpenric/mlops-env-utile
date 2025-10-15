# Quiz S1 — Mini-labo "Hello MLOps"

**Durée estimée** : 15 minutes  
**Seuil de réussite** : 7/10

---

## Partie A — Faire (6 questions QCM)

### Question 1
Tu veux changer le port de l'API de 8000 à 8080. Quelle commande ?

- A) `make serve PORT=8080`
- B) `make serve --port 8080`
- C) Modifier `Makefile` puis relancer `make serve`
- D) `python -m uvicorn services.uhi_service.app.main:app --port 8080`

<details>
<summary>Voir la réponse</summary>

**Réponse : A**

**Explication** : Le Makefile définit `PORT ?= 8000`, ce qui signifie que la variable `PORT` peut être surchargée en ligne de commande. La syntaxe correcte est `make serve PORT=8080`.

**Pourquoi pas D ?** La commande D fonctionne techniquement, mais contourne le Makefile (pas de variable `SERVICE`, pas de message "Démarrage..."). Toujours utiliser les commandes `make` pour la cohérence.
</details>

---

### Question 2
L'API retourne une erreur 500. Quelle est la **première** action de debugging ?

- A) Relancer `make train`
- B) Vérifier les logs du terminal où tourne `make serve`
- C) Supprimer le fichier `.pkl` et recréer
- D) Redémarrer le Mac

<details>
<summary>Voir la réponse</summary>

**Réponse : B**

**Explication** : Les logs Uvicorn (terminal `make serve`) affichent le traceback complet de l'erreur Python. C'est **toujours** le premier réflexe : lire l'erreur complète avant de modifier quoi que ce soit.

**Erreurs fréquentes S1** :
- Modèle introuvable (`MODEL_PATH` incorrect)
- JSON mal formaté (virgule manquante, guillemets simples)
- Feature names mismatch (warning, pas erreur 500)
</details>

---

### Question 3
Tu veux entraîner un 2e modèle avec `n_estimators=100` au lieu de 50. Où modifier ?

- A) Makefile, ligne `train:`
- B) `services/uhi_service/src/train.py`, ligne `RandomForestRegressor(...)`
- C) `environment.yml`, section `dependencies`
- D) `services/uhi_service/app/main.py`

<details>
<summary>Voir la réponse</summary>

**Réponse : B**

**Explication** : Les hyperparamètres du modèle sont définis dans `train.py` lors de l'instanciation de `RandomForestRegressor(n_estimators=50, ...)`. Modifier cette ligne, puis relancer `make train`.

**Bonne pratique** : En S4 (MLflow), les hyperparamètres seront loggués automatiquement pour traçabilité.
</details>

---

### Question 4
Tu veux tester l'API **sans terminal** (pas de curl). Comment ?

- A) Ouvrir `http://localhost:8000`
- B) Ouvrir `http://localhost:8000/docs`
- C) Utiliser Postman
- D) B et C sont corrects

<details>
<summary>Voir la réponse</summary>

**Réponse : D**

**Explication** :
- **B (Swagger UI)** : Documentation interactive auto-générée par FastAPI. Tu peux tester `/predict` directement dans le navigateur, voir le schéma JSON, exécuter des requêtes.
- **C (Postman)** : Client API graphique, utile pour tester des workflows complexes.
- **A** : Retourne juste `{"message": "UHI Prediction API", "status": "running"}` (endpoint root).

**Recommandation S1** : utiliser `/docs` (plus rapide que Postman pour débuter).
</details>

---

### Question 5
Après `make train`, où est sauvegardé le modèle ?

- A) `./models/uhi_model_v1.pkl`
- B) `services/uhi_service/models/uhi_model_v1.pkl`
- C) `mlruns/0/artifacts/model.pkl`
- D) Dans la mémoire RAM (pas sauvegardé)

<details>
<summary>Voir la réponse</summary>

**Réponse : B**

**Explication** : Le script `train.py` crée le dossier `services/uhi_service/models/` et y sauvegarde `uhi_model_v1.pkl` via `joblib.dump()`.

**Pourquoi pas C ?** MLflow n'est pas encore activé en S1 (sera ajouté en S4). Le dossier `mlruns/` n'existe pas encore.

**Important** : `.gitignore` exclut `*.pkl` pour éviter de versionner des fichiers lourds.
</details>

---

### Question 6
La commande `make smoke` échoue avec `curl: (7) Failed to connect`. Pourquoi ?

- A) Le modèle n'est pas entraîné
- B) L'API n'est pas démarrée (`make serve` pas lancé)
- C) Le port 8000 est déjà utilisé
- D) B ou C

<details>
<summary>Voir la réponse</summary>

**Réponse : D**

**Explication** :
- **B** : Si `make serve` ne tourne pas, rien n'écoute sur le port 8000 → `curl` ne peut pas se connecter.
- **C** : Si un autre processus utilise déjà le port 8000, `uvicorn` échoue au démarrage (erreur visible dans les logs).

**Solution B** : Lancer `make serve` dans un terminal séparé.  
**Solution C** : Utiliser un autre port (`make serve PORT=8001`) ou tuer le processus (`lsof -ti:8000 | xargs kill`).
</details>

---

## Partie B — Comprendre (4 questions ouvertes)

### Question 7
Pourquoi utilise-t-on des **données synthétiques** en S1 au lieu de vraies données satellites/cadastre ?

<details>
<summary>Voir la réponse</summary>

**Réponse attendue** (3 points clés) :

1. **Démarrage rapide** : Pas besoin de télécharger/nettoyer des données réelles (gain de temps pour valider le workflow).
2. **Distribution contrôlée** : On connaît les relations (ndvi ↓ + densité ↑ = chaleur ↑), ce qui permet de **vérifier que le modèle apprend** correctement.
3. **Indépendance** : Le focus S1 est sur l'**infra MLOps** (API, Makefile, tests), pas sur la qualité des données. Les vraies données viendront en S9-S12 (GIS).

**Anti-pattern** : Commencer par chercher des datasets parfaits → blocage de plusieurs jours → abandon. **Shipping > perfection en S1.**
</details>

---

### Question 8
Le modèle prédit `uhi_score: 78.06` pour `building_density=0.7`. Est-ce cohérent ? Justifie.

<details>
<summary>Voir la réponse</summary>

**Réponse : Oui, cohérent**

**Justification** :
- Score UHI = 0-100 (0 = pas de chaleur, 100 = îlot maximal)
- Entrées : `ndvi=0.5` (végétation moyenne), `building_density=0.7` (forte densité bâtie), `water_distance=1000m` (éloigné de l'eau)
- **Logique physique** : Beaucoup de béton + peu de végétation + loin de l'eau = forte chaleur urbaine
- **Score ~78/100** : zone à risque élevé, cohérent avec les paramètres

**Si le modèle avait prédit 12/100** → incohérent, signalerait un bug (mauvais sens des features, erreur de signes).
</details>

---

### Question 9
Explique la différence entre `conda activate mlops` et `source ~/miniforge3/bin/activate mlops`.

<details>
<summary>Voir la réponse</summary>

**Réponse attendue** :

**`conda activate mlops`** (recommandé) :
- Commande moderne, intégrée à conda 4.6+
- Fonctionne sur bash, zsh, fish
- Gère automatiquement les variables d'environnement, PATH, PS1 (prompt)

**`source ~/miniforge3/bin/activate mlops`** (ancienne méthode) :
- Fonctionne mais obsolète
- Peut causer des conflits de PATH si plusieurs conda installés
- Moins robuste sur zsh/fish

**Sur Mac M1 avec Miniforge** : toujours utiliser `conda activate` (initialisé par défaut dans `.zshrc` lors de l'installation).
</details>

---

### Question 10
Décris le flux complet de `make smoke` : qu'est-ce qui se passe étape par étape ?

<details>
<summary>Voir la réponse</summary>

**Réponse attendue** (étapes numérotées) :

1. **Make lit le Makefile** : trouve la règle `smoke:`
2. **Exécute la commande curl** : envoie une requête HTTP POST à `http://127.0.0.1:8000/predict`
3. **Headers** : `Content-Type: application/json` (indique que le body est du JSON)
4. **Body** : `{"ndvi": 0.5, "building_density": 0.7, "water_distance": 1000}` (données d'entrée)
5. **FastAPI reçoit la requête** : route `/predict` interceptée
6. **Validation Pydantic** : vérifie que le JSON respecte le schéma `UHIInput` (3 floats)
7. **Chargement modèle** : `model.predict()` appelé avec les 3 features
8. **RandomForest prédit** : retourne un score (ex: 78.06)
9. **FastAPI retourne** : JSON `{"uhi_score": 78.06}`, code HTTP 200
10. **curl affiche** : la réponse est pipée vers `python -m json.tool` (formatage lisible)

**Si une étape échoue** : erreur 4xx/5xx avec message explicite dans les logs Uvicorn.
</details>

---

## Barème & Interprétation

| Score | Niveau | Action |
|-------|--------|--------|
| 9-10 | ⭐⭐⭐ Excellent | Prêt pour S2 |
| 7-8 | ⭐⭐ Bien | Réviser les questions ratées, puis S2 |
| 5-6 | ⭐ Fragile | Refaire le TP S1 (make train/serve/smoke) avant S2 |
| 0-4 | ⚠️ Lacunes | Revoir les concepts de base (API REST, conda, Makefile) |

---

## Auto-évaluation

**Questions à se poser après le quiz** :
- Ai-je **exécuté moi-même** toutes les commandes (train/serve/smoke) ?
- Puis-je **expliquer à un débutant** ce que fait chaque ligne du Makefile ?
- Si l'API crashe, sais-je où **chercher les logs** ?

Si 3 × oui → **S1 solidement acquise** 🎉