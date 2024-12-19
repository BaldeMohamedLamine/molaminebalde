from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView
from .models import Profile, SocialProfile
from .forms import ProfileForm, SocialProfileForm

# Inscription
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("votre inscription a ete effectué avec succes ")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'portfolio/signup.html', {'form': form})

# Connexion
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'portfolio/login.html', {'form': form})

# Déconnexion
def user_logout(request):
    logout(request)
    return redirect('login')

# Profil utilisateur
@login_required
def profile_detail(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    social_profiles = SocialProfile.objects.filter(user=request.user)
    return render(request, 'portfolio/profile_detail.html', {'profile': profile, 'social_profiles': social_profiles})

# Mise à jour du profil
@login_required
def update_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'portfolio/update_profile.html', {'form': form})

# Mise à jour des profils sociaux
@login_required
def update_social_profiles(request):
    if request.method == 'POST':
        formset = SocialProfileForm(request.POST, queryset=SocialProfile.objects.filter(user=request.user))
        if formset.is_valid():
            formset.save()
            return redirect('profile')
    else:
        formset = SocialProfileForm(queryset=SocialProfile.objects.filter(user=request.user))
    return render(request, 'portfolio/update_social_profiles.html', {'formset': formset})
