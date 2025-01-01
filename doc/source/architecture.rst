Architecture
=============

Ce projet suit une architecture Django standard, organisée pour faciliter le développement et la maintenance.

Arborescence
-------------
Voici une vue d'ensemble des dossiers principaux du projet :

.. code-block:: none

    Python-OC-Lettings-FR/
    ├── config/                # Configuration principale (settings, urls, wsgi)
    ├── lettings/              # Application pour les biens immobiliers
    ├── profiles/              # Application pour les profils utilisateurs
    ├── static/                # Fichiers statiques globaux (CSS, JS, images)
    ├── templates/             # Templates partagés entre les applications
    ├── manage.py              # Commande principale de gestion Django
    └── oc-lettings-site.sqlite3  # Base de données SQLite incluse


Applications
------------

- ``oc_lettings_site/`` :
    - Fournit la vue et les routes pour la page d'accueil. Cette application ne contient pas de modèles.

- ``lettings/`` :
    - Gère les biens immobiliers et leurs détails.
    - Structure typique :
        - ``models.py`` : Définit les modèles de données pour les biens immobiliers.
        - ``views.py`` : Logique métier pour gérer les annonces.
        - ``urls.py`` : Routes spécifiques à cette application.
        - ``admin.py`` : Personnalisation de l'interface d'administration.
        - ``tests/`` : Tests unitaires pour cette application.
        - ``templates/`` : Templates HTML associés.
        - ``apps.py`` : Configuration de l'application.

- ``profiles/`` :
    - Gère les profils utilisateurs.
    - Structure similaire à ``lettings``.

Statique et Templates
---------------------
- ``static/`` : Contient les fichiers statiques globaux (CSS, JS, images).
- ``templates/`` : Regroupe les templates globaux du projet, partagés entre les applications.

