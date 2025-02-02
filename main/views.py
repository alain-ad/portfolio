from django.shortcuts import render

# Create your views here.
#ici on a défini une fonction home qui prend en paramètre request et qui retourne un objet render et on peut les changer en fonction de nos besoins
def home(request):
    context = {
        # Header section
        'name': "Alain ANDRIANALIJAONA",
        'title': "Full-Stack Developer",
        'tagline': "Building modern and scalable web applications",
        'cta_text': "Contact Me",
        'cta_link': "#contact",

        # About section
        'about_description': (
            "I am a passionate developer with experience in creating modern, scalable "
            "applications using cutting-edge technologies."
        ),
        'personal_info': {
            'bio': 'Développeur web passionné avec 2 ans.',
            'image': 'path/to/profile/image.jpg',  # Chemin vers l'image de profil si vous en avez une
        },
        'skills': {
            'frontend': [
                {'name': 'HTML', 'level': 95},
                {'name': 'CSS', 'level': 90},
                {'name': 'JavaScript', 'level': 85},
                {'name': 'React.js', 'level': 70},
            ],
            'backend': [
                {'name': 'Python/Django', 'level': 90},
                {'name': 'Node.js', 'level': 85},
                {'name': 'API REST', 'level': 85},
            ],
            'tools': [
                {'name': 'Git', 'level': 80},
                {'name': 'PostgreSQL', 'level': 75},
            ]
        },

        # Projects section
        'projects': [
            {
            'title': 'Color game',
            'description': 'A fun and interactive color guessing game.',
            'technologies': ['HTML', 'CSS', 'JavaScript'],
            'link': 'https://github.com/alain-ad/lesson.git',
            'image': 'static/images/coloGame.jpg',
            },
            {
            'title': 'Portfolio',
            'description': 'A personal portfolio website to showcase my projects and skills.',
            'technologies': ['HTML', 'CSS', 'JavaScript', 'Django'],
            'link': 'https://github.com/alain-ad/portfolio.git',
            'image': 'static/images/portimage.jpg',
            },
        ],

        # Experience section
        'experiences': [
{
        'title': 'Stagiaire Développeur Web',
        'company': 'ESMIA, Tana',
        'period': '2023',
        'description': 'Mise en réseau et développement de site SIRH, assistant de ressources humaines.',
        'technologies': ['HTML', 'CSS', 'JavaScript', 'PHP']
    },
    {
        'title': 'Stagiaire Développeur Web',
        'company': 'MESUPRES, Tsimbazaza',
        'period': '2024',
        'description': 'Développement d’un système de saisie automatique pour la gestion des employés, incluant la création de fonctionnalités web. Collaboration avec les équipes pour définir les besoins du projet et validation des outils développés. Documentation des processus et formation des collègues sur l\'utilisation des nouvelles solutions.',
        'technologies': ['JavaScript', 'Python', 'MySQL', 'Web Development']
    }
        ],

        # Education section
        'education': [
            {
                'degree': 'Licens en Informatique',
                'school': 'École Supérieur de Management et de l\' informatique appliqué',
                'year': '2022',
                'description': 'Spécialisation en développement web et applications mobiles'
            },
        ],

        # Languages section
        'languages': [
            {'name': 'Malagasy', 'level': 'Langue maternelle'},
            {'name': 'Français', 'level': 'Courant'},
            {'name': 'Anglais', 'level': 'Intermédiaire'},
        ],

        # Contact section
        'contact_email': "alainandrianalijaona@gmail.com",
        'contact_phone': "+261 34 96 580 10",
        'social_links': {
            'LinkedIn': "https://www.linkedin.com/in/rojo-alain-andrianalijaona-9818a0233/",
            'GitHub': "https://github.com/alain-ad",
        },
    }
    
    return render(request, 'home.html', context)
