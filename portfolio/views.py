from django.shortcuts import render, redirect
from .models import Project, Skill,Experience,ExperienceStats,Service,Testimonial,Certification
from .models import Article
from .models import ContactMessage
from accounts.models import Profile, SocialProfile
from django.http import HttpRequest
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib import messages

def home(request):
    projects = Project.objects.all()  
    skills = Skill.objects.all()  
    profile = Profile.objects.first() 
    experiences = Experience.objects.all()  
    social_profiles = SocialProfile.objects.all()
    stats = ExperienceStats.objects.first()
    services = Service.objects.all() 
    testimonials = Testimonial.objects.all() 
    article = Article.objects.all().order_by('-created_at'),
    certification = Certification.objects.all().order_by('-date_obtained')
    context = {
        'projects': projects,
        'skills': skills,
        'profile': profile,
        'experiences': experiences,
        'social_profiles': social_profiles,
        'stats': stats,
        'services': services,
        'testimonials': testimonials,
        'articles': article,
        'certification': certification
    }
    return render(request, 'portfolio/index.html', context)

def contact_view(request):
    if request.method == 'POST':
        # Récupération des données du formulaire
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Sauvegarder le message dans la base de données
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Construire le sujet et le corps de l'e-mail
        email_subject = f"Message de {name}"
        body = f"""
        Nom: {name}
        Email: {email}
        Sujet: {subject}
        Message: {message}
        """

        # Envoi de l'e-mail
        send_mail(
            email_subject,
            body,
            email,  # Email de l'envoyeur
            ['baldelenz@gmail.com'],  # Adresse e-mail destinataire
        )

        # Ajouter un message de succès
        messages.success(request, 'Votre message a été envoyé avec succès !')

        # Rediriger vers une page de confirmation après avoir traité le formulaire
        return redirect(reverse('confirmation') + f'?name={name}&email={email}')
    
    else:
        return render(request, 'index.html')

def confirmation_view(request: HttpRequest):
    name = request.GET.get('name')
    email = request.GET.get('email')

    context = {'name': name, 'email': email}
    return render(request, 'confirmation.html', context)


