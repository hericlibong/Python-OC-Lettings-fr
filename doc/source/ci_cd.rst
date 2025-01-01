Pipeline CI/CD avec Github Actions et Render
============================================
Ce fichier YAML configure un pipeline CI/CD pour le projet déployé sur Render, en utilisant Github Actions. Il automatise les étapes de test, de création d'image Docker et de déploiement.

Structure générale
------------------
Voici un aperçu des principales sections du fichier :

1. Déclencheurs
2. Jobs :
   
   - ``build`` : Exécute les tests et vérifie le style de code.
   - ``containerize`` : Construit et pousse une image Docker.
   - ``deploy`` : Déploie l'application sur Render.

Détails des sections
---------------------

**Déclencheurs**
Cette section détermine quand le pipeline doit être exécuté.

.. code-block:: yaml

    on:
      push:
        branches:
          - master
          - feature/*  # Toutes les branches dont le nom commence par "feature"
      pull_request:
        branches:
          - master  # Sur chaque pull request vers master

**Explications** :

- Le pipeline s'exécute lors de :
  
  - **Push** : Sur les branches `master` et celles correspondant au motif `feature/*`.
  - **Pull request** : Lorsqu'une PR cible la branche `master`.

---

**Job : build**
Le job ``build`` exécute les tests, le linting, et garantit que le code est propre et fonctionnel.

.. code-block:: yaml

    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
          - name: Checkout repository
            uses: actions/checkout@v3

          - name: Set up Python
            uses: actions/setup-python@v2
            with:
              python-version: '3.12'

          - name: Install dependencies
            run: |
              python -m pip install --upgrade pip
              pip install -r requirements.txt

          - name: Run Flake8
            if: github.ref == 'refs/heads/master' || github.ref == 'refs/heads/feature/*'
            run: |
              pip install flake8
              flake8 .

          - name: Run tests with pytest
            env:
              SECRET_KEY: ${{ secrets.DJANGO_SECRET_KEY }}
            run: |
              pip install pytest pytest-cov
              pytest --cov=. --cov-report=term-missing

**Explications** :

1. **Environnement** :
   
   - ``runs-on: ubuntu-latest`` : Exécute le job sur une VM Ubuntu.

2. **Étapes** :
   
   - ``actions/checkout`` : Clone le code du dépôt.
   - ``setup-python`` : Configure Python 3.12.
   - ``Install dependencies`` : Installe les dépendances listées dans `requirements.txt`.
   - ``Run Flake8`` : Vérifie le style de code (PEP8).
   - ``Run tests with pytest`` :
     - Exécute les tests avec `pytest`.
     - Génère un rapport de couverture de code.

3. **Conditions** :
   
   - Le linting et les tests ne s'exécutent que sur les branches `master` et `feature/*`.

---

**Job : containerize**

Le job ``containerize`` construit une image Docker et la pousse sur Docker Hub.

.. code-block:: yaml

    containerize:
      needs: build
      if: github.ref == 'refs/heads/master'
      runs-on: ubuntu-latest
      steps:
        - name: Checkout repository
          uses: actions/checkout@v3

        - name: Log in to Docker Hub
          env:
            DOCKER_USERNAME: ${{ secrets.DOCKER_USERNAME }}
            DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}
          run: echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin

        - name: Build and tag Docker image
          run: |
            docker build -t ${{ secrets.DOCKER_USERNAME }}/my_app:${{ github.sha }} .
            docker tag ${{ secrets.DOCKER_USERNAME }}/my_app:${{ github.sha }} ${{ secrets.DOCKER_USERNAME }}/my_app:latest

        - name: Push Docker image to Docker Hub
          run: |
            docker push ${{ secrets.DOCKER_USERNAME }}/my_app:${{ github.sha }}
            docker push ${{ secrets.DOCKER_USERNAME }}/my_app:latest

**Explications** :

1. **Enchaînement** :
   
   - ``needs: build`` : Ce job ne s'exécute que si le job ``build`` réussit.
   - ``if: github.ref == 'refs/heads/master'`` : S'exécute uniquement sur la branche `master`.

2. **Étapes** :
   
   - ``Log in to Docker Hub`` : Connecte Docker Hub en utilisant les secrets ``DOCKER_USERNAME`` et ``DOCKER_PASSWORD``.
   - ``Build and tag Docker image`` :
     - Construit une image Docker pour le projet avec le SHA du commit comme tag unique.
     - Ajoute également le tag ``latest``.
   - ``Push Docker image to Docker Hub`` : Pousse l'image sur Docker Hub.

---

**Job : deploy**

Le job ``deploy`` déclenche le déploiement sur Render en utilisant l'API de Render.

.. code-block:: yaml

    deploy:
      name: Deploy to Render
      needs: containerize
      if: github.ref == 'refs/heads/master'
      runs-on: ubuntu-latest
      steps:
        - name: Trigger Render Deploy
          run: |
            curl -X POST "https://api.render.com/v1/services/${{ secrets.RENDER_SERVICE_ID }}/deploys" \
              -H "Authorization: Bearer ${{ secrets.RENDER_API_KEY }}" \
              -H "Content-Type: application/json" \
              -d '{"image": "docker.io/'"${{ secrets.DOCKER_USERNAME }}"'/my_app:latest"}'
          env:
            RENDER_API_KEY: ${{ secrets.RENDER_API_KEY }}


**Explications** :

1. **Enchaînement** :
   
   - ``needs: containerize`` : Ce job dépend du succès du job ``containerize``.

2. **Conditions** :
   
   - ``if: github.ref == 'refs/heads/master'`` : Ce job ne s'exécute que sur la branche `master`.

3. **Étape** :
   
   - ``Trigger Render Deploy`` :
     - Utilise l'API de Render pour déployer une nouvelle version de l'application avec l'image Docker taguée ``latest``.


