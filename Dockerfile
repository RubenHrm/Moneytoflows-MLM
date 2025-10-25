# Étape 1 : Image de base
FROM python:3.11-slim

# Étape 2 : Définir le dossier de travail
WORKDIR /app

# Étape 3 : Copier les fichiers
COPY . .

# Étape 4 : Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : Exposer le port
EXPOSE 3000

# Étape 6 : Lancer le serveur
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:3000"]
