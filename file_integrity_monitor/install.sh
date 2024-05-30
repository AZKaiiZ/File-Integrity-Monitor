#!/bin/bash

# Variables
REPO_URL="https://github.com/AZKaiiZ/File-Integrity-Monitor/raw/main/file_integrity_monitor"
INSTALL_DIR="/usr/local/share/file_integrity_monitor"

# Mettre à jour les sources de paquets
sed -i 's/^deb cdrom/#deb cdrom/' /etc/apt/sources.list

# Mettre à jour la liste des paquets
apt-get update

# Installer les dépendances nécessaires
apt-get install -y python3 python3-venv

# Créer le répertoire pour le projet
mkdir -p $INSTALL_DIR

# Télécharger les fichiers depuis GitHub
wget -O $INSTALL_DIR/hash_utils.py $REPO_URL/hash_utils.py
wget -O $INSTALL_DIR/file_io.py $REPO_URL/file_io.py
wget -O $INSTALL_DIR/integrity_checker.py $REPO_URL/integrity_checker.py
wget -O $INSTALL_DIR/main.py $REPO_URL/main.py

# Créer un environnement virtuel Python
python3 -m venv $INSTALL_DIR/venv

# Activer l'environnement virtuel et installer pyinotify via pip
source $INSTALL_DIR/venv/bin/activate
pip install pyinotify
deactivate

# Ajouter un service systemd pour exécuter le script au démarrage
cat <<EOT > /etc/systemd/system/file_integrity_monitor.service
[Unit]
Description=File Integrity Monitor

[Service]
ExecStart=$INSTALL_DIR/venv/bin/python $INSTALL_DIR/main.py /etc/ -o /home/user/hashes.txt
Restart=always

[Install]
WantedBy=multi-user.target
EOT

# Activer et démarrer le service
systemctl enable file_integrity_monitor.service
systemctl start file_integrity_monitor.service
