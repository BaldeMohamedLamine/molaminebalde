from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.conf import settings

# Gestionnaire d'utilisateurs personnalisé
class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, phone, password=None):
        if not email:
            raise ValueError('L\'adresse email est obligatoire')
        if not username:
            username = "Utilisateur"

        email = self.normalize_email(email)
        user = self.model(
            email=email, 
            username=username, 
            first_name=first_name, 
            last_name=last_name, 
            phone=phone
        )
        user.set_password(password)  
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, phone, password=None):
        user = self.create_user(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=40, default='pas de Nom', blank=True, null=True)
    aprpos = models.TextField()
    birthday = models.CharField(max_length=20)
    degree = models.CharField(max_length=20)
    address = models.CharField(max_length=255, default='Unknown Address')
    freelance = models.BooleanField(default=True)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=20, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'phone']

    objects = UserManager()

    def __str__(self):
        return self.username if self.username else self.email

    # Permissions
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile/', blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    contact_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class SocialProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    platform = models.CharField(max_length=100)  
    url = models.URLField()

    def __str__(self):
        return f'{self.platform} de {self.user.username}'
