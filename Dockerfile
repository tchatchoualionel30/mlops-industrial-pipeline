# On part d'une image Python légère officielle
FROM python:3.9-slim

# On définit le dossier de travail dans le conteneur
WORKDIR /app

# On copie les dépendances (juste pour référence)
COPY requirements.txt .

# ⚡ CORRECTION : On installe les paquets manuellement SANS DVC
# Cela évite le conflit "Dependency Hell" avec botocore
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pandas scikit-learn "mlflow>=2.0" pytest numpy dagshub

# On copie tout le code source dans le conteneur
COPY . .

# Variable d'environnement pour MLflow
ENV MLFLOW_TRACKING_URI=""

# Commande par défaut
CMD ["python", "src/train.py"]