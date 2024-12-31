Introduction
============

Bienvenue dans la documentation de **Python OC Lettings**, une application web développée en Django qui vise à simplifier la gestion des profils utilisateurs et des biens immobiliers.

Objectifs principaux
---------------------
L'objectif de ce projet est de fournir une plateforme où les utilisateurs peuvent :

- **Créer, consulter et modifier des profils personnels.**
- **Ajouter et gérer des annonces de locations immobilières.**

Fonctionnalités principales
----------------------------
Gestion des profils utilisateurs :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Création, modification et affichage des profils.
- Association des profils aux biens immobiliers.

Gestion des biens immobiliers :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Ajout et modification des annonces.
- Affichage des détails de chaque bien immobilier.

Structure de l'application
---------------------------
L'application est divisée en plusieurs modules ou **applications Django** :

- ``oc_lettings_site`` : Gère uniquement la page d'accueil du projet, sans modèles associés.
- ``lettings`` : Gère les biens immobiliers et leurs informations.
- ``profiles`` : Gère les informations des utilisateurs (profils).

Technologies utilisées
-----------------------
Ce projet utilise les technologies et outils suivants :

- **Framework Django** (v5.1.4) : Pour la gestion back-end.
- **Python** : Développé avec la version 3.12, compatible avec 3.10 minimum.
- **Sentry** : Intégré pour le suivi des erreurs et la journalisation.
- **Render** : Déploiement de l'application grâce à un pipeline CI/CD robuste.
- **Read the Docs** : Utilisé pour cette documentation.
- **GitHub** : Versionnement et gestion du code source.

Nous vous invitons à explorer les différentes sections de cette documentation pour mieux comprendre le fonctionnement et la structure de cette application. Bonne lecture !
