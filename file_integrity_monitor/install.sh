#!/bin/bash

# Installer les dépendances nécessaires
apt-get update
apt-get install -y python3 python3-pip
pip3 install pyinotify

# Créer le répertoire pour le projet
mkdir -p /usr/local/share/file_integrity_monitor

# Copier les scripts dans /usr/local/share/file_integrity_monitor
cp hash_utils.py /usr/local/share/file_integrity_monitor/
cp file_io.py /usr/local/share/file_integrity_monitor/
cp integrity_checker.py /usr/local/share/file_integrity_monitor/
cp main.py /usr/local/share/file_integrity_monitor/
cp README.md /usr/local/share/file_integrity_monitor/

# Créer des liens symboliques dans /usr/local/bin pour exécuter les scripts depuis n'importe où
ln -s /usr/local/share/file_integrity_monitor/hash_utils.py /usr/local/bin/hash_utils.py
ln -s /usr/local/share/file_integrity_monitor/file_io.py /usr/local/bin/file_io.py
ln -s /usr/local/share/file_integrity_monitor/integrity_checker.py /usr/local/bin/integrity_checker.py
ln -s /usr/local/share/file_integrity_monitor/main.py /usr/local/bin/main.py

# Ajouter un service systemd pour exécuter le script au démarrage
cat <<EOT > /etc/systemd/system/file_integrity_monitor.service
[Unit]
Description=File Integrity Monitor

[Service]
ExecStart=/usr/bin/python3 /usr/local/share/file_integrity_monitor/main.py /etc/ -o /home/user/hashes.txt
Restart=always

[Install]
WantedBy=multi-user.target
EOT

# Activer et démarrer le service
systemctl enable file_integrity_monitor.service
systemctl start file_integrity_monitor.service
