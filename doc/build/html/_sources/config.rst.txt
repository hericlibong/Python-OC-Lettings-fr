Configuration principale
=========================
Le répertoire ``config`` contient les fichiers essentiels à la configuration et au fonctionnement global du projet :

- ``settings.py`` : Définit les paramètres globaux du projet (bases de données, applications installées, variables d’environnement, etc.).
- ``urls.py`` : Centralise les routes globales du projet et inclut les URLs des applications.
- ``wsgi.py`` : Point d’entrée pour le serveur web en mode WSGI.
- ``asgi.py`` : Point d’entrée pour le serveur web en mode ASGI (asynchrone).

Ce répertoire n'est pas une application Django mais joue un rôle crucial dans la gestion du projet.

settings.py
-----------
Le fichier ``settings.py`` configure les paramètres globaux du projet Django, en distinguant les environnements de développement et de production. Voici une présentation détaillée des sections clés.

Configuration Sentry
--------------------
Sentry est utilisé pour la journalisation et le suivi des erreurs dans l'application.

- ``DSN Sentry`` : Configuré via la variable d'environnement ``SENTRY_DSN``.
- ``Intégration Django`` : Ajoutée pour capturer les erreurs spécifiques au framework.

Exemple de configuration dans ``settings.py`` :

.. code-block:: python

    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=os.getenv('SENTRY_DSN'),
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
        send_default_pii=True,
        _experiments={
            "continuous_profiling_auto_start": True,
        }
    )

En complément, les erreurs de niveau ``ERROR`` sont également envoyées à Sentry grâce à un handler spécifique dans le dictionnaire ``LOGGING``.

.. code-block:: python

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {module} {message}',
                'style': '{',
            },
            'simple': {
                'format': '{levelname} {message}',
                'style': '{',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
            },
            'sentry': {
                'class': 'sentry_sdk.integrations.logging.EventHandler',
                'level': 'ERROR',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console', 'sentry'],
                'level': 'INFO',
                'propagate': True,
            },
            'lettings.views': {
                'handlers': ['console'],
                'level': 'ERROR',
                'propagate': True,
            },
            '': {
                'handlers': ['console', 'sentry'],
                'level': 'ERROR',
                'propagate': False,
            },
        },
    }

Fonctionnement des composants
-----------------------------
Voici une description détaillée des composants de la configuration ``LOGGING`` :

1. ``formatters``

   Définit le format des messages dans les logs. Par exemple :

   .. code-block:: text

       ERROR 2024-12-31 12:34:56 my_module Une erreur s'est produite

2. ``handlers``

   - ``console`` : Affiche les logs dans le terminal.
   - ``sentry`` : Envoie les logs de niveau ``ERROR`` et supérieur à Sentry.

3. ``loggers``

   - ``django`` : Capture les logs spécifiques à Django.
   - ``lettings.views`` : Définit un logger dédié pour la vue ``lettings``.
   - Logger global (``''``) : Capture tous les logs non assignés à un logger spécifique.

Personnalisation
----------------
Vous pouvez personnaliser la configuration de logging :

- Ajouter des loggers spécifiques pour d'autres modules de l'application.
- Modifier le niveau des logs selon l'environnement (ex. : ``DEBUG`` en développement, ``ERROR`` en production).
- Adapter les formatters pour inclure davantage de détails, comme les adresses IP ou les identifiants utilisateur.

Variables d'environnement
--------------------------
Les variables d'environnement sont utilisées pour sécuriser des informations sensibles et adapter l'application à différents environnements.

Exemples de variables définies dans le fichier ``.env`` :

.. code-block:: bash

    DEBUG=True
    SECRET_KEY=ma_clé_sécurisée
    ALLOWED_HOSTS=localhost,127.0.0.1
    SENTRY_DSN=ma_valeur_dsn

Elles sont chargées dans ``settings.py`` avec la bibliothèque ``python-dotenv`` :

.. code-block:: python

    from dotenv import load_dotenv
    import os

    load_dotenv()

    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    SECRET_KEY = os.getenv('SECRET_KEY')
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')
    SENTRY_DSN = os.getenv('SENTRY_DSN')

Modes Développement et Production
---------------------------------
La variable ``DEBUG`` contrôle si l'application est en mode développement ou production. Par défaut, elle est configurée via ``os.getenv`` pour s'adapter à l'environnement :

.. code-block:: python

    DEBUG = os.getenv('DEBUG', 'False') == 'True'

.. important::
    Ne jamais utiliser ``DEBUG=True`` en production, car cela expose des informations sensibles.

Les hôtes autorisés sont également gérés dynamiquement avec ``ALLOWED_HOSTS`` :

.. code-block:: python

    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')

Base de données
---------------
L'application utilise SQLite comme base de données par défaut. La configuration est simplifiée grâce à ``os.path`` pour générer le chemin dynamiquement :

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'oc-lettings-site.sqlite3'),
        }
    }

Si une autre base de données est nécessaire (par exemple, PostgreSQL), il suffit de modifier la section ``DATABASES`` et d'ajuster les variables d'environnement.

Gestion des fichiers statiques
-------------------------------
Les fichiers statiques sont servis efficacement en production grâce à WhiteNoise. Voici les points clés de la configuration :

- **Répertoire de collecte des fichiers** : Défini par ``STATIC_ROOT``.
- **Répertoire des fichiers sources** : Listé dans ``STATICFILES_DIRS``.
- **Stockage optimisé** : Utilisation de ``CompressedManifestStaticFilesStorage`` pour minimiser et optimiser les fichiers.

Extrait de configuration dans ``settings.py`` :

.. code-block:: python

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

Le middleware WhiteNoise est également ajouté pour servir les fichiers statiques :

.. code-block:: python

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        # Autres middlewares
    ]


urls.py
-------
Le fichier ``urls.py`` du répertoire ``config`` centralise toutes les routes du projet Django. Il utilise le mécanisme d'inclusion pour déléguer la gestion des URLs spécifiques aux applications individuelles.

Voici le contenu du fichier ``urls.py`` :

.. code-block:: python

    from django.contrib import admin
    from django.urls import path, include
    from django.views.defaults import page_not_found, server_error

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('oc_lettings_site.urls', namespace='oc_lettings_site')),
        path('lettings/', include('lettings.urls', namespace='lettings')),
        path('profiles/', include('profiles.urls', namespace='profiles')),
        path('404/', lambda request: page_not_found(request, exception=None)),  # Test 404 page
        path('500/', lambda request: server_error(request)),  # Test 500 page
    ]

Description des composants
--------------------------
1. **Administration Django**

   La route ``admin/`` permet d'accéder à l'interface d'administration fournie par Django.

   Exemple :

   `http://localhost:8000/admin <http://localhost:8000/admin>`_

2. **Inclusions des URLs des applications**

   Chaque application du projet gère ses propres URLs. Le fichier ``urls.py`` principal les inclut en utilisant la fonction ``include``.

   Exemple :

   - ``path('', include('oc_lettings_site.urls', namespace='oc_lettings_site'))`` :
     Inclut les routes définies dans ``oc_lettings_site/urls.py`` et les associe au namespace ``oc_lettings_site``.

   - Cela permet de déléguer la gestion des URLs spécifiques à chaque application.



3. **Pages de test pour les erreurs 404 et 500** 
   
   - Les deux dernières lignes ajoutent des routes de test pour simuler des erreurs :
  
     - ``path('404/', lambda request: page_not_found(request, exception=None))`` : Simule une erreur 404.
     - ``path('500/', lambda request: server_error(request))`` : Simule une erreur 500.
   - Ces routes sont particulièrement utiles pour vérifier que les pages personnalisées d'erreur sont bien configurées.



Concept de namespaces
---------------------
Les namespaces sont utilisés pour organiser et différencier les routes des différentes applications. Cela permet d'éviter les conflits de noms lorsqu'une même route (par exemple, ``index``) est définie dans plusieurs applications.

1. **Namespace global** :
   
  - Défini dans le fichier ``urls.py`` principal via l'inclusion.
  - Exemple :
  
     - ``namespace='lettings'`` assigne toutes les URLs de l'application ``lettings`` au namespace ``lettings``.

2. **Utilisation dans les templates et vues** :
   
  - Les namespaces permettent d'appeler les URLs de manière explicite.
  - Exemple d'utilisation dans un template :
     ```html
     <a href="{% url 'lettings:index' %}">Voir les locations</a>
     ```
  - Ici, ``lettings:index`` appelle la vue ``index`` définie dans l'application ``lettings``.

Proposition d'autres explications
---------------------------------
1. **Avantages de l'inclusion d'URLs** :
   
  - Simplifie la gestion des routes en isolant les URLs propres à chaque application.
  - Facilite la maintenance et la réutilisation des applications.

2. **Utilisation des fonctions Django pour les erreurs** :
   
  - Les fonctions ``page_not_found`` et ``server_error`` appartiennent au module ``django.views.defaults``.
  - Elles fournissent des réponses par défaut pour les erreurs HTTP (404 et 500), mais peuvent être remplacées par des templates personnalisés.

3. **Extensions futures possibles** :
   
  - Ajouter des tests unitaires pour vérifier que les routes renvoient les réponses attendues.
  - Configurer des pages d’erreur plus conviviales avec des templates dédiés.

Exemple de gestion des erreurs dans ``settings.py`` :

.. code-block:: python

    # settings.py
    HANDLER404 = 'config.views.custom_404'
    HANDLER500 = 'config.views.custom_500'



Tests du répertoire config
--------------------------
Le répertoire ``config/tests`` contient les tests unitaires associés aux fichiers de configuration principaux du projet Django. Ces tests assurent que les composants critiques (ASGI, WSGI, et routes globales) fonctionnent correctement.

Arborescence des fichiers
--------------------------
.. code-block:: none

    config/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    ├── tests/
    │   ├── __init__.py
    │   ├── test_asgi.py         # Teste la configuration ASGI
    │   ├── test_urls.py         # Teste les routes globales
    │   └── test_wsgi.py         # Teste la configuration WSGI

Détails des tests
-----------------

1. Test ASGI
~~~~~~~~~~~~
Le fichier ``test_asgi.py`` vérifie que l'application ASGI est correctement chargée.

.. code-block:: python

    from config.asgi import application

    def test_asgi_application():
        """
        Test if the ASGI application is loaded without errors.

        Assertions:
            - The ASGI application instance is not None.
        """
        assert application is not None, "ASGI application is None"

2. Test WSGI
~~~~~~~~~~~~
Le fichier ``test_wsgi.py`` vérifie que l'application WSGI est correctement chargée.

.. code-block:: python

    from config.wsgi import application

    def test_wsgi_application():
        """
        Test that the WSGI application is loaded without errors.

        Assertions:
            - The WSGI application instance is not None.
        """
        assert application is not None, "WSGI application is None"

3. Test des URLs
~~~~~~~~~~~~~~~~
Le fichier ``test_urls.py`` contient des tests pour les routes globales et les namespaces associés aux applications. Il vérifie que les URLs peuvent être résolues correctement.

.. code-block:: python

    from django.test import SimpleTestCase
    from django.urls import reverse, resolve


    class ConfigUrlsTest(SimpleTestCase):
        """
        Tests for the URL configurations in the config directory.

        Methods:
            - test_profiles_namespace: Checks the 'profiles' namespace.
            - test_lettings_namespace: Checks the 'lettings' namespace.
            - test_homepage: Checks the namespace for the homepage.
        """

        def test_profiles_namespace(self):
            """
            Vérifie que l'application 'profiles' a un espace de nom 'profiles'.

            Assertions:
                - The 'profiles:index' URL resolves without errors.
            """
            url = reverse('profiles:index')
            self.assertIsNotNone(resolve(url))

        def test_lettings_namespace(self):
            """
            Vérifie que l'application 'lettings' a un espace de nom 'lettings'.

            Assertions:
                - The 'lettings:index' URL resolves without errors.
            """
            url = reverse('lettings:index')
            self.assertIsNotNone(resolve(url))

        def test_homepage(self):
            """
            Vérifie le namespace de la page d'accueil.

            Assertions:
                - The 'oc_lettings_site:index' URL resolves without errors.
            """
            url = reverse('oc_lettings_site:index')
            self.assertIsNotNone(resolve(url))




Conclusion
----------
Les fichiers ``settings.py`` et ``urls.py`` jouent des rôles essentiels dans la gestion de l'application Django :

- ``settings.py`` :
  
  - Définit les paramètres globaux pour configurer les environnements de développement et de production.
  - Gère les intégrations externes comme Sentry et WhiteNoise pour optimiser la journalisation et les fichiers statiques.
  - Permet une personnalisation avancée via des variables d'environnement.

- ``urls.py`` :
  
  - Centralise la gestion des routes du projet.
  - Utilise l'inclusion pour déléguer les URLs spécifiques aux applications individuelles.
  - Intègre des namespaces pour éviter les conflits entre les applications et pour faciliter la navigation.

Ces deux fichiers combinés assurent la flexibilité et la modularité de l'application, en permettant une configuration robuste et une gestion claire des routes. Leur bonne compréhension est essentielle pour maintenir et étendre l'application.

- ``tests/``:

Les tests dans ``config/tests`` garantissent que les composants critiques du répertoire ``config`` (ASGI, WSGI et URLs) fonctionnent correctement. Ils sont essentiels pour prévenir les régressions et assurer la stabilité du projet.



Vous êtes maintenant prêt à explorer les applications du projet et leur structure spécifique.



