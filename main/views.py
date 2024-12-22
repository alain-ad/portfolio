from django.shortcuts import render

# Create your views here.
def home(request):
    context= {
         # Header section
        'name': "Alain ANDRIANALIJAONA",  # Remplacez par votre nom
        'title': "Full-Stack Developer",  # Titre professionnel
        'tagline': "Building modern and scalable web applications",  # Phrase d'accroche
        'cta_text': "Contact Me",  # Texte du bouton CTA
        'cta_link': "#contact",  # Lien vers la section contact

        # About section
        'about_description': (
            "I am a passionate developer with experience in creating modern, scalable "
            "applications using cutting-edge technologies."
        ),
        'skills': ["HTML", "CSS", "JavaScript", "Python", "Django", "React"],  # Vos compétences
        'technologies': ["PostgreSQL", "Git"],  # Vos technologies

        # Contact section
        'contact_email': "alainandrianalijaona@gmail.com",
        'contact_phone': "+261 34 96 580 10",
        'social_links': {
            'LinkedIn': "https://www.linkedin.com/in/rojo-alain-andrianalijaona-9818a0233/",
            'GitHub': "https://github.com/alain-ad",
        },
    }
    return render(request,'home.html', context)

def about(request):
    context = {
        # Informations personnelles
        'personal_info': {
            'name': 'Alain ANDRIANALIJAONA',
            'title': 'Développeur Full Stack',
            'bio': 'Développeur web passionné avec 52 ans.',
            'image': 'path/to/profile/image.jpg',  # Chemin vers l'image de profil
        },
        
        # Compétences techniques
        'skills': {
            'frontend': [
                {'name': 'React.js', 'level': 70},
                # {'name': 'Vue.js', 'level': 85},
                # {'name': 'HTML5/CSS3', 'level': 95},
                # {'name': 'JavaScript (ES6+)', 'level': 90},
            ],
            'backend': [
                {'name': 'Node.js', 'level': 85},
                {'name': 'Python/Django', 'level': 90},
                # {'name': 'PHP/Laravel', 'level': 80},
                {'name': 'API REST', 'level': 85},
            ],
            'tools': [
                {'name': 'Git', 'level': 80},
                # {'name': 'Docker', 'level': 85},
                # {'name': 'AWS', 'level': 80},
                # {'name': 'CI/CD', 'level': 85},
            ]
        },

        # Expérience professionnelle
        'experiences': [
            # {
            #     'title': 'Développeur Full Stack Senior',
            #     'company': 'Entreprise XYZ',
            #     'period': '2020 - Présent',
            #     'description': 'Développement d\'applications web complexes, direction d\'équipe, architecture de solutions.',
            #     'technologies': ['React', 'Node.js', 'AWS']
            # },
            {
                'title': 'Développeur Front-end',
                'company': 'Startup ABC',
                'period': '2018 - 2020',
                'description': 'Création d\'interfaces utilisateur réactives, optimisation des performances.',
                'technologies': ['Vue.js', 'JavaScript', 'CSS3']
            }
        ],

        # Formation
        'education': [
            {
                'degree': 'Licens en Informatique',
                'school': 'École Supérieur de Management et de l\' informatique appliqué',
                'year': '2022',
                'description': 'Spécialisation en développement web et applications mobiles'
            },
            # {
            #     'degree': 'Licence en Informatique',
            #     'school': 'Université de Sciences',
            #     'year': '2016',
            #     'description': 'Formation générale en informatique'
            # }
        ],

        # Langues
        'languages': [
            {'name': 'Malagasy', 'level': 'Langue maternelle'},
            {'name': 'Français', 'level': 'Courant'},
            {'name': 'Anglais', 'level': 'Intermédiaire'},
        ]

        # Certifications
        # 'certifications': [
        #     {
        #         'name': 'AWS Certified Developer',
        #         'issuer': 'Amazon Web Services',
        #         'year': '2023'
        #     },
        #     {
        #         'name': 'Professional Scrum Master I',
        #         'issuer': 'Scrum.org',
        #         'year': '2022'
        #     }
        # ]
    }
    
    return render(request, 'about.html', context)

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')

# from .models import Project  # Import du modèle Project
# Si vous utilisez une base de données (par exemple, pour stocker des informations sur vos projets), ces fonctions de vues jouent un rôle plus actif. Elles :
# def projects(request):
#     # Récupérer tous les projets depuis la base de données
#     project_list = Project.objects.all()
    
#     # Transmettre les données à 'projects.html' via un contexte
#     return render(request, 'main/projects.html', {'projects': project_list})
