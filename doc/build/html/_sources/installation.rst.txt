Installation
============

Ce guide explique comment configurer le projet **Python OC Lettings** en local.

Prérequis
---------
Assurez-vous que votre environnement dispose des éléments suivants :

- Python 3.10 ou 3.12 installé.
- Git installé pour cloner le dépôt.
- Un environnement virtuel configuré (optionnel mais recommandé).

Clonage du projet
------------------
Cloner le dépôt en exécutant la commande suivante dans votre terminal :

.. code-block:: bash

    git clone https://github.com/hericlibong/Python-OC-Lettings-fr.git
    cd Python-OC-Lettings-fr

Installation des dépendances
----------------------------
Créez un environnement virtuel et activez-le :

.. code-block:: bash

    python -m venv venv
    source venv/bin/activate    # Sur Linux/Mac
    venv\Scripts\activate       # Sur Windows

Installez les dépendances nécessaires :

.. code-block:: bash

    pip install -r requirements.txt

Configuration des variables d'environnement
-------------------------------------------
Créez un fichier `.env` dans le répertoire racine et configurez les variables nécessaires. Voici un exemple :

.. code-block:: bash

    DEBUG=True
    SECRET_KEY=remplacez_par_une_clé_sécurisée_de_settings.py
    ALLOWED_HOSTS=127.0.0.1,localhost
    SENTRY_DSN=remplacez_par_votre_valeur_Sentry

.. note::

    La variable `DEBUG` est configurée dans le fichier `settings.py` pour s’adapter automatiquement à l’environnement (développement ou production).
    Plus d'informations seront données dans la section "Configuration Globale".


Base de données
---------------
L'application utilise une base de données SQLite incluse dans le dépôt (`oc-lettings-site.sqlite3`). 
Recommandations :

- Cette base de données est déjà configurée avec les tables et les données nécessaires. 
- Aucune migration n'est requise pour démarrer. 
- Si besoin, vous pouvez consulter la base avec un outil compatible SQLite (ex. DB Browser for SQLite).


Lancement du serveur
---------------------
Démarrez le serveur local :

.. code-block:: bash

    python manage.py runserver

Accédez ensuite à l'application via [http://localhost:8000](http://localhost:8000).
