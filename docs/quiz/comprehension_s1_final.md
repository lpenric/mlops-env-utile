# Test Compréhension Opérationnelle S1

**Durée** : 10 minutes  
**Format** : Réponses courtes (3-5 phrases), en langage naturel (pas de code)

---

## Instructions

Réponds à ces 5 questions **sans regarder les fichiers ni la documentation**. Si tu bloques sur 2+ questions, consolide S1 avant de passer à S2.

---

### Question 1 — Flux de bout en bout

Décris en 4-5 étapes ce qui se passe entre le moment où tu lances `make train` et le moment où tu reçois une réponse JSON de `/predict`.

**Réponse attendue** (éléments clés) :

1. **`make train`** exécute `train.py` qui génère des données synthétiques (NDVI, densité, distance eau)
2. **Entraînement** : RandomForest apprend la relation features → score UHI
3. **Sauvegarde** : Le modèle est sérialisé en `.pkl` dans `services/uhi_service/models/`
4. **`make serve`** démarre FastAPI qui **charge le .pkl en mémoire** au startup
5. **Requête `/predict`** : FastAPI valide le JSON (Pydantic), appelle `model.predict()`, retourne le score

**Validation** : Tu dois mentionner le fichier `.pkl`, le chargement en mémoire, et la prédiction. Si tu sautes une étape clé, revoir le workflow.

---

### Question 2 — Modification simple

Un client veut que l'API tourne sur le port 8080 au lieu de 8000. Que fais-tu et pourquoi ?

**Réponse attendue** :

**Action** : `make serve PORT=8080`

**Explication** : Le Makefile définit `PORT ?= 8000`, ce qui signifie que c'est une valeur par défaut qui peut être surchargée en ligne de commande. En passant `PORT=8080`, on surcharge la variable sans modifier le code.

**Validation** : Pas besoin de modifier le `Makefile` ni `main.py`, juste la commande. Si tu as dit "modifier main.py", c'est trop complexe pour ce besoin simple.

---

### Question 3 — Debugging

L'API retourne une erreur 500 sur `/predict`. Décris ton processus de debugging en 3 étapes concrètes.

**Réponse attendue** :

1. **Lire les logs** du terminal où tourne `make serve` : chercher le traceback Python (ligne d'erreur, type d'exception)
2. **Identifier la cause** : vérifier que le modèle `.pkl` est chargé (`model is not None`), que le JSON est bien formaté (3 clés : ndvi, building_density, water_distance), que les types sont corrects (floats)
3. **Corriger et tester** : si JSON mal formaté → corriger les guillemets/virgules ; si modèle absent → relancer `make train` ; puis retester avec `make smoke`

**Validation** : Méthodologie structurée (logs → diagnostic → correction), pas "je réessaie au hasard". Si tu as dit "redémarrer le Mac", c'est cargo cult.

---

### Question 4 — Dépendances

Pourquoi doit-on faire `make train` avant `make serve` ? Que se passerait-il sans ?

**Réponse attendue** :

**Raison** : `make train` crée le fichier `.pkl` (modèle sauvegardé) dans `services/uhi_service/models/`. `make serve` charge ce fichier au démarrage de l'API via `joblib.load(MODEL_PATH)`.

**Conséquence si absent** : L'API démarre mais `model = None`. Quand on appelle `/predict`, FastAPI retourne `{"error": "Model not loaded"}` car il ne peut pas faire de prédiction sans modèle.

**Lien workflow** : Le `.pkl` est le **pont** entre l'entraînement (offline) et le serving (online). Sans lui, l'API est une coquille vide.

**Validation** : Tu dois mentionner le fichier `.pkl` et le chargement. Si tu as dit "ça marche pas" sans expliquer pourquoi, revoir le concept de persistance.

---

### Question 5 — Pitch client

Un client te demande "Qu'as-tu livré cette semaine (S1) ?". Réponds en 2-3 phrases, focus valeur métier (pas jargon technique).

**Réponse attendue** :

"J'ai construit une API de prédiction des îlots de chaleur urbains. Elle analyse la végétation, la densité bâtie et la distance à l'eau pour identifier les zones à risque. L'API répond en moins de 50 millisecondes et inclut une documentation interactive pour faciliter les tests."

**Ou** :

"J'ai livré un service ML opérationnel qui prédit le risque de surchauffe urbaine. Tout est automatisé (entraînement, déploiement, tests) via des commandes simples. Les résultats sont exploitables immédiatement par vos équipes via une API REST standard."

**Validation** : Langage non-technique (pas "RandomForest", "joblib", "Pydantic"), focus bénéfice client (rapidité, simplicité, exploitable). Si tu as récité des termes techniques, revoir l'angle "valeur métier".

---

## Barème

| Score | Niveau | Action |
|-------|--------|--------|
| 5/5 ✅ | Compréhension opérationnelle solide | Prêt pour S2 |
| 3-4 ⚠️ | Compréhension partielle | Refaire le TP S1, revoir concepts flous |
| 0-2 ❌ | Cargo cult (rituels sans compréhension) | NE PAS passer à S2, consolider S1 |

**Critère de validation** : Tu peux expliquer **en langage naturel** (pas réciter du code ou des commandes).

---

## Anti-patterns à éviter

❌ **Réponse type cargo cult** :
- "Je fais ça parce que c'est dans le PLAN_MAITRE"
- "Je sais pas, mais ça marche"
- Récitation de commandes sans expliquer le pourquoi

✅ **Réponse opérationnelle correcte** :
- Mention du flux de données (entrée → traitement → sortie)
- Lien cause-effet ("sans X, alors Y échoue parce que...")
- Langage naturel ("L'API charge le fichier .pkl au démarrage pour...")