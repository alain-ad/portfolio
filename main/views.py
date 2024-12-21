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
    return render(request, 'about.html')

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
