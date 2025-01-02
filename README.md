# Orange County Lettings App

## Présentation

Orange County Lettings App est une application web développée en Django pour la gestion des profils utilisateurs et des annonces de locations immobilières. Ce projet a été conçu pour fournir une plateforme intuitive où les utilisateurs peuvent :

- Créer, consulter et modifier leurs profils.
- Ajouter et gérer des annonces de biens immobiliers.

Le projet inclut une architecture modulaire avec trois applications principales : `oc_lettings_site`, `lettings`, et `profiles`. Chaque composant est conçu pour être autonome et extensible.

---

## Fonctionnalités

### Gestion des Profils Utilisateurs
- Création, modification et affichage des profils utilisateurs.
- Chaque profil est associé à un utilisateur Django standard.
- Stockage des informations telles que la ville préférée de l'utilisateur.

### Gestion des Biens Immobiliers
- Ajout et modification des annonces de biens immobiliers.
- Affichage détaillé des informations d'un bien, telles que l'adresse, le titre, etc.

### Page d'Accueil
- Une page d'accueil centralisant les accès aux différentes sections de l'application.

---

## Instructions pour l'installation

### Prérequis
- Python 3.12
- Git
- Docker (optionnel pour le déploiement)

### Étapes d'installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/hericlibong/Python-OC-Lettings-fr.git
    cd Python-OC-Lettings-FR
    ```

2. Installez les dépendances :
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows : venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Configurez les variables d'environnement en créant un fichier `.env` à la racine :
    ```bash
    SECRET_KEY="votre_clé_secrète"
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    SENTRY_DSN="votre_dsn_sentry"
    ```

4. Lancez les migrations :
    ```bash
    python manage.py migrate
    ```

5. Collectez les fichiers statiques :
    ```bash
    python manage.py collectstatic --noinput
    ```

6. Démarrez le serveur de développement :
    ```bash
    python manage.py runserver
    ```

---

## Instructions pour l'usage

### Accès à l'application
- Page d'accueil : [http://localhost:8000/](http://localhost:8000/)
- Panel d'administration : [http://localhost:8000/admin](http://localhost:8000/admin)
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Déploiement avec Docker

Pour créer une image Docker localement :
```bash
docker build -t orange-county-lettings .
```

Pour exécuter le conteneur Docker :

```bash
docker run -p 8000:8000 orange-county-lettings
```

## Informations complémentaires

### Architecture

Le projet est divisé en trois applications Django principales :

- `oc_lettings_site` : Gère la page d'accueil du projet.
- `lettings` : Gère les annonces de locations immobilières.
- `profiles` : Gère les profils utilisateurs.

### Documentation

La documentation complète est disponible sur [Read the Docs](https://orange-county-lettings-app.readthedocs.io/fr/latest/index.html).

### CI/CD

- Les pipelines CI/CD sont configurés avec GitHub Actions.
- Déploiement automatisé via Render avec des conteneurs Docker.

### Tests

- Couverture complète des tests pour les modèles, vues et URLs.
- Exécution des tests avec pytest :

  ```bash
  pytest --cov=. --cov-report=term-missing
  ```

### Auteur

Créé par Heric Libong dans le cadre du projet P13 d'OpenClassrooms.

