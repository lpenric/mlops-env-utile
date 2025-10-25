# Quiz S4 — MLflow Tracking

**Durée estimée** : 15 minutes  
**Seuil de réussite** : 7/10

## Partie A — Faire (6 questions QCM)

### Question 1
Tu viens de lancer `make train SERVICE=uhi_service`. Dans quel dossier MLflow stocke-t-il les informations du run (params, metrics, artefacts) ?

- A) `services/uhi_service/models/`
- B) `./mlruns/0/[run_id]/`
- C) `/tmp/mlflow/`
- D) `~/.mlflow/experiments/`

<details>
<summary>Voir la réponse</summary>

**Réponse : B**

**Explication** : MLflow utilise `./mlruns/` à la racine du projet par défaut. L'experiment ID 0 (Default) crée un sous-dossier `0/`, et chaque run a son propre sous-dossier identifié par un UUID (ex: `da7ff42a...`).

**Anti-pattern** : Chercher les runs dans `services/` ou confondre avec le modèle .pkl sauvegardé manuellement (qui va dans `services/uhi_service/models/`).
</details>

---

### Question 2
L'interface MLflow UI sur `http://localhost:5000` affiche une page blanche. Quelle est la cause la plus probable sur Mac ?

- A) MLflow n'est pas installé
- B) Le port 5000 est occupé par un autre process
- C) Problème de résolution DNS avec `localhost`
- D) Firewall bloque le port

<details>
<summary>Voir la réponse</summary>

**Réponse : C**

**Explication** : Sur Mac, `localhost` peut avoir des problèmes de résolution DNS. L'API MLflow répond correctement (testable avec `curl`), mais le frontend ne charge pas. Solution : utiliser `http://127.0.0.1:5000` (IP loopback directe).

**Erreur fréquente** : Relancer MLflow ou changer de port alors que le serveur fonctionne. Toujours tester l'API avec `curl` avant.

**Commande diagnostic** : `curl "http://127.0.0.1:5000/api/2.0/mlflow/experiments/get?experiment_id=0"` (guillemets obligatoires à cause du `?` en zsh).
</details>

---

### Question 3
Tu veux réinitialiser complètement MLflow pour repartir de zéro. Quelle est la méthode correcte ?

- A) `rm -rf mlruns/*`
- B) `rm -rf mlruns` puis `make train`
- C) `mlflow experiments delete --experiment-id 0`
- D) `rm -rf mlruns` puis `mkdir mlruns`

<details>
<summary>Voir la réponse</summary>

**Réponse : B**

**Explication** : `rm -rf mlruns` supprime tout. Au prochain `make train`, MLflow recrée automatiquement la structure (`mlruns/0/meta.yaml`, etc.). C'est la méthode la plus propre.

**Anti-pattern A** : `rm -rf mlruns/*` laisse un dossier `mlruns/` vide. MLflow refuse de réinitialiser (sécurité) et génère l'erreur "Could not find experiment with ID 0".

**Anti-pattern D** : Créer `mlruns/` manuellement avant le premier run bloque aussi la réinitialisation auto.

**Règle** : Si `mlruns/` n'existe pas → MLflow le crée. Si `mlruns/` existe → MLflow suppose qu'il contient des données importantes.
</details>

---

### Question 4
Dans ton code `train.py`, tu as ajouté `mlflow.log_param("max_depth", 10)`. Où retrouves-tu cette valeur dans MLflow UI ?

- A) Onglet "Metrics"
- B) Onglet "Parameters" (ou colonne `max_depth` dans la liste des runs)
- C) Onglet "Artifacts"
- D) Onglet "Tags"

<details>
<summary>Voir la réponse</summary>

**Réponse : B**

**Explication** : `log_param()` enregistre un hyperparamètre (valeur fixée avant l'entraînement). MLflow l'affiche dans la section "Parameters" de chaque run, et permet de créer une colonne `max_depth` dans le tableau de comparaison.

**Différence clé** :
- `log_param()` → hyperparams (max_depth, n_estimators)
- `log_metric()` → métriques de performance (mae, r2_score)
- `log_model()` → artefact modèle (fichier pkl)

**Astuce UI** : Cliquer sur "Columns" pour afficher/masquer les colonnes params et metrics.
</details>

---

### Question 5
Tu obtiens l'erreur `MlflowException: Could not find experiment with ID 0` au lancement de `make train`. Quelle est la solution immédiate ?

- A) Réinstaller MLflow : `conda install mlflow`
- B) Créer l'experiment : `mlflow experiments create --experiment-name "Default"`
- C) Supprimer et recréer : `rm -rf mlruns` puis `make train`
- D) Changer l'experiment ID dans le code

<details>
<summary>Voir la réponse</summary>

**Réponse : C**

**Explication** : Cette erreur survient quand `mlruns/` existe mais que `mlruns/0/meta.yaml` est absent (structure corrompue). La solution la plus simple : supprimer complètement `mlruns/` et laisser MLflow le recréer proprement.

**Option B fonctionne aussi** mais nécessite la bonne syntaxe : `mlflow experiments create --experiment-name "Default" --artifact-location file://$(pwd)/mlruns/0`. Option C est plus rapide.

**Erreur fréquente** : Avoir fait `rm -rf mlruns/*` puis `mkdir mlruns` avant l'erreur. C'est justement ce qui casse la structure.
</details>

---

### Question 6
Tu compares 2 runs dans MLflow UI. Run 1 a `max_depth=10, mae=4.74`. Run 2 a `max_depth=15, mae=4.75`. Que peux-tu en conclure ?

- A) Le modèle avec max_depth=15 est meilleur (plus profond = mieux)
- B) Le modèle avec max_depth=10 est meilleur (MAE plus faible)
- C) Les 2 modèles sont équivalents (différence négligeable)
- D) Impossible de conclure sans voir R² et les données de test

<details>
<summary>Voir la réponse</summary>

**Réponse : C (ou D acceptable)**

**Explication** : Différence de MAE de 0.01 sur un score ~4.7 est **négligeable** (±0.2%). Sur des données synthétiques avec bruit aléatoire, c'est du bruit statistique. Les 2 modèles performent pareil.

**Réponse D acceptable** car en production, on regarde aussi :
- R² (variance expliquée)
- Performance sur données de test (pas juste train)
- Latence d'inférence (max_depth=10 peut être plus rapide)
- Coût de réentraînement

**Anti-pattern B** : Choisir systématiquement le MAE le plus bas sans contexte. En ML, une différence <1% est souvent du bruit.

**Lien S5** : Le Model Registry (semaine prochaine) aide à comparer et choisir la version à mettre en production.
</details>

---

## Partie B — Comprendre (4 questions ouvertes)

### Question 7
Explique en 3-4 phrases : pourquoi MLflow Tracking est utile dans un projet ML ? Que se passerait-il sans ?

<details>
<summary>Voir la réponse</summary>

**Réponse attendue** (3 points clés) :

1. **Traçabilité** : MLflow enregistre automatiquement tous les runs (params, métriques, artefacts). Sans lui, tu devrais noter manuellement "quel modèle j'ai entraîné avec quels hyperparams", ce qui est source d'erreurs.

2. **Comparaison** : L'interface permet de comparer visuellement plusieurs runs (ex: max_depth=10 vs 15). Sans outil, tu dois relire des logs texte éparpillés ou refaire les entraînements.

3. **Reproductibilité** : Chaque run sauvegarde le modèle + metadata. Si un modèle performe bien en prod, tu peux retrouver exactement comment il a été entraîné. Sans MLflow, risque de "on sait plus quel modèle on a déployé".

**Lien avec valeur client** : En cas de régression en production (modèle v2 moins bon que v1), MLflow permet un rollback immédiat vers v1. Sans tracking, c'est la panique ("c'était quoi les bons hyperparams déjà ?").

**Anticipation S5** : Le Model Registry (semaine prochaine) ajoute une couche au-dessus : versions nommées (v1, v2) avec états (Staging, Production) pour gérer le cycle de vie des modèles.
</details>

---

### Question 8
Tu as lancé `make train` 4 fois aujourd'hui. MLflow affiche 4 runs dans l'UI. Un client te demande "pourquoi garder tous ces runs, ça prend de la place ?". Comment réponds-tu ?

<details>
<summary>Voir la réponse</summary>

**Réponse attendue** (3 points clés) :

1. **Historique d'expérimentation** : Les 4 runs montrent ton processus d'optimisation (ex: tester différents hyperparams). C'est la preuve que tu as itéré et comparé scientifiquement, pas choisi au hasard.

2. **Audit & conformité** : En environnement pro (banque, santé, énergie), tu dois pouvoir justifier "pourquoi ce modèle en production ?". MLflow fournit la trace complète : qui, quand, avec quels params, quelle performance.

3. **Coût négligeable** : Un run MLflow = quelques Ko de metadata + 1 fichier .pkl (~1-5 Mo). 100 runs = ~500 Mo max. C'est bien moins cher que de refaire un entraînement perdu.

**Pitch client** : "C'est comme un journal de bord automatique. Si votre modèle régresse en production, je peux retrouver instantanément le bon modèle et ses paramètres, au lieu de passer 2 jours à réexpérimenter. Ça réduit votre risque opérationnel de 80%."

**Note** : En pratique, on peut nettoyer les runs de test (durée <1s, pas de metrics) après validation. Mais garder tous les runs complets est la bonne pratique.
</details>

---

### Question 9
Décris en 4 étapes le flux complet entre `make train` et voir le run dans MLflow UI. (Focus : que se passe-t-il sous le capot ?)

<details>
<summary>Voir la réponse</summary>

**Réponse attendue** (flux logique) :

1. **Lancement** : `make train` exécute `python services/uhi_service/src/train.py`. Python démarre, imports chargés (numpy, sklearn, mlflow).

2. **Enregistrement** : `with mlflow.start_run():` crée un nouveau run dans `./mlruns/0/[run_id]/`. MLflow génère un UUID unique, crée la structure de dossiers.

3. **Logging** : Pendant l'entraînement, `mlflow.log_param()` écrit dans `params/`, `mlflow.log_metric()` dans `metrics/`, `mlflow.sklearn.log_model()` sauvegarde le modèle dans `artifacts/model/`.

4. **UI** : `mlflow ui` lit le contenu de `./mlruns/0/` (tous les sous-dossiers run_id), parse les fichiers metadata, et affiche le tableau dans le navigateur. Chaque rechargement de page relit `mlruns/` (pas de cache base de données pour l'instant).

**Validation** : Mention de `./mlruns/[run_id]/`, distinction params/metrics/artifacts, et compréhension que l'UI lit directement le système de fichiers (pas de serveur séparé en mode local).

**Lien avec S5** : Le Model Registry ajoute une couche "registered models" avec versions nommées, mais utilise toujours `mlruns/` en backend.
</details>

---

### Question 10
Un collègue débutant te dit : "J'ai fait `rm -rf mlruns/*`, maintenant MLflow plante. Mais hier ça marchait !" Explique-lui en langage simple pourquoi et comment réparer.

<details>
<summary>Voir la réponse</summary>

**Réponse attendue** (explication pédagogique) :

1. **Pourquoi ça casse** : `rm -rf mlruns/*` supprime le contenu (les runs + le fichier `meta.yaml` de l'experiment 0) mais laisse le dossier `mlruns/` vide. MLflow voit que `mlruns/` existe et suppose qu'il contient une structure valide, mais ne trouve pas l'experiment 0 → erreur.

2. **Analogie** : C'est comme vider complètement un classeur mais laisser le meuble vide. Quand tu cherches le dossier "Default", tu trouves le meuble mais pas le dossier → confusion.

3. **Solution** : Supprime le dossier entier (`rm -rf mlruns`), pas juste le contenu. Au prochain `make train`, MLflow dira "ah, pas de classeur, je dois en créer un neuf" et reconstruit tout proprement.

**Règle simple** : Pour reset MLflow, toujours faire `rm -rf mlruns` (supprimer le dossier), jamais `rm -rf mlruns/*` (vider le contenu).

**Validation** : Si ton collègue peut expliquer à quelqu'un d'autre avec ses propres mots (sans réciter ta réponse), c'est gagné. Sinon, lui faire tester la manipulation pour comprendre viscéralement.
</details>

---

## Barème & Interprétation

| Score | Niveau | Action |
|-------|--------|--------|
| 9-10 | ⭐⭐⭐ Excellent | Prêt pour S5 (Model Registry) |
| 7-8 | ⭐⭐ Bien | Réviser questions ratées, puis S5 |
| 5-6 | ⭐ Fragile | Relancer 2 runs MLflow + explorer UI avant S5 |
| 0-4 | ⚠️ Lacunes | Refaire TP S4 (train + UI + reset), puis refaire quiz |

## Auto-évaluation

**Questions à se poser après le quiz** :
- Peux-tu expliquer oralement (sans notes) le flux `make train` → MLflow UI à un collègue ?
- Si MLflow plante demain, peux-tu diagnostiquer en <5 min (logs, curl, structure dossiers) ?
- Peux-tu pitcher la valeur de MLflow Tracking à un client en 2 phrases (focus bénéfice métier, pas technique) ?

Si 3 × oui → **S4 solidement acquise** 🎉  
Si 2/3 → Revoir les concepts flous (questions ouvertes ratées)  
Si ≤1 → Refaire le TP S4 avant de passer à S5