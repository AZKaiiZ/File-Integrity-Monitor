# File Integrity Monitor

Ce projet surveille l'intégrité des fichiers dans un répertoire donné en calculant les hashs des fichiers et en utilisant `inotify` pour détecter les modifications, créations et suppressions de fichiers.

## Prérequis

- Debian ou une distribution basée sur Debian (par exemple, Ubuntu)
- Python 3
- `pip` (gestionnaire de paquets Python)
- `pyinotify` (bibliothèque Python pour `inotify`)

## Installation

1. Clonez le repository ou téléchargez les fichiers nécessaires.
2. Assurez-vous que le script d'installation `install.sh` est exécutable :

    ```bash
    chmod +x install.sh
    ```

3. Exécutez le script d'installation avec des privilèges root :

    ```bash
    sudo ./install.sh
    ```

Ce script installera les dépendances nécessaires, copiera les scripts dans `/usr/local/share/file_integrity_monitor` et configurera un service systemd pour exécuter le script de surveillance au démarrage.

## Structure du projet

- `hash_utils.py` : Module pour le calcul des hashs des fichiers.
- `file_io.py` : Module pour la sauvegarde des hashs dans un fichier.
- `integrity_checker.py` : Module pour la surveillance de l'intégrité des fichiers.
- `main.py` : Script principal orchestrant l'exécution des autres modules.
- `install.sh` : Script d'installation pour configurer le projet sur une machine Debian.

## Utilisation

### Lancer le service manuellement

Pour démarrer manuellement le service de surveillance de l'intégrité des fichiers, exécutez la commande suivante :

```bash
sudo systemctl start file_integrity_monitor.service
