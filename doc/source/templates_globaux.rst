Templates globaux
=================

Le projet inclut des templates globaux pour définir la structure de base et gérer les erreurs HTTP. Ces fichiers assurent une cohérence visuelle et une meilleure expérience utilisateur.

Template base.html
------------------
Le fichier ``base.html`` sert de modèle principal pour tous les templates du projet. Il définit la structure HTML de base, y compris les en-têtes, le pied de page, et les inclusions CSS/JS.

**Points clés** :

- **Navbar** : Inclut des liens vers les sections principales (profils, locations, etc.).
- **Blocs modifiables** :
  
  - ``{% block title %}`` : Définit le titre de la page.
  - ``{% block content %}`` : Contenu principal de chaque page.

**Extrait de code** :

.. code-block:: html

    <html lang="en">
        <head>
            <title>{% block title %}{% endblock title %}</title>
            <link href="{% static 'css/styles.css' %}" rel="stylesheet" />
        </head>
        <body>
            <nav class="navbar">
                <a href="{% url 'oc_lettings_site:index' %}">Home</a>
                <a href="{% url 'profiles:index' %}">Profiles</a>
                <a href="{% url 'lettings:index' %}">Lettings</a>
            </nav>
            {% block content %}{% endblock %}
            <footer>
                <p>Copyright &copy; 2023 Orange County Lettings</p>
            </footer>
        </body>
    </html>

Templates d'erreurs HTTP
------------------------
Les templates ``404.html`` et ``500.html`` personnalisent les pages d'erreurs HTTP pour offrir une meilleure expérience utilisateur.

``404.html``
Affiche un message lorsque la page demandée n'existe pas.

**Extrait de code** :

.. code-block:: html

    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
    <a href="{% url 'oc_lettings_site:index' %}">Return to Home</a>

``500.html``
Affiche un message en cas d'erreur interne au serveur.

**Extrait de code** :

.. code-block:: html

    <h1>500 - Server Error</h1>
    <p>Oops! Something went wrong on our side. Please try again later.</p>
    <a href="{% url 'oc_lettings_site:index' %}">Return to Home</a>

---

Commandes pour tester les pages d'erreurs
-----------------------------------------
Pour tester ces pages localement, ajoutez temporairement ces routes dans ``config/urls.py`` :

.. code-block:: python

    from django.views.defaults import page_not_found, server_error

    urlpatterns += [
        path('404/', lambda request: page_not_found(request, exception=None)),
        path('500/', lambda request: server_error(request)),
    ]
