def save_hashes_to_file(file_hashes, output_file):
    """
    Enregistre les hashes des fichiers dans un fichier de sortie.
    
    Args:
        file_hashes (dict): Un dictionnaire contenant les chemins des fichiers en tant que clés et les hashes correspondants en tant que valeurs.
        output_file (str): Le chemin du fichier de sortie.
    """
    try:
        with open(output_file, 'w') as file:
            for file_path, file_hash in file_hashes.items():
                file.write(f"{file_path}:{file_hash}\n")
    except FileNotFoundError:
        print(f"Erreur : Le fichier de sortie {output_file} est introuvable.")
    except PermissionError:
        print(f"Erreur : Vous n'avez pas les autorisations nécessaires pour écrire dans le fichier {output_file}.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'enregistrement des hashes dans le fichier {output_file} : {e}")