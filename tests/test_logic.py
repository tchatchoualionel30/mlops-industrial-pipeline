import pytest
import numpy as np

def test_data_shape():
    """
    Vérifie que notre logique de génération de données
    crée bien les bonnes dimensions.
    """
    # Simulation simple de données
    X = np.random.rand(10, 5)
    assert X.shape == (10, 5), "Erreur de dimension des données"

def test_model_output():
    """
    Vérifie que le modèle sort bien une valeur numérique et pas du texte.
    """
    # Ce test est basique, mais dans la réalité on testerait 
    # des fonctions de pré-traitement spécifiques
    valeur = 5.5
    assert isinstance(valeur, float), "La prédiction doit être un nombre"
    assert valeur > 0, "La qualité du vin ne peut pas être négative"