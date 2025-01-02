Configuration de qualité du code et des tests
=============================================

Le fichier ``setup.cfg`` est situé à la racine du projet. Il permet de configurer plusieurs outils essentiels pour maintenir la qualité du code et gérer les tests. Voici une explication détaillée des différentes sections configurées dans ce fichier.

Flake8
------
Flake8 est un outil de vérification de style de code conforme à la PEP8.

Configuration dans ``setup.cfg`` :

.. code-block:: ini

    [flake8]
    max-line-length = 99  # Limite la longueur maximale des lignes à 99 caractères
    exclude = **/migrations/*,venv, config/settings.py, doc/  # Exclut certains dossiers et fichiers

**Explications** :

- ``max-line-length`` : Définit une limite plus permissive pour la longueur des lignes afin d'améliorer la lisibilité.
- ``exclude`` : Ignore les dossiers et fichiers comme les migrations, l'environnement virtuel ``venv``, et les fichiers liés à la documentation.

Pytest
------
Pytest est utilisé pour exécuter les tests unitaires et fonctionnels.

Configuration dans ``setup.cfg`` :

.. code-block:: ini

    [tool:pytest]
    DJANGO_SETTINGS_MODULE = config.settings  # Définit les paramètres Django pour les tests
    python_files = tests.py test_*.py *_tests.py  # Détecte les fichiers de test
    addopts = -v  # Exécute les tests avec une sortie détaillée

**Explications** :

- ``DJANGO_SETTINGS_MODULE`` : Charge les paramètres Django nécessaires pour l'exécution des tests.
- ``python_files`` : Identifie les fichiers contenant les tests grâce à leurs noms.
- ``addopts`` : Active un mode verbeux pour afficher plus d'informations pendant l'exécution des tests.

Coverage
--------
Coverage est utilisé pour mesurer la couverture des tests.

Configuration dans ``setup.cfg`` :

.. code-block:: ini

    [coverage:run]
    omit =
        */tests/*
        */migrations/*
        manage.py

**Explications** :

- ``omit`` : Exclut les fichiers non pertinents pour les rapports de couverture, comme les tests eux-mêmes, les migrations, et ``manage.py``.

Pydocstyle
----------
Pydocstyle vérifie la qualité des docstrings selon les conventions PEP257.

Configuration dans ``setup.cfg`` :

.. code-block:: ini

    [pydocstyle]
    match = (models|views|urls)\.py$  # Analyse uniquement les fichiers models.py, views.py, et urls.py
    match-dir = lettings|profiles|oc_lettings_site  # Limite l'analyse aux dossiers principaux
    ignore = D203, D204, D212, D406, D407, D413  # Ignore certaines règles spécifiques

**Explications** :

- ``match`` : Restreint l'analyse aux fichiers essentiels comme ``models.py``, ``views.py``, et ``urls.py``.
- ``match-dir`` : Limite l'analyse aux dossiers principaux (``lettings``, ``profiles``, et ``oc_lettings_site``).
- ``ignore`` : Désactive certaines règles comme D203 (lignes vides) et D204 (description en une ligne).

Pycodestyle
-----------
Pycodestyle est un autre outil pour vérifier le style de code.

Configuration dans ``setup.cfg`` :

.. code-block:: ini

    [pycodestyle]
    max-line-length = 99  # Autorise jusqu'à 99 caractères par ligne
    exclude = */migrations/*, */tests/*, venv/  # Ignore certains dossiers et fichiers

**Explications** :

- Similaire à Flake8, mais spécifique à l'analyse de style.

Commandes utiles
----------------
Voici des commandes pratiques pour exécuter les outils configurés :

.. code-block:: bash

    # Vérifier le style avec Flake8
    flake8 .

    # Lancer les tests avec Pytest
    pytest

    # Vérifier la couverture avec Coverage
    pytest --cov=.

    # Vérifier les docstrings avec Pydocstyle
    pydocstyle
