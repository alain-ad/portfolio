# Portfolio Static

Ce projet est un portfolio statique sans base de données. Il est conçu pour être simple, rapide et facile à déployer.

## Table des matières
1. [Introduction](#introduction)
2. [Fonctionnalités](#fonctionnalités)
3. [Installation](#installation)
4. [Utilisation](#utilisation)
5. [Structure du projet](#structure-du-projet)
6. [Contribuer](#contribuer)
7. [Licence](#licence)

## Introduction
Ce portfolio statique permet de présenter vos projets, compétences et expériences de manière élégante et professionnelle. Il est entièrement statique, ce qui signifie qu'il n'y a pas de base de données ou de backend à gérer.

## Fonctionnalités
- Présentation des projets
- section about
- Section compétences
- Section expériences
- Section contacts
- Design responsive
- Facile à personnaliser

## Installation
Pour installer ce projet, suivez les étapes ci-dessous :

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/alain-ad/portfolio.git
    ```
2. Accédez au répertoire du projet :
    ```bash
    cd portfolio
    ```
3. Installez les dépendances nécessaires :
    ```bash
    pip install -r requirements.txt
    ```
4. Démarrez le serveur de développement :
    ```bash
    python manage.py runserver
    ```

## Utilisation
Pour personnaliser le portfolio, modifiez les fichiers , views, HTML et CSS selon vos besoins. Vous pouvez ajouter vos propres projets, compétences et expériences en éditant les sections correspondantes dans le fichier `main/views.py`

## Structure du projet
Voici la structure des fichiers et des dossiers du projet :

```
portfolio/
├── manage.py
├── portfolio/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── main/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── templates/
│   │   └── app/
│   │       └── home.html
│   ├── static/
│       ├── css/
│       │   └── styles.css
│       ├── js/
│       │   └── scripts.js
│       ├── images/
│               └── (vos images ici)
└── README.md
```

## Contribuer
Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet, veuillez suivre ces étapes :

1. Forkez le dépôt.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/nouvelle-fonctionnalité`).
3. Commitez vos modifications (`git commit -am 'Ajout d'une nouvelle fonctionnalité'`).
4. Poussez votre branche (`git push origin feature/nouvelle-fonctionnalité`).
5. Ouvrez une Pull Request.


## Collaboration

Ce projet a été développé en collaboration avec une autre personne. Voici comment nous avons géré la collaboration :

1. **Répartition des tâches** : Nous avons divisé les tâches en fonction de nos compétences respectives. Par exemple, une personne s'est concentrée sur le design et le frontend, tandis que l'autre s'est occupée de l'intégration avec Django.

2. **Utilisation de Git** : Nous avons utilisé Git pour le contrôle de version et GitHub pour héberger le dépôt. 


4. **Revue de code** : Chaque Pull Request a été revue par l'autre contributeur pour s'assurer de la qualité du code et de la conformité aux normes du projet.

## Django

Bien que ce projet soit principalement statique, nous avons utilisé Django pour certaines fonctionnalités dynamiques. Voici comment nous avons intégré Django :

1. **Installation de Django** : Pour installer Django, exécutez la commande suivante :
    ```bash
    pip install django
    ```

2. **Configuration du projet Django** : Nous avons créé un projet Django et configuré les paramètres nécessaires dans le fichier `settings.py`.

3. **Création d'applications Django** : Nous avons créé des applications Django pour gérer différentes parties du portfolio, comme les projets, les compétences et les expériences.

4. **vues** : Nous avons créé des vues pour afficher ces informations dans le portfolio.

5. **Templates** : Nous avons utilisé le système de templates de Django pour générer les pages HTML du portfolio.

Pour plus de détails sur l'utilisation de Django, consultez la documentation officielle de Django : [https://docs.djangoproject.com/](https://docs.djangoproject.com/).