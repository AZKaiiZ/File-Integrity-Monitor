import argparse
from hash_utils import take_files_hashes
from file_io import save_hashes_to_file
from integrity_checker import check_file_integrity

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Vérifie l\'intégrité des fichiers en surveillant les modifications.')
    parser.add_argument('directory', type=str, help='Le répertoire à surveiller.')
    parser.add_argument('-o', '--output', type=str, default='hashes.txt', help='Le fichier où les hashes seront sauvegardés.')
    args = parser.parse_args()

    # Prendre les hashes des fichiers lors de l'installation
    file_hashes = take_files_hashes(args.directory)
    if file_hashes:
        save_hashes_to_file(file_hashes, args.output)
    else:
        print("Impossible de générer les hashes des fichiers. Veuillez vérifier les erreurs ci-dessus.")

    # Vérifier l'intégrité des fichiers en surveillant les modifications
    check_file_integrity(args.directory)
