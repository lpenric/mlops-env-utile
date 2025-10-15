# Quiz S2 — Git/GitHub & README propre

**Durée estimée** : 15 minutes  
**Seuil de réussite** : 7/10

---

## Partie A — Faire (6 questions QCM)

### Question 1
Tu viens de créer un fichier `test.py` dans ton repo. Quelle séquence de commandes permet de le versionner et de le pousser sur GitHub ?

- A) `git add test.py` → `git push` → `git commit -m "ajout test"`
- B) `git commit -m "ajout test"` → `git add test.py` → `git push`
- C) `git add test.py` → `git commit -m "ajout test"` → `git push`
- D) `git push` → `git add test.py` → `git commit -m "ajout test"`

<details>
<summary>Voir la réponse</summary>

**Réponse : C**

**Explication** :  
L'ordre correct est **stage → commit → push** :
1. `git add` = prépare le fichier (staging area)
2. `git commit` = crée le snapshot versionné localement
3. `git push` = envoie les commits vers GitHub

**Pourquoi pas les autres** :
- A : On ne peut pas `push` avant `commit`
- B : On ne peut pas `commit` avant `add` (fichier non stagé)
- D : On ne peut pas `push` avant d'avoir créé un commit

**Anti-pattern** : Faire `git add .` puis oublier le commit → rien n'est versionné, juste préparé.

</details>

---

### Question 2
Ton `.gitignore` contient `*.pkl`. Tu fais `git add .` puis `git status`. Que va afficher Git ?

- A) Tous les fichiers, y compris `uhi_model_v1.pkl`
- B) Tous les fichiers SAUF `uhi_model_v1.pkl`
- C) Erreur "fichier ignoré"
- D) Rien (working tree clean)

<details>
<summary>Voir la réponse</summary>

**Réponse : B**

**Explication** :  
`.gitignore` filtre automatiquement les fichiers lors du `git add`. Les patterns (ex: `*.pkl`) sont exclus **silencieusement** (pas d'erreur, ils sont juste ignorés).

**Pourquoi pas les autres** :
- A : Faux, `.gitignore` fait son travail
- C : Git n'affiche pas d'erreur pour les fichiers ignorés
- D : `git status` montrera les autres fichiers modifiés (non `.pkl`)

**Erreur fréquente** : Créer `.gitignore` APRÈS avoir déjà fait `git add` → les `.pkl` sont déjà trackés. Solution : `git rm --cached *.pkl`.

</details>

---

### Question 3
Tu veux vérifier si des fichiers `.pkl` ont été versionnés par erreur. Quelle commande utilises-tu ?

- A) `ls *.pkl`
- B) `git status | grep pkl`
- C) `git ls-files | grep pkl`
- D) `find . -name "*.pkl"`

<details>
<summary>Voir la réponse</summary>

**Réponse : C**

**Explication** :  
`git ls-files` liste **tous les fichiers versionnés** (trackés par Git). Si `grep pkl` retourne une ligne → problème.

**Pourquoi pas les autres** :
- A : Montre les `.pkl` présents localement, pas forcément versionnés
- B : `git status` montre les fichiers **modifiés**, pas tous les fichiers trackés
- D : `find` liste les fichiers système, pas le statut Git

**Commande alternative** : `git ls-tree -r main --name-only | grep pkl` (liste depuis le dernier commit).

</details>

---

### Question 4
GitHub te demande un mot de passe lors du `git push`, mais refuse ton mot de passe GitHub. Que se passe-t-il ?

- A) Ton compte GitHub est désactivé
- B) Le repo n'existe pas sur GitHub
- C) GitHub a désactivé l'authentification par mot de passe en 2021
- D) Tu as tapé le mauvais mot de passe

<details>
<summary>Voir la réponse</summary>

**Réponse : C**

**Explication** :  
Depuis août 2021, GitHub refuse les mots de passe pour les opérations Git. Tu dois utiliser :
- **Personal Access Token** (PAT) : https://github.com/settings/tokens
- **SSH** : clé publique/privée (`ssh-keygen`)

**Pourquoi pas les autres** :
- A/D : Ton compte fonctionne (tu peux te connecter sur github.com)
- B : L'erreur serait différente ("repository not found")

**Solution immédiate** :  
Générer un PAT (coche `repo`) → utiliser le token comme mot de passe lors du push.

</details>

---

### Question 5
Tu as fait `git commit -m "fix bug"` mais tu réalises que tu as oublié d'ajouter un fichier. Quelle commande permet de **modifier le dernier commit** (avant push) ?

- A) `git commit --amend`
- B) `git reset HEAD~1`
- C) `git revert HEAD`
- D) `git add . && git commit -m "ajout fichier oublié"`

<details>
<summary>Voir la réponse</summary>

**Réponse : A**

**Explication** :  
`git commit --amend` modifie le dernier commit (ajoute des fichiers ou change le message).

**Workflow** :
```bash
git add fichier_oublie.py
git commit --amend --no-edit  # Garde le même message
# Ou : git commit --amend -m "nouveau message"
```

**Pourquoi pas les autres** :
- B : Annule le commit (les fichiers redeviennent non committés)
- C : Crée un **nouveau** commit qui annule le précédent (historique pollué)
- D : Crée un 2e commit séparé (pas de modification du 1er)

**⚠️ ATTENTION** : N'utilise `--amend` que AVANT `git push`. Après push, ça réécrit l'historique (problème si d'autres personnes ont cloné).

</details>

---

### Question 6
Tu cloches ton repo dans `/tmp` pour tester. Quelle commande utilises-tu ?

- A) `git download https://github.com/user/repo.git`
- B) `git clone https://github.com/user/repo.git`
- C) `git pull https://github.com/user/repo.git`
- D) `git fetch https://github.com/user/repo.git`

<details>
<summary>Voir la réponse</summary>

**Réponse : B**

**Explication** :  
`git clone` télécharge un repo complet (code + historique Git) dans un nouveau dossier.

**Syntaxe** :
```bash
cd /tmp
git clone https://github.com/user/repo.git
cd repo  # Le dossier est créé automatiquement
```

**Pourquoi pas les autres** :
- A : `git download` n'existe pas
- C : `git pull` = mise à jour d'un repo **déjà cloné** (télécharge les nouveaux commits)
- D : `git fetch` = télécharge les commits sans les appliquer (manuel)

**Différence clone vs pull** : `clone` = 1ère fois, `pull` = mise à jour.

</details>

---

## Partie B — Comprendre (4 questions ouvertes)

### Question 7
Explique en 3 étapes ce qui se passe entre `git init` et voir ton README sur GitHub.

<details>
<summary>Voir la réponse</summary>

**Réponse attendue** (3 points clés) :

1. **`git init`** : Crée le dossier caché `.git/` qui stocke l'historique des versions (base de données locale Git).

2. **`git add . → git commit`** : Crée un snapshot (photo) de tous les fichiers à un instant T. Ce snapshot est stocké dans `.git/` avec un hash unique (ex: `a3f2c1b`).

3. **`git remote add origin <URL> → git push`** : Envoie les commits locaux vers GitHub (serveur distant). GitHub affiche automatiquement le README.md à la racine.

**Validation** : Mention de `.git/`, notion de snapshot, et lien local→distant.

**Lien avec valeur client** : Le client peut cloner ton repo et avoir **exactement** le même code que toi, avec l'historique complet (qui a changé quoi, quand).

</details>

---

### Question 8
Un client te demande pourquoi tu n'as pas versionné les modèles `.pkl` dans GitHub. Que lui réponds-tu ? (3 arguments)

<details>
<summary>Voir la réponse</summary>

**Réponse attendue** (3 points clés) :

1. **Taille** : Un modèle `.pkl` fait 10-500 Mo. Versionner 10 versions = 5 GB → repo GitHub bloqué (limite 1 GB). Clone du repo = 10 minutes au lieu de 10 secondes.

2. **Reproductibilité** : Les modèles sont des **artefacts générés** par `make train`. Versionner le code source (train.py) suffit → n'importe qui peut régénérer le `.pkl` à l'identique.

3. **Sécurité** : Un modèle peut contenir des données d'entraînement (risque de fuite). Mieux vaut le stocker dans un **Model Registry** (MLflow, S3) avec contrôle d'accès.

**Validation** : Arguments techniques (taille) + opérationnels (reproductibilité) + sécurité.

**Bonus** : "En S5, je mettrai en place MLflow Model Registry pour versionner les modèles proprement, avec rollback 1-click."

</details>

---

### Question 9
L'API retourne une erreur 404 après `git push`. Décris ton processus de debugging en 3 étapes.

<details>
<summary>Voir la réponse</summary>

**Réponse attendue** (3 étapes) :

1. **Vérifier que le code est bien pushé** :
   ```bash
   # Sur GitHub, rafraîchir la page → vérifier que les derniers commits apparaissent
   git log --oneline  # Comparer avec les commits visibles sur GitHub
   ```

2. **Vérifier que le serveur local utilise le bon code** :
   ```bash
   cd ~/mlops_env_utile
   git status  # Doit afficher "working tree clean"
   # Si des fichiers modifiés apparaissent → ils ne sont pas committés
   ```

3. **Redémarrer le serveur** :
   ```bash
   # Arrêter le serveur (Ctrl+C)
   make serve
   # Le serveur charge le code au démarrage, pas en live
   ```

**Validation** : Méthodologie structurée (vérification serveur distant → local → redémarrage), pas "je réessaie au hasard".

**Erreur fréquente** : Modifier le code, commit/push, mais **oublier de redémarrer** le serveur → l'API utilise toujours l'ancien code en mémoire.

</details>

---

### Question 10
Pourquoi le `.gitignore` est-il nécessaire ? Que se passerait-il sans ?

<details>
<summary>Voir la réponse</summary>

**Réponse attendue** (3 points) :

1. **Raison technique** : Empêche de versionner des fichiers temporaires (`__pycache__/`, `.DS_Store`) ou lourds (`*.pkl`, `mlruns/`). Sans `.gitignore`, chaque `git add .` inclurait 50+ fichiers inutiles.

2. **Conséquence si absent** : 
   - Repo pollué (historique illisible)
   - Clone lent (gigaoctets de logs MLflow)
   - Conflits Git sur des fichiers auto-générés (ex: `.pyc`)

3. **Impact métier** : Un client qui clone ton repo reçoit 1 GB de données inutiles → mauvaise première impression → "ce dev n'est pas pro".

**Validation** : Lien workflow (git add) → conséquence technique (taille) → impact client (professionnalisme).

**Bonus** : ".gitignore est comme un filtre anti-spam pour Git : il laisse passer uniquement le code source utile."

</details>

---

## Barème & Interprétation

| Score | Niveau | Action |
|-------|--------|--------|
| 9-10 | ⭐⭐⭐ Excellent | Prêt pour S3 (tests pytest) |
| 7-8 | ⭐⭐ Bien | Réviser questions ratées, puis S3 |
| 5-6 | ⭐ Fragile | Refaire TP S2 (créer un 2e repo test) |
| 0-4 | ⚠️ Lacunes | Consolider Git (tutoriel interactif : learngitbranching.js.org) |

---

## Auto-évaluation

**Questions à se poser après le quiz** :

1. **Peux-tu expliquer la différence entre `git add`, `git commit`, et `git push` à un ami non-technique ?**  
   → Si oui : tu comprends le flux local→distant.

2. **Peux-tu diagnostiquer pourquoi un fichier `.pkl` apparaît sur GitHub alors que tu as un `.gitignore` ?**  
   → Si oui : tu maîtrises le debugging Git.

3. **Peux-tu créer un repo GitHub from scratch en <5 min, sans tutoriel ?**  
   → Si oui : tu as automatisé le workflow S2.

Si 3 × oui → **S2 solidement acquise** 🎉