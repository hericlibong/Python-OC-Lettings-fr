lettings
========
L'application ``lettings`` est utilisée pour gérer les propriétés de location. Elle utilise deux modèles principaux : ``Address`` et ``Letting``. Les vues associées permettent de lister les locations disponibles et d'afficher les détails d'une location spécifique.

Structure de l'application
--------------------------
Voici une vue d'ensemble des fichiers de l'application :

.. code-block:: none

    lettings/
    ├── __init__.py
    ├── admin.py              # Enregistre les modèles dans l'admin Django
    ├── apps.py               # Configuration de l'application
    ├── models.py             # Définition des modèles Address et Letting
    ├── templates/            # Templates HTML pour les pages index et letting
    │   ├── index.html
    │   ├── letting.html
    ├── tests/                # Tests unitaires pour les vues et modèles
    │   ├── test_models.py
    │   ├── test_views.py
    ├── urls.py               # Routes spécifiques à l'application lettings
    ├── views.py              # Logique des vues
    └── migrations/           # Fichiers de migration générés automatiquement

Modèles
-------
L'application ``lettings`` utilise deux modèles : ``Address`` et ``Letting``.

1. **Address**

   Ce modèle représente une adresse postale.

   **Champs** :

   - ``number`` : Numéro de rue (entier positif, max 9999).
   - ``street`` : Nom de la rue (chaine de caractères, max 64).
   - ``city`` : Ville (chaine de caractères, max 64).
   - ``state`` : Code d'état (chaine de 2 caractères, ex. "CA").
   - ``zip_code`` : Code postal (entier positif, max 99999).
   - ``country_iso_code`` : Code ISO du pays (chaine de 3 caractères, ex. "USA").

   **Relation** : Ce modèle est utilisé dans une relation one-to-one avec le modèle ``Letting``.

   **Exemple de code** :

   .. code-block:: python

       from django.db import models
       from django.core.validators import MaxValueValidator, MinLengthValidator

       class Address(models.Model):
           number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
           street = models.CharField(max_length=64)
           city = models.CharField(max_length=64)
           state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
           zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
           country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

           def __str__(self):
               return f'{self.number} {self.street}'

2. **Letting**

   Ce modèle représente une propriété de location.

   **Champs** :

   - ``title`` : Nom ou titre de la propriété.
   - ``address`` : Relation one-to-one avec un objet ``Address``.

   **Exemple de code** :

   .. code-block:: python

       class Letting(models.Model):
           title = models.CharField(max_length=256)
           address = models.OneToOneField(Address, on_delete=models.CASCADE)

           def __str__(self):
               return self.title

Vues
----
L'application contient deux vues principales, définies dans ``views.py`` :

1. **index**

   Affiche la liste de toutes les propriétés disponibles.

   **Requête** :

   - Type : GET
   - URL : ``/lettings/``

   **Description** :

   Cette vue récupère tous les objets ``Letting`` et les passe au template ``lettings/index.html``.

   .. code-block:: python

       from django.shortcuts import render
       from .models import Letting

       def index(request):
           lettings_list = Letting.objects.all()
           context = {'lettings_list': lettings_list}
           return render(request, 'lettings/index.html', context)

2. **letting**

   Affiche les détails d'une propriété spécifique.

   **Requête** :

   - Type : GET
   - URL : ``/lettings/<letting_id>/``

   **Description** :

   Cette vue récupère un objet ``Letting`` par son ID et passe les détails au template ``lettings/letting.html``.

   .. code-block:: python

       from django.shortcuts import render
       from .models import Letting

       def letting(request, letting_id):
           letting = Letting.objects.get(id=letting_id)
           context = {
               'title': letting.title,
               'address': letting.address,
           }
           return render(request, 'lettings/letting.html', context)

Routes
------
Les routes de l'application sont définies dans ``urls.py`` :

.. code-block:: python

    from django.urls import path
    from . import views

    app_name = 'lettings'

    urlpatterns = [
        path('', views.index, name='index'),
        path('<int:letting_id>/', views.letting, name='letting'),
    ]

- **Namespace** : ``lettings``, utilisé pour éviter les conflits avec d'autres applications.
  
- Routes principales :
  
  - ``path('', views.index, name='index')`` : Liste des propriétés.
  - ``path('<int:letting_id>/', views.letting, name='letting')`` : Détails d'une propriété.

Templates
---------
1. **index.html**

   Affiche la liste des propriétés.

   **Exemple de contenu** :

   .. code-block:: html

       {% for letting in lettings_list %}
           <li><a href="{% url 'lettings:letting' letting_id=letting.id %}">{{ letting.title }}</a></li>
       {% endfor %}

2. **letting.html**

   Affiche les détails d'une propriété.

   .. code-block:: html

       <p>{{ address.number }} {{ address.street }}</p>
       <p>{{ address.city }}, {{ address.state }} {{ address.zip_code }}</p>
       <p>{{ address.country_iso_code }}</p>


Note sur les migrations
------------------------
.. note::

    Certaines migrations ont été effectuées manuellement pour repositionner correctement les tables
    associées à l'application ``lettings`` dans la base de données. Ces modifications ont permis
    d'assurer une structure cohérente et fonctionnelle. Depuis cette refactorisation, la structure 
    est stable et les tables sont correctement en place.



Tests de l'application lettings
===============================
Les tests de l'application ``lettings`` vérifient la configuration, les modèles, les URLs et les vues associées à la gestion des propriétés de location. Ces tests sont essentiels pour garantir la stabilité et le bon fonctionnement de cette partie de l'application.

Structure des tests
-------------------
Le dossier ``lettings/tests`` contient les tests organisés comme suit :

.. code-block:: none

    lettings/tests/
    ├── __init__.py              # Initialisation du package de tests
    ├── test_apps.py             # Tests pour la configuration de l'application
    ├── test_models.py           # Tests pour les modèles Address et Letting
    ├── test_urls.py             # Tests pour les routes de l'application
    ├── test_views.py            # Tests pour les vues principales (index et letting)

Tests détaillés
---------------

1. Test de la configuration de l'application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Le fichier ``test_apps.py`` vérifie que l'application ``lettings`` est correctement configurée dans Django.

.. code-block:: python

    from django.apps import apps
    from lettings.apps import LettingsConfig

    def test_lettings_app():
        """
        Test that the LettingsConfig is correctly registered in Django.

        Assertions:
            - Le nom de l'application est bien 'lettings'.
            - L'application est enregistrée correctement dans Django.
        """
        assert LettingsConfig.name == 'lettings'
        assert apps.get_app_config('lettings').name == 'lettings'

2. Tests des modèles
~~~~~~~~~~~~~~~~~~~~
Le fichier ``test_models.py`` vérifie le fonctionnement des modèles ``Address`` et ``Letting``.

**Test 1 : Représentation sous forme de chaîne**

.. code-block:: python

    from django.test import TestCase
    from lettings.models import Letting, Address

    class LettingsModelTests(TestCase):
        def test_address_str(self):
            """
            Test the string representation of the Address model.

            Assertions:
                - La méthode __str__ d'Address retourne '123 Main St'.
            """
            address = Address.objects.create(
                number=123,
                street='Main St',
                city='Springfield',
                state='IL',
                zip_code=62701,
                country_iso_code='USA'
            )
            self.assertEqual(str(address), '123 Main St')

        def test_letting_str(self):
            """
            Test the string representation of a Letting instance.

            Assertions:
                - La méthode __str__ de Letting retourne 'Test Letting'.
            """
            address = Address.objects.create(
                number=123,
                street='Main St',
                city='Springfield',
                state='IL',
                zip_code=62701,
                country_iso_code='USA'
            )
            letting = Letting.objects.create(
                title='Test Letting',
                address=address
            )
            self.assertEqual(str(letting), 'Test Letting')

3. Tests des URLs
~~~~~~~~~~~~~~~~~
Le fichier ``test_urls.py`` vérifie que les routes définies dans ``lettings/urls.py`` pointent correctement vers les vues correspondantes.

.. code-block:: python

    from django.urls import reverse, resolve
    from django.test import SimpleTestCase
    from lettings.views import index, letting

    class TestUrls(SimpleTestCase):
        def test_index_url_resolves(self):
            """
            Test the URL resolution for the index view.

            Assertions:
                - La route 'lettings:index' est associée à la vue 'index'.
            """
            url = reverse('lettings:index')
            self.assertEqual(resolve(url).func, index)

        def test_letting_url_resolves(self):
            """
            Test the URL resolution for the letting view.

            Assertions:
                - La route 'lettings:letting' est associée à la vue 'letting'.
            """
            url = reverse('lettings:letting', args=[1])
            self.assertEqual(resolve(url).func, letting)

4. Tests des vues
~~~~~~~~~~~~~~~~~
Le fichier ``test_views.py`` contient des tests pour valider les vues principales (index et letting).

**Test 1 : Vue index**

.. code-block:: python

    from django.test import TestCase
    from django.urls import reverse
    from lettings.models import Letting, Address

    class LettingViewsTest(TestCase):
        def setUp(self):
            address = Address.objects.create(
                number=123,
                street='Main St',
                city='Springfield',
                state='IL',
                zip_code=62701,
                country_iso_code='USA'
            )
            Letting.objects.create(
                title='Test Letting',
                address=address
            )

        def test_index_view(self):
            """
            Teste que la vue index retourne le bon statut et utilise le bon template.

            Assertions:
                - Le statut HTTP est 200.
                - Le template utilisé est 'lettings/index.html'.
            """
            response = self.client.get(reverse('lettings:index'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'lettings/index.html')

**Test 2 : Vue letting**

.. code-block:: python

        def test_letting_view(self):
            """
            Teste que la vue letting retourne le bon statut et utilise le bon template.

            Assertions:
                - Le statut HTTP est 200.
                - Le template utilisé est 'lettings/letting.html'.
            """
            letting = Letting.objects.first()
            response = self.client.get(reverse('lettings:letting', args=[letting.id]))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'lettings/letting.html')

**Test 3 : Gestion des erreurs**

.. code-block:: python

        def test_index_view_logs_error(self):
            """
            Test that an exception in the index view is logged and raised.

            Assertions:
                - Une exception est levée lors d'une erreur dans Letting.objects.all().
                - Le message d'erreur est journalisé dans les logs.
            """
            from unittest.mock import patch

            with patch('lettings.models.Letting.objects.all', side_effect=Exception("Test exception")):
                with self.assertLogs('lettings.views', level='ERROR') as log:
                    with self.assertRaises(Exception):
                        self.client.get(reverse('lettings:index'))
                    self.assertTrue(
                        any("Error in lettings index view: Test exception" in message
                            for message in log.output)
                    )




