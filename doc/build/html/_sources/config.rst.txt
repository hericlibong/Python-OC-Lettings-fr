Configuration Globale
=====================

Ce document décrit les fichiers de configuration globaux du projet.

Fichiers
--------

- **`settings.py`** :
  - Contient toutes les configurations principales du projet, telles que :
    - **Sentry** : Gestion des erreurs via logs.
    - **Bases de données** : Configuration de PostgreSQL.
    - **Applications Django** : Liste des `INSTALLED_APPS`.

- **`urls.py`** :
  - Centralise les URL de toutes les applications.
  - Définit les namespaces pour les routes principales.

Exemple : 
::

from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('oc_lettings_site.urls', namespace='oc_lettings_site')),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),  
]

