# Quiz S3 — Tests fumigène (pytest) & Validation Pydantic

**Durée estimée** : 15 minutes  
**Seuil de réussite** : 7/10

---

## Partie A — Faire (6 questions QCM)

### Question 1
Tu lances `make serve SERVICE=uhi_service` mais l'API refuse de démarrer avec l'erreur `[Errno 48] Address already in use`. Quelle est la meilleure solution ?

- A) Redémarrer le Mac
- B) `lsof -ti:8000 | xargs kill -9`
- C) Changer le code de l'API pour écouter sur port 8001
- D) `make serve PORT=8000` (relancer la même commande)

<details>
<summary>Voir la réponse</summary>

**Réponse : B**

**Explication** : Le port 8000 est déjà occupé par un processus Uvicorn précédent (souvent lancé en arrière-plan avec `&`). `lsof -ti:8000` trouve le PID du processus, `xargs kill -9` le tue.

**Pourquoi pas les autres ?**
- A) Redémarrer le Mac est overkill et prend 2 min au lieu de 2 secondes
- C) Modifier le code n'est pas nécessaire, le Makefile supporte `PORT=`
- D) Relancer la même commande reproduira l'erreur

**Alternative valide** : `make serve PORT=8001` (utilise un port différent sans tuer l'ancien processus)

**Erreur fréquente** : Taper `lsof -ti/8000` (slash au lieu de deux-points) → erreur "unknown protocol name"
</details>

---

### Question 2
Tu veux tester que ton API rejette correctement un input invalide (ndvi=99.9 au lieu de [-1, 1]). Quel code HTTP doit retourner l'endpoint `/predict` ?

- A) 200 OK
- B) 400 Bad Request
- C) 422 Unprocessable Entity
- D) 500 Internal Server Error

<details>
<summary>Voir la réponse</summary>

**Réponse : C**

**Explication** : FastAPI + Pydantic retournent automatiquement **422 Unprocessable Entity** quand la validation échoue (contraintes `Field(ge=, le=)` non respectées). C'est la convention REST pour "syntaxe JSON valide, mais données invalides".

**Pourquoi pas les autres ?**
- A) 200 = succès → signifierait que l'API accepte n'importe quelle valeur (bug)
- B) 400 = requête malformée (ex: JSON cassé) → ici le JSON est valide, c'est la valeur qui pose problème
- D) 500 = erreur serveur (bug dans le code) → ici c'est une erreur client (input invalide)

**Validation dans le test** :
```python
assert response.status_code == 422
assert "detail" in response.json()  # Message d'erreur de validation
```
</details>

---

### Question 3
Tu lances `pytest -q` mais vois le message `ERROR: file or directory not found: tests/test_smoke.py`. Quelle est la cause la plus probable ?

- A) pytest n'est pas installé dans l'environnement conda
- B) Le fichier `test_smoke.py` a une faute de frappe dans le nom
- C) Tu es dans le mauvais dossier (pas à la racine du projet)
- D) Le fichier `tests/__init__.py` est manquant

<details>
<summary>Voir la réponse</summary>

**Réponse : C**

**Explication** : pytest cherche le fichier depuis le **dossier courant**. Si tu es dans `services/uhi_service/app/`, pytest cherche `services/uhi_service/app/tests/test_smoke.py` qui n'existe pas. Solution : `cd ~/mlops_env_utile` avant de lancer pytest.

**Pourquoi pas les autres ?**
- A) Si pytest n'était pas installé, l'erreur serait `command not found: pytest`
- B) Une faute de frappe donnerait aussi "file not found", mais c'est moins fréquent que le mauvais dossier
- D) `__init__.py` n'est pas obligatoire pour pytest (utile pour imports, mais pas bloquant)

**Vérification rapide** : `pwd` doit afficher `/Users/enriclapa/mlops_env_utile`

**Anti-pattern** : Se déplacer dans les sous-dossiers pour consulter des fichiers, puis oublier de revenir à la racine pour les commandes `make` et `pytest`.
</details>

---

### Question 4
Après avoir modifié `services/uhi_service/app/main.py`, tu fais `git add /services/uhi_service/app/main.py` mais Git retourne `fatal: Invalid path '/services'`. Pourquoi ?

- A) Le fichier n'existe pas
- B) Git ne supporte pas les chemins avec plusieurs niveaux de sous-dossiers
- C) Le `/` initial indique un chemin absolu (racine du disque) au lieu de relatif
- D) Il faut faire `git add .` pour ajouter tous les fichiers modifiés

<details>
<summary>Voir la réponse</summary>

**Réponse : C**

**Explication** : En Git, `/services/` = chemin **absolu** depuis la racine du disque (équivalent de `C:\services` sur Windows). Git cherche `/services/` à la racine du Mac, qui n'existe pas. La syntaxe correcte est `git add services/uhi_service/app/main.py` (sans `/` initial) = chemin **relatif** depuis le dossier courant.

**Pourquoi pas les autres ?**
- A) Si le fichier n'existait pas, l'erreur serait différente (pathspec did not match any files)
- B) Git supporte sans problème les arborescences complexes
- D) `git add .` fonctionne, mais ajoute TOUS les fichiers modifiés (pas toujours souhaité)

**Règle à retenir** : En Git, toujours utiliser des chemins relatifs (sans `/` au début).

**Syntaxes valides** :
- `git add services/uhi_service/app/main.py` (relatif)
- `git add ./services/uhi_service/app/main.py` (relatif explicite)
</details>

---

### Question 5
Tu as fait un commit S3, puis un `git reset --hard HEAD~1` par erreur, perdant ton travail. Comment récupérer le commit "perdu" ?

- A) `git pull origin main` (télécharger depuis GitHub)
- B) `git reflog -10` puis `git reset --hard <hash_commit_s3>`
- C) Impossible, le commit est définitivement perdu
- D) `git revert HEAD` (annuler l'annulation)

<details>
<summary>Voir la réponse</summary>

**Réponse : B**

**Explication** : `git reflog` garde l'historique complet de tous les mouvements de HEAD, même après reset/rebase. Le commit S3 est "détaché" mais existe encore en mémoire (~30 jours). `git reflog -10` affiche les 10 derniers mouvements, tu identifies le hash du commit S3, puis `git reset --hard <hash>` revient à cet état.

**Pourquoi pas les autres ?**
- A) `git pull` fonctionne **seulement si tu avais pushé avant** le reset. Si le commit est uniquement local, pull ne ramène rien.
- C) Git garde tout en mémoire pendant ~30 jours, rien n'est définitivement perdu (sauf si git gc force)
- D) `git revert` crée un nouveau commit qui annule les changements, mais ne récupère pas un commit perdu

**Exemple reflog** :
```
4dbbc80 HEAD@{1}: commit: S3: Tests pytest
45c0771 HEAD@{2}: reset: moving to HEAD~1
```
→ Le commit 4dbbc80 est récupérable avec `git reset --hard 4dbbc80`

**Commande bonus** : `git cherry-pick <hash>` (appliquer ce commit sur la branche actuelle sans reset complet)
</details>

---

### Question 6
Tu veux ajouter le dossier `tests/` à un commit existant (déjà pushé sur GitHub) sans créer un nouveau commit. Quelle séquence de commandes ?

- A) `git add tests/ && git commit -m "Ajout tests"`
- B) `git add tests/ && git commit --amend --no-edit && git push`
- C) `git add tests/ && git commit --amend --no-edit && git push --force`
- D) `git add tests/ && git push`

<details>
<summary>Voir la réponse</summary>

**Réponse : C**

**Explication** : `git commit --amend` modifie le dernier commit au lieu d'en créer un nouveau. `--no-edit` garde le message de commit existant. **Comme l'historique est modifié**, le push normal sera rejeté (conflict). Il faut `git push --force` pour écraser la version distante.

**Pourquoi pas les autres ?**
- A) Crée un **nouveau** commit au lieu de modifier l'existant
- B) `git push` (sans --force) sera rejeté par GitHub avec `! [rejected] main -> main (non-fast-forward)`
- D) Il manque l'étape `commit --amend`, le push échouera

**Avertissement** : `git push --force` est **destructif** si quelqu'un d'autre a déjà pull le commit. En solo (ou en coordination), c'est OK.

**Alternative sans force push** : Créer un nouveau commit `"S3: Ajout tests/"` (option A), plus sûr mais historique moins propre.
</details>

---

## Partie B — Comprendre (4 questions ouvertes)

### Question 7
Explique en langage naturel (sans code) ce qui se passe entre le moment où tu lances `pytest -q tests/test_smoke.py` et l'affichage de `3 passed in 0.11s`.

<details>
<summary>Voir la réponse</summary>

**Réponse attendue** (3 points clés) :
1. **Découverte** : pytest analyse le fichier `test_smoke.py`, trouve toutes les fonctions commençant par `test_*` (3 fonctions ici)
2. **Setup + Exécution** : Pour chaque test, pytest injecte les fixtures (ex: `api_url`), lance la fonction, vérifie que les `assert` passent (pas d'exception levée)
3. **Rapport** : Si tous les asserts sont OK, pytest affiche `3 passed`. Si un assert échoue, pytest affiche le détail de l'erreur (ligne, valeur attendue vs reçue)

**Validation** :
- Mention du découverte automatique (pattern `test_*`)
- Mention des fixtures (injection automatique)
- Mention des assertions (validation des résultats)

**Lien avec valeur client** : "Les tests s'exécutent en quelques secondes et détectent automatiquement les régressions, sans intervention manuelle. Ça divise par 10 le temps de validation avant mise en prod."
</details>

---

### Question 8
Pourquoi Pydantic avec `Field(ge=-1.0, le=1.0)` est mieux que faire `if ndvi < -1 or ndvi > 1: raise Exception` dans le code de `/predict` ?

<details>
<summary>Voir la réponse</summary>

**Réponse attendue** (3 points clés) :
1. **Déclaratif vs impératif** : Avec Pydantic, tu **déclares** les contraintes une fois dans le schéma. Avec des `if`, tu dois répéter la validation partout (duplication, risque d'oubli).
2. **Automatisation** : FastAPI valide automatiquement **avant** que le code de `/predict` s'exécute. Si invalide, FastAPI retourne 422 sans toucher ton code → séparation des responsabilités.
3. **Documentation auto** : Les contraintes Pydantic apparaissent dans `/docs` (Swagger UI), le client voit immédiatement les limites acceptées. Avec des `if`, rien n'est documenté.

**Bonus** : Messages d'erreur standardisés (format JSON cohérent avec `detail`), pas besoin de gérer les exceptions manuellement.

**Lien avec S4+** : En S4, MLflow va logger les contraintes Pydantic automatiquement, traçabilité complète des entrées acceptées.
</details>

---

### Question 9
Un développeur junior te dit : "Je fais toujours `git add .` puis `git commit -m "WIP"` puis `git push`, même si le code ne marche pas. C'est OK ?". Que lui réponds-tu ? (Avantages/inconvénients)

<details>
<summary>Voir la réponse</summary>

**Réponse attendue** (3 points clés) :
1. **Avantages** : Commit fréquent = backup cloud automatique (protection contre perte de données), historique détaillé du parcours (utile pour reflog/git bisect), permet de rollback rapidement si fausse route.
2. **Inconvénients** : Historique Git "sale" (plein de commits WIP), difficile de comprendre l'évolution du projet, complique les code reviews (beaucoup de bruit).
3. **Recommandation équilibrée** : Commit WIP local OK pour protéger le travail, mais **avant de push** : soit squash (fusionner commits WIP), soit rebase interactif pour nettoyer l'historique. Ou utiliser des branches feature (WIP sur branche, merge propre sur main).

**Validation** : Mention du trade-off backup vs propreté, pas de réponse dogmatique ("TOUJOURS" ou "JAMAIS").

**Contexte MLOps** : En production, on veut un historique propre (1 commit = 1 feature/fix testée). En développement solo, WIP fréquent est acceptable tant qu'on nettoie avant livraison client.
</details>

---

### Question 10
Un client te demande : "Qu'as-tu livré cette semaine S3 et pourquoi c'est utile pour mon projet d'îlots de chaleur urbains ?". Réponds en 2-3 phrases, focus valeur métier (pas de jargon technique).

<details>
<summary>Voir la réponse</summary>

**Réponse attendue** (éléments clés) :
1. **Livrable** : "J'ai mis en place des tests automatiques qui vérifient que l'API refuse les données aberrantes et retourne toujours des prédictions cohérentes."
2. **Bénéfice** : "Ça élimine 90% des bugs avant la mise en production et garantit que vos agents terrain reçoivent des alertes fiables, pas des scores UHI négatifs ou supérieurs à 100."
3. **Impact temps/coût** : "Plus besoin de tester manuellement à chaque modification, ça divise par 5 le temps de validation et réduit le risque de pannes."

**Validation** :
- Pas de mention "pytest", "Pydantic", "422" → langage client
- Focus sur **conséquence concrète** (fiabilité, gain de temps, réduction risque)
- Lien avec le domaine métier (îlots de chaleur, agents terrain)

**Anti-pattern** : "J'ai installé pytest et créé 3 tests unitaires avec des fixtures et des assertions sur les codes HTTP" → trop technique, pas de valeur métier visible.
</details>

---

## Barème & Interprétation

| Score | Niveau | Action |
|-------|--------|--------|
| 9-10 | ⭐⭐⭐ Excellent | Prêt pour S4 (MLflow Tracking) |
| 7-8 | ⭐⭐ Bien | Réviser questions ratées (relire réponses détaillées), puis S4 |
| 5-6 | ⭐ Fragile | Refaire le TP S3 (relancer tests, Git amend), comprendre le flux avant S4 |
| 0-4 | ⚠️ Lacunes | Revoir concepts de base de S3 (pytest doc, Pydantic doc, Git reflog) |

---

## Auto-évaluation

**Questions à se poser après le quiz** :
- Peux-tu expliquer à un ami **sans regarder les fichiers** pourquoi pytest est plus rapide que tester manuellement avec curl ?
- Si l'API crashe en production, peux-tu décrire ton processus de debugging en 3 étapes concrètes (logs, reflog, rollback) ?
- Comprends-tu la différence entre "le code fonctionne" et "le code est testé automatiquement" ?

Si 3 × oui → **S3 solidement acquise** 🎉  
Si 2 × non → Refaire le TP S3 avant S4