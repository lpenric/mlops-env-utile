# Test Compréhension Opérationnelle S2

**Durée** : 10 minutes  
**Format** : Réponses courtes (3-5 phrases), en langage naturel (pas de code)

---

## Instructions

Réponds à ces 5 questions **sans regarder les fichiers ni la documentation**. Si tu bloques sur 2+ questions, consolide S2 avant de passer à S3.

---

### Question 1 — Flux de bout en bout

Décris en 4-5 étapes ce qui se passe entre `git init` et voir ton README affiché sur la page GitHub de ton repo.

**Réponse attendue** (éléments clés) :

1. **`git init`** : Crée le dossier caché `.git/` dans ton projet. Ce dossier stocke toute la base de données Git (historique des modifications, commits, branches).

2. **`git add . && git commit -m "message"`** : Crée un snapshot (photo) de tous les fichiers à l'instant T. Ce snapshot est stocké localement dans `.git/` avec un identifiant unique (hash, ex: `a3f2c1b`).

3. **`git remote add origin <URL>`** : Lie ton repo local à un repo distant sur GitHub. C'est comme enregistrer l'adresse d'un serveur distant dans ton carnet.

4. **`git push -u origin main`** : Envoie les commits locaux vers GitHub (transfert réseau). GitHub reçoit les fichiers + l'historique complet.

5. **Affichage automatique** : GitHub détecte `README.md` à la racine et l'affiche automatiquement en Markdown sur la page d'accueil du repo.

**Validation** : 
- Mention de `.git/` (stockage local)
- Notion de snapshot/commit
- Distinction local (`.git/`) vs distant (GitHub)
- Rôle automatique du README

---

### Question 2 — Modification simple

Un client veut que tu changes le message du premier commit de "S1: Premier service" à "S1: API MLOps UHI + screenshots". Que fais-tu et pourquoi ?

**Réponse attendue** :

**Ce que je fais** :
```bash
git commit --amend -m "S1: API MLOps UHI + screenshots"
git push -f origin main
```

**Pourquoi** :
- `git commit --amend` modifie le dernier commit (message ou contenu)
- `-f` (force push) est nécessaire car j'ai réécrit l'historique (le hash du commit a changé)
- **ATTENTION** : Ne faire ça que si personne d'autre n'a cloné le repo, sinon ça crée des conflits

**Alternative si déjà partagé** : Créer un nouveau commit avec le bon message, et expliquer dans un 2e commit : "docs: clarification message commit précédent".

**Validation** : Compréhension de `--amend` + risques de réécriture d'historique + alternative si repo partagé.

---

### Question 3 — Debugging

Tu fais `git push` et GitHub affiche "error: failed to push some refs". Décris ton processus de debugging en 3 étapes concrètes.

**Réponse attendue** :

**Étape 1 : Lire le message d'erreur complet**
- Souvent, Git indique si le problème est : authentification, commits en retard sur le distant, ou branch protection.
- Exemple fréquent : "Updates were rejected because the remote contains work that you do not have locally"

**Étape 2 : Vérifier l'état local vs distant**
```bash
git status  # Vérifie que tous les changements sont committés
git log --oneline  # Compare avec les commits visibles sur GitHub
```

**Étape 3 : Synchroniser si nécessaire**
- Si le distant a des commits que tu n'as pas : `git pull origin main` (télécharge et fusionne)
- Si conflit d'authentification : vérifier PAT ou SSH
- Si tu veux forcer (DANGEREUX) : `git push -f` (écrase le distant)

**Validation** : Méthodologie structurée (lecture erreur → diagnostic local/distant → synchronisation), pas "je retente au hasard".

---

### Question 4 — Dépendances

Pourquoi le `.gitignore` exclut `*.pkl` mais PAS `docs/screenshots/*.png` ? Que se passerait-il si on excluait aussi les screenshots ?

**Réponse attendue** :

**Raison technique** :
- `.pkl` = fichiers lourds (10-500 Mo), auto-générés par `make train`, reproductibles → pas de valeur dans l'historique Git
- `.png` screenshots = légers (50-200 Ko), créés manuellement, servent de **preuve sociale** pour le portfolio → doivent être versionnés

**Conséquence si screenshots exclus** :
- Le README afficherait des liens cassés (images introuvables sur GitHub)
- Un client qui clone le repo ne verrait pas les preuves visuelles → impact négatif sur la crédibilité
- Perte de l'élément différenciateur du portfolio (pas de capture = client doit "imaginer" le résultat)

**Règle générale** : 
- Exclure : fichiers générés automatiquement, lourds, ou contenant des secrets
- Inclure : code source, documentation, assets légers (images, configs)

**Validation** : Distinction fichiers générés vs manuels + impact client + règle générale.

---

### Question 5 — Pitch client

Un client te demande "Qu'as-tu livré cette semaine S2 ?". Réponds en 2-3 phrases, focus valeur métier (pas jargon technique).

**Réponse attendue** :

**Pitch 1 (angle maintenance/collaboration)** :
"J'ai mis en place un système de versioning professionnel pour votre projet MLOps. Désormais, chaque modification du code est tracée, vous pouvez revenir en arrière en cas d'erreur, et n'importe quel développeur peut cloner le projet et contribuer sans risque de conflit. Votre code est également accessible publiquement sur GitHub, ce qui renforce votre image de marque technique."

**Pitch 2 (angle rapidité/fiabilité)** :
"J'ai configuré un système de sauvegarde automatique du code sur GitHub, avec des règles pour éviter de versionner des fichiers inutiles (gain de vitesse : le repo reste léger, clone en 5 secondes au lieu de 5 minutes). Si quelque chose casse demain, on peut revenir à la version stable d'hier en 1 clic."

**Pitch 3 (angle portfolio/preuve sociale)** :
"J'ai rendu votre projet accessible publiquement sur GitHub avec des captures d'écran qui montrent l'API en action. Ça sert de vitrine technique : n'importe qui peut voir la qualité du travail sans devoir installer le projet. C'est un atout pour attirer des partenaires ou lever des fonds."

**Validation** :
- Pas de jargon (Git, commit, push, remote)
- Focus bénéfices concrets (vitesse, sécurité, collaboration, image)
- Langage accessible à un non-technique
- Ancrage valeur métier (gain de temps, réduction risque, crédibilité)

---

## Barème

| Score | Niveau | Action |
|-------|--------|--------|
| 5/5 ✅ | Compréhension opérationnelle solide | Prêt pour S3 |
| 3-4 ⚠️ | Compréhension partielle | Refaire le TP S2 (créer un 2e repo test), revoir concepts flous |
| 0-2 ❌ | Cargo cult (rituels sans compréhension) | NE PAS passer à S3, consolider S2 |

**Critère de validation** : Tu peux expliquer **en langage naturel** (pas réciter des commandes Git).

---

## Anti-patterns à éviter

❌ **Réponse type cargo cult** :
- "Je fais `git push` parce que c'est dans le PLAN_MAITRE"
- "Je sais pas pourquoi .gitignore, mais ça marche"
- Récitation de commandes sans expliquer le flux de données

✅ **Réponse opérationnelle correcte** :
- Mention du flux local → distant (`.git/` → GitHub)
- Lien cause-effet ("sans `.gitignore`, alors les .pkl sont versionnés, ce qui...")
- Langage naturel ("Git crée un snapshot des fichiers à chaque commit pour...")
- Ancrage valeur client ("Ça permet au client de revenir en arrière si...")