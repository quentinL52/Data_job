#!/bin/bash

# Mettre à jour les paquets
apt-get update

# Installer Chromium
apt-get install -y chromium-browser

# Créer un lien symbolique pour Google Chrome
ln -s /usr/bin/chromium-browser /usr/bin/google-chrome
