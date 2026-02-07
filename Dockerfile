# On part d'une image Python légère officielle
FROM python:3.9-slim

# On définit le dossier de travail dans le conteneur
WORKDIR /app

# On copie les dépendances
COPY requirements.txt .

# On installe les librairies
# --no-cache-dir permet de garder l'image légère
RUN pip install --no-cache-dir -r requirements.txt

# On copie tout le code source dans le conteneur
COPY . .

# Variable d'environnement pour MLflow (sera surchargée par GitHub Actions)
ENV MLFLOW_TRACKING_URI=""

# Commande par défaut : lancer l'entraînement (ou une API serveuse)
# Pour cet exemple, on lance l'entraînement
CMD ["python", "src/train.py"]