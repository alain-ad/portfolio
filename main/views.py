from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    return render(request, 'main/projects.html')

def contact(request):
    return render(request, 'main/contact.html')

# from .models import Project  # Import du modèle Project
# Si vous utilisez une base de données (par exemple, pour stocker des informations sur vos projets), ces fonctions de vues jouent un rôle plus actif. Elles :
# def projects(request):
#     # Récupérer tous les projets depuis la base de données
#     project_list = Project.objects.all()
    
#     # Transmettre les données à 'projects.html' via un contexte
#     return render(request, 'main/projects.html', {'projects': project_list})
