profiles
========
L'application ``profiles`` gère les profils utilisateurs. Elle utilise le modèle Django intégré ``User`` et un modèle personnalisé ``Profile`` pour stocker des informations supplémentaires comme la ville favorite.

Structure de l'application
--------------------------
Voici une vue d'ensemble des fichiers de l'application :

.. code-block:: none

    profiles/
    ├── __init__.py
    ├── admin.py              # Enregistre le modèle Profile dans l'admin Django
    ├── apps.py               # Configuration de l'application
    ├── models.py             # Définition du modèle Profile
    ├── templates/            # Templates HTML pour les pages index et profile
    │   ├── index.html
    │   ├── profile.html
    ├── tests/                # Tests unitaires pour les modèles, vues et URLs
    │   ├── test_apps.py
    │   ├── test_models.py
    │   ├── test_urls.py
    │   ├── test_views.py
    ├── urls.py               # Routes spécifiques à l'application profiles
    ├── views.py              # Logique des vues
    └── migrations/           # Fichiers de migration générés automatiquement

Modèles
-------
L'application utilise un modèle personnalisé pour enrichir le modèle ``User`` de Django.

1. **User**

   Le modèle ``User`` est intégré à Django et fournit les fonctionnalités de base pour la gestion des utilisateurs (nom, prénom, email, etc.).

2. **Profile**

   Ce modèle étend les fonctionnalités du modèle ``User`` en ajoutant un champ optionnel pour la ville favorite.

   **Champs** :

   - ``user`` : Relation one-to-one avec le modèle ``User``.
   - ``favorite_city`` : Ville favorite de l'utilisateur (chaine de caractères, max 64).

   **Exemple de code** :

   .. code-block:: python

       from django.db import models
       from django.contrib.auth.models import User

       class Profile(models.Model):
           user = models.OneToOneField(User, on_delete=models.CASCADE)
           favorite_city = models.CharField(max_length=64, blank=True)

           def __str__(self):
               return self.user.username

Vues
----
L'application contient deux vues principales, définies dans ``views.py`` :

1. **index**

   Affiche la liste de tous les profils utilisateurs.

   **Requête** :

   - Type : GET
   - URL : ``/profiles/``

   **Description** :

   Cette vue récupère tous les objets ``Profile`` et les passe au template ``profiles/index.html``.

   .. code-block:: python

       from django.shortcuts import render
       from .models import Profile

       def index(request):
           profiles_list = Profile.objects.all()
           context = {'profiles_list': profiles_list}
           return render(request, 'profiles/index.html', context)

2. **profile**

   Affiche les détails d'un profil utilisateur spécifique.

   **Requête** :

   - Type : GET
   - URL : ``/profiles/<username>/``

   **Description** :

   Cette vue récupère un objet ``Profile`` en fonction du nom d'utilisateur et passe ses détails au template ``profiles/profile.html``.

   .. code-block:: python

       def profile(request, username):
           profile = Profile.objects.get(user__username=username)
           context = {'profile': profile}
           return render(request, 'profiles/profile.html', context)

Routes
------
Les routes de l'application sont définies dans ``urls.py`` :

.. code-block:: python

    from django.urls import path
    from . import views

    app_name = 'profiles'

    urlpatterns = [
        path('', views.index, name='index'),
        path('<str:username>/', views.profile, name='profile'),
    ]

- **Namespace** : ``profiles``, utilisé pour éviter les conflits avec d'autres applications.
  
- Routes principales :
  
  - ``path('', views.index, name='index')`` : Liste des profils.
  - ``path('<str:username>/', views.profile, name='profile')`` : Détails d'un profil.




Templates
---------
L'application utilise deux templates principaux pour afficher les profils.

1. **index.html**

   Affiche la liste de tous les profils utilisateurs avec des liens vers leurs détails.

   **Fonctionnalités principales** :

   - Liste tous les objets ``Profile`` récupérés dans la vue ``index``.
   - Affiche un message si aucun profil n'est disponible.

2. **profile.html**

   Affiche les détails d'un profil utilisateur spécifique.

   **Fonctionnalités principales** :

   - Affiche les détails du profil (nom, prénom, email, ville favorite).
   - Les données sont passées par la vue ``profile``.

Note sur les migrations
------------------------
.. note::

    Certaines migrations ont été effectuées manuellement pour repositionner correctement les tables
    associées à l'application ``lettings`` dans la base de données. Ces modifications ont permis
    d'assurer une structure cohérente et fonctionnelle. Depuis cette refactorisation, la structure 
    est stable et les tables sont correctement en place.


Tests de l'application profiles
===============================
Les tests de l'application ``profiles`` vérifient la configuration, les modèles, les URLs et les vues associées aux profils utilisateurs. Ils permettent de garantir le bon fonctionnement de cette partie de l'application.

Structure des tests
-------------------
Le dossier ``profiles/tests`` contient les tests organisés comme suit :

.. code-block:: none

    profiles/tests/
    ├── __init__.py              # Initialisation du package de tests
    ├── test_apps.py             # Tests pour la configuration de l'application
    ├── test_models.py           # Tests pour le modèle Profile
    ├── test_urls.py             # Tests pour les routes de l'application
    ├── test_views.py            # Tests pour les vues principales (index et profile)

Tests détaillés
---------------

1. **Test de la configuration de l'application**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le fichier ``test_apps.py`` vérifie que l'application ``profiles`` est correctement configurée dans Django.

.. code-block:: python

    from django.apps import apps
    from profiles.apps import ProfilesConfig

    def test_profiles_app():
        """
        Test that the ProfilesConfig is correctly registered in Django.

        Assertions:
            - Le nom de l'application est bien 'profiles'.
            - L'application est enregistrée correctement dans Django.
        """
        assert ProfilesConfig.name == 'profiles'
        assert apps.get_app_config('profiles').name == 'profiles'

2. **Tests des modèles**
~~~~~~~~~~~~~~~~~~~~~~~~
Le fichier ``test_models.py`` vérifie le fonctionnement du modèle ``Profile``.

.. code-block:: python

    from django.test import TestCase
    from profiles.models import Profile
    from django.contrib.auth.models import User

    class ProfileTestCase(TestCase):
        def test_profile_str(self):
            """
            Test the string representation of the Profile model.

            Assertions:
                - La méthode __str__ retourne le nom d'utilisateur associé au profil.
            """
            user = User.objects.create_user(username='testuser', password='12345')
            profile = Profile.objects.create(user=user, favorite_city='Paris')
            self.assertEqual(str(profile), 'testuser')

3. **Tests des URLs**
~~~~~~~~~~~~~~~~~~~~~
Le fichier ``test_urls.py`` vérifie que les routes définies dans ``profiles/urls.py`` pointent correctement vers les vues correspondantes.

.. code-block:: python

    from django.test import SimpleTestCase
    from django.urls import reverse, resolve
    from profiles.views import profile, index

    class ProfilesUrlsTest(SimpleTestCase):
        def test_index_url_resolves(self):
            """
            Test the URL resolution for the index view.

            Assertions:
                - La route 'profiles:index' est associée à la vue 'index'.
            """
            url = reverse('profiles:index')
            self.assertEqual(resolve(url).func, index)

        def test_profile_url_resolves(self):
            """
            Test the URL resolution for the profile view.

            Assertions:
                - La route 'profiles:profile' est associée à la vue 'profile'.
            """
            url = reverse('profiles:profile', args=['some-username'])
            self.assertEqual(resolve(url).func, profile)
            
4. **Tests des vues**
~~~~~~~~~~~~~~~~~~~~~
Le fichier ``test_views.py`` contient des tests pour valider les vues principales (index et profile).

**Test 1 : Vue index**

.. code-block:: python

    from django.test import TestCase
    from django.urls import reverse
    from profiles.models import Profile
    from django.contrib.auth.models import User

    class ProfilesViewsTest(TestCase):
        def setUp(self):
            self.user = User.objects.create_user(username='testuser', password='12345')
            Profile.objects.create(user=self.user, favorite_city='Alençon')

        def test_index_view(self):
            """
            Teste que la vue index retourne le bon statut et utilise le bon template.

            Assertions:
                - Le statut HTTP est 200.
                - Le template utilisé est 'profiles/index.html'.
                - Le contenu 'testuser' est présent dans la réponse.
            """
            response = self.client.get(reverse('profiles:index'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'profiles/index.html')
            self.assertContains(response, 'testuser')

**Test 2 : Vue profile**

.. code-block:: python

        def test_profile_view(self):
            """
            Teste que la vue profile retourne le bon statut et utilise le bon template.

            Assertions:
                - Le statut HTTP est 200.
                - Le template utilisé est 'profiles/profile.html'.
                - Les détails du profil (nom d'utilisateur, ville favorite) sont affichés.
            """
            response = self.client.get(reverse('profiles:profile', args=[self.user.username]))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'profiles/profile.html')
            self.assertContains(response, 'testuser')
            self.assertContains(response, 'Alençon')

**Test 3 : Gestion des erreurs**

.. code-block:: python

        from unittest.mock import patch
        import logging

        logger = logging.getLogger('profiles.views')

        def test_index_view_logs_error(self):
            """
            Test that the index view logs an error and raises an exception when an error occurs.

            Assertions:
                - Une exception est levée lors d'une erreur dans Profile.objects.all().
                - Le message d'erreur est journalisé dans les logs.
            """
            with patch('profiles.models.Profile.objects.all', side_effect=Exception("Test exception")):
                with self.assertLogs(logger, level='ERROR') as log:
                    with self.assertRaises(Exception):
                        self.client.get(reverse('profiles:index'))
                    self.assertTrue(
                        any("Error in profiles index view: Test exception" in message
                            for message in log.output)
                    )

        def test_profile_view_logs_error(self):
            """
            Test que la vue profile journalise une erreur et lève une exception en cas d'erreur.

            Assertions:
                - Une exception est levée lors d'une erreur dans Profile.objects.get().
                - Le message d'erreur est journalisé dans les logs.
            """
            with patch("profiles.models.Profile.objects.get", side_effect=Exception("Test exception")):
                with self.assertLogs(logger, level="ERROR") as log:
                    with self.assertRaises(Exception):
                        self.client.get(reverse("profiles:profile", args=["testuser"]))
                    self.assertTrue(
                        any("Error in profiles profile view: Test exception" in message
                            for message in log.output)
                    )

