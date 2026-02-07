import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import mlflow
import mlflow.sklearn
import sys
import os

# --- CONFIGURATION ---
# On définit une graine aléatoire pour que les résultats soient reproductibles
np.random.seed(42)

def generate_data():
    """
    Génère un dataset factice de qualité de vin pour l'exemple.
    Dans un vrai projet, on chargerait un CSV (ex: pd.read_csv('data/wine.csv'))
    """
    print("🔄 Génération des données...")
    # 1000 lignes, 10 colonnes (features)
    X = np.random.rand(1000, 10) 
    # La cible (y) est une fonction des features + un peu de bruit aléatoire
    y = X[:, 0] * 2 + X[:, 1] * 5 + np.random.normal(0, 0.1, 1000)
    
    # On crée un DataFrame pour faire propre
    cols = [f"feature_{i}" for i in range(10)]
    df = pd.DataFrame(X, columns=cols)
    df['quality'] = y
    
    # Sauvegarde locale pour DVC (simulation)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/wine_quality.csv", index=False)
    return df

def train_model():
    """
    Fonction principale : Charge les données, entraîne le modèle et log dans MLflow.
    """
    print("🚀 Démarrage de l'entraînement...")

    # 1. Chargement des données
    df = generate_data()
    X = df.drop("quality", axis=1)
    y = df["quality"]

    # 2. Séparation train/test (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # 3. Configuration des hyperparamètres du modèle
    # On pourrait les passer en arguments du script pour l'optimisation
    n_estimators = 100
    max_depth = 5

    # 4. Activation de MLflow
    # On définit l'expérience (le dossier virtuel dans MLflow)
    mlflow.set_experiment("WineQuality_Industrial_Ops")

    with mlflow.start_run():
        print("🤖 Entraînement du modèle Random Forest...")
        rf = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth)
        rf.fit(X_train, y_train)

        # 5. Prédictions et Calcul des métriques
        predictions = rf.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, predictions))
        mae = mean_absolute_error(y_test, predictions)

        print(f"📊 Métriques -> RMSE: {rmse:.4f}, MAE: {mae:.4f}")

        # 6. LOGGING DANS MLFLOW (Crucial pour le MLOps)
        # On enregistre les paramètres utilisés (pour savoir quelle config a donné quel résultat)
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        
        # On enregistre les métriques de performance
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)

        # On enregistre le modèle lui-même pour pouvoir le déployer plus tard
        # "model" est le nom du dossier dans le registre
        mlflow.sklearn.log_model(rf, "model")
        
        # Condition de succès (pour le pipeline CI/CD)
        # Si le modèle est trop mauvais, on peut faire échouer le script
        if rmse > 0.5:
            print("❌ Modèle rejeté : RMSE trop élevé")
            # sys.exit(1) # Décommenter pour bloquer le déploiement si mauvais
        else:
            print("✅ Modèle validé")

if __name__ == "__main__":
    train_model()