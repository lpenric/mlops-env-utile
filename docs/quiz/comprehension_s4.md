# Test Compréhension Opérationnelle S4

**Durée** : 10 minutes  
**Format** : Réponses courtes (3-5 phrases), en langage naturel (pas de code)

---

## Instructions

Réponds à ces 5 questions **sans regarder les fichiers ni la documentation**. Si tu bloques sur 2+ questions, consolide S4 avant de passer à S5.

---

### Question 1 — Flux de bout en bout

Décris en 4-5 étapes ce qui se passe entre le moment où tu tapes `make train` et le moment où tu vois le run dans MLflow UI.

**Réponse attendue** (éléments clés) :

1. **Lancement** : `make train` exécute `python services/uhi_service/src/train.py`. Le script Python démarre et charge les imports (numpy, sklearn, mlflow).

2. **Création du run** : `with mlflow.start_run():` génère un UUID unique (ex: `da7ff42a...`) et crée un dossier `./mlruns/0/da7ff42a.../` avec la structure (params/, metrics/, artifacts/).

3. **Entraînement & logging** : Le modèle RandomForest s'entraîne. Pendant ce temps, `mlflow.log_param()` écrit les fichiers dans `params/`, `mlflow.log_metric()` dans `metrics/`, et `mlflow.sklearn.log_model()` sauvegarde le modèle .pkl dans `artifacts/model/`.

4. **Fin du run** : Le script affiche "Run MLflow ID : da7ff42a..." et se termine. Tous les fichiers sont écrits dans `./mlruns/`.

5. **Affichage dans l'UI** : Quand tu lances `mlflow ui --port 5000` et ouvres `http://127.0.0.1:5000`, l'interface lit le contenu de `./mlruns/0/`, parse tous les sous-dossiers (run_id), et affiche le tableau avec les runs, params, metrics. Pas de base de données séparée : l'UI lit directement le système de fichiers.

**Validation** : Tu comprends que MLflow stocke tout dans `./mlruns/` (fichiers locaux), et que l'UI est juste une interface de lecture de ces fichiers.

---

### Question 2 — Modification simple

Un collègue te demande "je veux comparer 3 valeurs de max_depth (5, 10, 15) dans MLflow. Que dois-je faire ?"

**Réponse attendue** :

Modifier `services/uhi_service/src/train.py` ligne ~55 (variable `max_depth`), puis lancer `make train` 3 fois en changeant la valeur à chaque fois :
- 1er run : `max_depth = 5` → `make train`
- 2e run : `max_depth = 10` → `make train`
- 3e run : `max_depth = 15` → `make train`

Ensuite, ouvrir `mlflow ui --port 5000` et aller dans l'onglet Runs. Cliquer sur "Columns" et cocher `max_depth`, `mae`, `r2_score` pour voir les 3 valeurs côte à côte. Tu peux aussi sélectionner les 3 runs (checkbox) et cliquer "Compare" pour voir un graphique.

**Validation** : Pas besoin de modifier le code MLflow, juste changer la valeur de l'hyperparam et relancer l'entraînement. MLflow enregistre automatiquement chaque run séparément.

---

### Question 3 — Debugging

Tu lances `make train` et tu obtiens l'erreur `MlflowException: Could not find experiment with ID 0`. Décris ton processus de debugging en 3 étapes concrètes.

**Réponse attendue** :

1. **Lire l'erreur complète** : Le message dit "Could not find experiment with ID 0", ce qui signifie que MLflow cherche l'experiment Default (ID 0) mais ne le trouve pas dans `./mlruns/`.

2. **Vérifier la structure mlruns/** : Faire `ls -la mlruns/`. Si le dossier existe mais est vide (pas de sous-dossier `0/` ou pas de fichier `meta.yaml`), c'est que la structure a été corrompue (probablement après un `rm -rf mlruns/*` qui a vidé le contenu sans supprimer le dossier).

3. **Reset propre** : Supprimer complètement le dossier (`rm -rf mlruns`), puis relancer `make train`. MLflow va recréer automatiquement `mlruns/0/meta.yaml` et la structure complète. Le run devrait passer sans erreur.

**Validation** : Méthodologie structurée (lire erreur → vérifier structure fichiers → action correctrice), pas "je réessaie au hasard" ou "je réinstalle MLflow".

---

### Question 4 — Dépendances

Pourquoi MLflow Tracking est-il nécessaire dans un projet ML ? Que se passerait-il si tu n'utilisais pas MLflow ?

**Réponse attendue** :

**Raison technique** : MLflow enregistre automatiquement tous les runs d'entraînement (hyperparams, métriques, modèle) dans une structure organisée. Sans lui, tu devrais noter manuellement dans un fichier texte ou Excel "quel modèle avec quels params a donné quelle performance", ce qui est source d'erreurs et de perte d'information.

**Conséquence si absent** : En production, si un modèle régresse (par exemple, tu déploies un nouveau modèle qui performe moins bien), tu ne sais plus quel était le bon modèle ni comment le refaire. Tu dois réexpérimenter pendant des heures ou des jours pour retrouver les bons hyperparams. C'est un risque opérationnel majeur.

**Lien avec workflow global** : MLflow Tracking est la base du cycle de vie MLOps : d'abord tu traces les expérimentations (S4), puis tu versionnes les meilleurs modèles (S5 Registry), puis tu déploies et monitors (S6-S8). Sans tracking, impossible de faire du Registry ou du rollback.

**Validation** : Tu comprends que MLflow = mémoire du projet ML, pas juste un "nice to have". C'est une assurance contre la perte d'information et la régression en production.

---

### Question 5 — Pitch client

Un client te demande "Qu'as-tu livré cette semaine S4 ?". Réponds en 2-3 phrases, focus valeur métier (pas technique).

**Réponse attendue** :

"J'ai mis en place un système de traçabilité automatique pour votre modèle de prédiction des îlots de chaleur. Chaque entraînement est maintenant enregistré avec ses paramètres et performances, ce qui permet de comparer scientifiquement différentes versions et de retrouver instantanément le meilleur modèle. Concrètement, si le modèle en production régresse demain, je peux revenir à la version précédente en 2 minutes au lieu de 2 jours de réexpérimentation, ce qui réduit votre risque opérationnel de 80%."

**Ou version alternative** :

"J'ai ajouté un 'journal de bord' automatique qui enregistre tous les essais d'amélioration du modèle. Vous avez maintenant une interface web où vous pouvez voir visuellement quel modèle performe le mieux et pourquoi. Ça transforme l'expérimentation ML d'un processus opaque ('on sait plus ce qu'on a testé') en un processus auditable et reproductible."

**Validation** : 
- Pas de jargon (MLflow, run, artifact)
- Focus bénéfice client (réduction risque, gain de temps, audit)
- Exemple concret (rollback en 2 min vs 2 jours)
- Lien avec valeur métier (fiabilité, conformité, coût)

---

## Barème

| Score | Niveau | Action |
|-------|--------|--------|
| 5/5 ✅ | Compréhension opérationnelle solide | Prêt pour S5 (Model Registry) |
| 3-4 ⚠️ | Compréhension partielle | Refaire le TP S4, revoir concepts flous (Q1 flux, Q4 dépendances) |
| 0-2 ❌ | Cargo cult (rituels sans compréhension) | NE PAS passer à S5, consolider S4 |

**Critère de validation** : Tu peux expliquer **en langage naturel** (pas réciter du code ou des commandes). Si quelqu'un qui ne connaît pas MLflow peut comprendre ta réponse, c'est gagné.

---

## Anti-patterns à éviter

❌ **Réponse type cargo cult** :
- "Je fais ça parce que c'est dans le PLAN_MAITRE"
- "Je sais pas, mais ça marche"
- Récitation de commandes sans expliquer le pourquoi (ex: "je tape make train puis mlflow ui")

✅ **Réponse opérationnelle correcte** :
- Mention du flux de données (entrée → traitement → sortie)
- Lien cause-effet ("sans X, alors Y échoue parce que...")
- Langage naturel ("MLflow lit les fichiers dans ./mlruns/ pour afficher...")
- Conscience de la valeur métier ("ça réduit le risque de...", "ça permet au client de...")

**Si tu as répondu correctement à 4-5 questions, tu as acquis une compréhension opérationnelle solide de MLflow Tracking. Passe à S5 !**