Dockerfile : Explications
==========================
Ce fichier Dockerfile configure l'image Docker pour exécuter l'application Django. Il est structuré en plusieurs étapes pour installer les dépendances, préparer l'environnement et lancer l'application.

Étapes détaillées
-----------------

1. **Utiliser une image de base**

   .. code-block:: dockerfile

       FROM python:3.12-slim

   **Explications** :
   
   - L'image de base utilisée est ``python:3.12-slim``.
   - Elle contient une version minimale de Python 3.12, réduisant la taille de l'image tout en fournissant un environnement Python complet.

2. **Définir le répertoire de travail**

   .. code-block:: dockerfile

       WORKDIR /app

   **Explications** :

   - Définit le répertoire de travail dans le conteneur.
   - Toutes les commandes suivantes (comme ``COPY`` ou ``RUN``) seront exécutées dans ce répertoire.

3. **Copier les fichiers dans le conteneur**

   .. code-block:: dockerfile

       COPY . /app

   **Explications** :

   - Copie tout le contenu du répertoire courant de l’hôte dans le répertoire ``/app`` du conteneur.
   - Cela inclut le code source, le fichier ``requirements.txt``, etc.

4. **Installer les dépendances**

   .. code-block:: dockerfile

       RUN pip install --no-cache-dir --upgrade pip && \
           pip install --no-cache-dir -r requirements.txt

   **Explications** :

   - Met à jour ``pip`` à la dernière version.
   - Installe les packages nécessaires listés dans ``requirements.txt``.
   - L’option ``--no-cache-dir`` évite de stocker les fichiers de cache, ce qui réduit la taille de l’image.

5. **Définir les variables d'environnement**

   .. code-block:: dockerfile

       ENV SECRET_KEY="a_secure_default_key_for_docker"

   **Explications** :

   - Définit une variable d'environnement pour Django, ici une clé secrète par défaut (non sécurisée).
   - Cette valeur peut être surchargée lors de l'exécution du conteneur avec l'option ``-e``.

6. **Collecter les fichiers statiques**

   .. code-block:: dockerfile

       RUN python manage.py collectstatic --noinput

   **Explications** :

   - Exécute la commande ``collectstatic`` pour préparer les fichiers statiques nécessaires à la production.
   - L’option ``--noinput`` évite les invites interactives pendant l’exécution.

7. **Exposer le port**

   .. code-block:: dockerfile

       EXPOSE 8000

   **Explications** :

   - Indique que le conteneur écoutera sur le port ``8000``.
   - Ce port doit correspondre au port configuré pour le serveur Django.

8. **Commande par défaut**

   .. code-block:: dockerfile

       CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

   **Explications** :

   - Définit la commande par défaut pour démarrer l’application.
   - Ici, le serveur Django démarre en écoutant toutes les interfaces réseau sur le port 8000.

---

Créer une image Docker manuellement
-----------------------------------
Pour créer une image Docker à partir de ce fichier Dockerfile, exécutez la commande suivante :

.. code-block:: bash

    docker build -t nom_de_l_image:tag .

**Exemple** :

.. code-block:: bash

    docker build -t my_app:latest .

- ``-t my_app:latest`` : Définit le nom (``my_app``) et le tag (``latest``) de l’image.
- ``.`` : Indique que le Dockerfile se trouve dans le répertoire courant.



