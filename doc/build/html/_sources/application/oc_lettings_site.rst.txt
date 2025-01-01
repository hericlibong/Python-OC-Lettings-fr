oc_lettings_site
=================
L'application ``oc_lettings_site`` est utilisée pour gérer la page d'accueil du projet. Elle n'utilise pas de modèles, mais se concentre sur la gestion de la vue principale et des tests associés.

Structure de l'application
--------------------------
Voici une vue d'ensemble des fichiers de l'application :

.. code-block:: none

    oc_lettings_site/
    ├── __init__.py
    ├── admin.py                  # Vide
    ├── apps.py                   # Configuration de l'application
    ├── models.py                 # Vide
    ├── tests/                    # Contient les tests unitaires
    │   ├── test_apps.py
    │   ├── test_views.py
    ├── templates/                # Contient les templates HTML
    │   ├── oc_lettings_site/index.html
    ├── urls.py                   # Définition des routes de l'application
    ├── views.py                  # Logique des vues
    └── migrations/               # Dossier de migrations (aucune migration en attente)


Vue principale
--------------
La vue principale, définie dans ``views.py``, sert à afficher la page d'accueil. Voici les comportements attendus et leurs assertions.

.. code-block:: python

    from django.shortcuts import render
    import logging

    logger = logging.getLogger(__name__)

    def index(request):
        """
        Renders the homepage of the application.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The rendered 'oc_lettings_site/index.html' template.

        Assertions:
            - La vue retourne un objet HttpResponse.
            - Le template utilisé est 'oc_lettings_site/index.html'.
            - Toute erreur est journalisée dans le logger 'oc_lettings_site.views'.
        """
        try:
            return render(request, 'oc_lettings_site/index.html')
        except Exception as e:
            logger.error(f"Error in oc_lettings_site index view: {e}")
            raise

Routes
------
Les routes de l'application sont définies dans ``urls.py`` :

.. code-block:: python

    from django.urls import path
    from . import views

    app_name = 'oc_lettings_site'

    urlpatterns = [
        path('', views.index, name='index'),
    ]

- **Namespace** : ``oc_lettings_site``, utilisé pour éviter les conflits avec d'autres applications.
- Route principale :
  - ``path('', views.index, name='index')`` : Définit la route pour la page d'accueil.

Template
--------
Le template utilisé pour la page d'accueil est ``oc_lettings_site/index.html`` :

.. code-block:: html

    {% extends "base.html" %}
    {% block title %}Holiday Homes{% endblock title %}

    {% block content %}
    <div class="container px-5 py-5 text-center">
        <div class="row justify-content-center">
            <div class="col-lg-8">
                <h1 class="page-header-ui-title mb-3 display-6">Welcome to Holiday Homes</h1>
            </div>
        </div>
    </div>

    <div class="container px-5 py-5 text-center">
        <div class="justify-content-center">
            <a class="btn fw-500 ms-lg-4 btn-primary px-10" href="{% url 'profiles:index' %}">
                Profiles
            </a>
            <a class="btn fw-500 ms-lg-4 btn-primary px-10" href="{% url 'lettings:index' %}">
                Lettings
            </a>
        </div>
    </div>
    {% endblock %}

Tests unitaires
---------------
L'application inclut des tests pour vérifier la configuration de l'application et la vue principale. Voici les comportements attendus, présentés avec des assertions explicites.

1. Test de l'application
~~~~~~~~~~~~~~~~~~~~~~~~
Le fichier ``test_apps.py`` vérifie que la configuration de l'application est correctement enregistrée dans Django.

.. code-block:: python

    from django.apps import apps
    from oc_lettings_site.apps import OCLettingsSiteConfig

    def test_oc_lettings_site_app():
        """
        Test that the OCLettingsSiteConfig is correctly registered in Django.

        Assertions:
            - Le nom de l'application est bien 'oc_lettings_site'.
            - L'application est enregistrée correctement dans Django.
        """
        assert OCLettingsSiteConfig.name == 'oc_lettings_site'
        assert apps.get_app_config('oc_lettings_site').name == 'oc_lettings_site'

2. Test de la vue
~~~~~~~~~~~~~~~~~
Le fichier ``test_views.py`` contient des tests pour valider le fonctionnement de la vue principale (index).

**Test 1 : Fonctionnement normal**

.. code-block:: python

    from django.test import TestCase
    from django.urls import reverse

    class OcLettingsSiteViewsTest(TestCase):
        def test_index_view(self):
            """
            Teste que la vue 'index' retourne un statut 200 et utilise le bon template.

            Assertions:
                - La réponse HTTP a un statut 200.
                - Le template utilisé est 'oc_lettings_site/index.html'.
                - Le contenu 'Welcome to Holiday Homes' est présent dans la réponse.
            """
            response = self.client.get(reverse('oc_lettings_site:index'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'oc_lettings_site/index.html')
            self.assertContains(response, 'Welcome to Holiday Homes')

**Test 2 : Gestion des erreurs**

.. code-block:: python

    from unittest.mock import patch
    from django.test import TestCase
    from django.urls import reverse
    import logging

    logger = logging.getLogger("oc_lettings_site.views")

    class OcLettingsSiteViewsTest(TestCase):
        def test_index_view_logs_error(self):
            """
            Test que la vue index journalise une erreur et lève une exception en cas d'erreur.

            Assertions:
                - Une exception est levée lors d'une erreur dans la vue.
                - Un message d'erreur est journalisé avec le logger 'oc_lettings_site.views'.
            """
            with patch("oc_lettings_site.views.render", side_effect=Exception("Test exception")):
                with self.assertLogs("oc_lettings_site.views", level="ERROR") as log:
                    with self.assertRaises(Exception):
                        self.client.get(reverse("oc_lettings_site:index"))
                    self.assertTrue(
                        any(
                            "Error in oc_lettings_site index view: Test exception" in message
                            for message in log.output
                        ),
                        f"Logs enregistrés: {log.output}",
                    )


Migrations
----------
Le dossier ``migrations`` a subi une refactorisation pour stabiliser la structure. Aucune migration supplémentaire n'est attendue, car l'application ne contient pas de modèles.
