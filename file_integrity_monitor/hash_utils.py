import hashlib
import os

def take_file_hash(file_path):
    """
    Calcule le hash SHA-256 d'un fichier.
    
    Args:
        file_path (str): Le chemin du fichier.
    
    Returns:
        str: Le hash SHA-256 du fichier.
    """
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            return hashlib.sha256(content).hexdigest()
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} est introuvable.")
        return None
    except PermissionError:
        print(f"Erreur : Vous n'avez pas les autorisations nécessaires pour accéder au fichier {file_path}.")
        return None
    except Exception as e:
        print(f"Une erreur s'est produite lors du calcul du hash du fichier {file_path} : {e}")
        return None

def take_files_hashes(directory):
    """
    Parcourt récursivement un répertoire et calcule le hash de chaque fichier.
    
    Args:
        directory (str): Le répertoire à parcourir.
    
    Returns:
        dict: Un dictionnaire contenant les chemins des fichiers en tant que clés et les hashes correspondants en tant que valeurs.
    """
    file_hashes = {}
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = take_file_hash(file_path)
                if file_hash:
                    file_hashes[file_path] = file_hash
    except Exception as e:
        print(f"Une erreur s'est produite lors du parcours du répertoire {directory} : {e}")
    return file_hashes