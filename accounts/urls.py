from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('signup:', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile_detail, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('profile/social/', views.update_social_profiles, name='update_social_profiles'),
]
