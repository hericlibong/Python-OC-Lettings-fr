# Etape 1: Utiliser une image de base
FROM python:3.12-slim

# Etape 2: Définir le répertoire de travail dans le conteneur
# Set the working directory
WORKDIR /app

# Etape 3: Copier les fichiers de l'app dans le conteneur
# Copy the current directory contents into the container at /app
COPY . /app

# Etape 4: Installer les dépendances
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Etape 5: Collecter les fichiers statiques pour la production
# Collect static files
RUN python manage.py collectstatic --noinput

# Etape 6: Exposer le port pour accéder à l'application
# Make port 8000 available to the world outside this container
EXPOSE 8000

# Etape 7: Commmande par défaut pour démarrer l'application
# Default command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
