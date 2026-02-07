# 🍷 Industrial MLOps Pipeline: Wine Quality Prediction

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Pipeline](https://img.shields.io/badge/Pipeline-CI%2FCD-green)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-orange)

## 📖 Description du Projet

Ce projet n'est pas seulement un modèle de Machine Learning, c'est une **usine logicielle complète (End-to-End MLOps Pipeline)**.

Il implémente les meilleures pratiques du **DevOps appliqué à la Data Science** pour garantir que chaque modification du code est testée, validée et déployée automatiquement.

L'objectif est de prédire la qualité du vin à partir de caractéristiques physico-chimiques, mais le véritable but est de démontrer une architecture robuste et automatisée.

---

## 🏗️ Architecture & Stack Technique

Le projet repose sur une chaîne d'automatisation moderne :

| Outil | Rôle dans le projet |
| :--- | :--- |
| **🐍 Python & Scikit-learn** | Entraînement du modèle (Random Forest Regressor). |
| **🐙 GitHub Actions** | Orchestration du pipeline CI/CD (Automatisation des tâches). |
| **🧪 Pytest** | Tests unitaires pour valider la qualité du code et des données. |
| **📈 MLflow & DagsHub** | Tracking des expériences (Expérimentation), logging des métriques (RMSE, MAE) et registre de modèles. |
| **🐳 Docker** | Conteneurisation de l'application pour la portabilité (Build & Push vers Docker Hub). |
| **☁️ DVC (Data Version Control)** | Gestion et versioning des datasets. |

---

## 🚀 Le Pipeline CI/CD (Automatisation)

À chaque `git push` sur la branche principale, un workflow GitHub Actions se déclenche et exécute les étapes suivantes séquentiellement :

### 1. 🛡️ Intégration Continue (CI) - `test-code`
* Installation de l'environnement Python.
* Vérification de la syntaxe du code (Linting).
* Exécution des **tests unitaires** avec `pytest` pour garantir que la logique de génération de données et d'entraînement est saine.
* *Si cette étape échoue, le pipeline s'arrête.*

### 2. 🧠 Entraînement Continu (CT) - `train-and-register`
* Récupération/Génération des données.
* Entraînement du modèle **RandomForest**.
* Calcul des performances (RMSE).
* **Logging automatique** des paramètres et métriques vers le serveur distant **DagsHub** via MLflow.
* Sauvegarde du modèle entraîné (`model.pkl`) dans le registre d'artefacts.

### 3. 📦 Déploiement Continu (CD) - `build-and-push-docker`
* Construction d'une image **Docker** optimisée (utilisation de `--no-cache-dir` pour réduire la taille).
* L'image contient tout l'environnement nécessaire pour exécuter le modèle.
* Envoi automatique (Push) de l'image sur **Docker Hub**.
* *Résultat :* Le modèle est prêt à être téléchargé et lancé n'importe où avec une simple commande `docker run`.

---

## 📂 Structure du Projet

```bash
├── .github/workflows
│   └── mlops.yaml      # Le cerveau de l'automatisation (Instructions du Robot)
├── src
│   ├
│   └── train.py        # Script de préparation/génération des données, d'entraînement et de logging MLflow
├── tests
│   └── test_logic.py   # Tests unitaires (Pytest)
├── Dockerfile          # La recette pour construire le conteneur
├── requirements.txt    # Liste des dépendances Python
└── README.md           # Documentation
🛠️ Installation et Utilisation Locale
Si vous souhaitez exécuter ce projet sur votre propre machine :

Option 1 : Via Python
Bash
# 1. Cloner le repo
git clone [https://github.com/votre-user/votre-repo.git](https://github.com/votre-user/votre-repo.git)
cd votre-repo

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer l'entraînement
python src/train.py
Option 2 : Via Docker (Recommandé)
Récupérez l'image prête à l'emploi directement depuis le Docker Hub :

Bash
# Télécharger et lancer l'image (Remplacer par votre pseudo)
docker run tchatchoualionel30/wine-quality-model:latest
🔐 Configuration des Secrets
Pour que ce pipeline fonctionne, les variables suivantes ont été configurées dans les Secrets GitHub :

MLFLOW_TRACKING_URI : L'adresse du serveur DagsHub.

MLFLOW_TRACKING_USERNAME : Nom d'utilisateur DagsHub.

MLFLOW_TRACKING_PASSWORD : Token d'accès DagsHub.

DOCKERHUB_USERNAME : Nom d'utilisateur Docker Hub.

DOCKERHUB_TOKEN : Token d'accès Docker Hub (avec droits Read & Write).

📊 Résultats
Performance du modèle : Les métriques (RMSE, MAE) sont visibles publiquement sur le tableau de bord DagsHub du projet.

Disponibilité : L'image Docker est disponible publiquement sur Docker Hub.

👤 Auteur
Projet réalisé par TCHATCHOUA LIONEL dans le cadre d'un projet MLOps pratique.