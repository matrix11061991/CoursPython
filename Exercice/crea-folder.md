Exemple de code Python qui crée une architecture de dossiers et de fichiers de manière récursive. 
Il faut avoir les autorisations nécessaires pour créer des dossiers et des fichiers à l'emplacement spécifié.
```python
import os
def creer_architecture(dossier_parent, structure):
    for nom, contenu in structure.items():
        chemin = os.path.join(dossier_parent, nom)
        if isinstance(contenu, dict):
            os.makedirs(chemin)
            creer_architecture(chemin, contenu)
        else:
            with open(chemin, 'w') as f:
                f.write(contenu)

# Exemple d'architecture de dossiers et de fichiers
structure = {
    'dossier1': {
        'fichier1.txt': 'Contenu du fichier 1',
        'dossier2': {
            'fichier2.txt': 'Contenu du fichier 2'
        }
    }
}

# Chemin du dossier parent où vous voulez créer la structure
dossier_parent = 'chemin/du/dossier/parent'  # Modifier avec le chemin réel

# Appel de la fonction pour créer l'architecture
creer_architecture(dossier_parent, structure)

```
