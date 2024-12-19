from .settings import *
import dj_database_url
import environ
import os

env = environ.Env(
    # définir le casting, valeur par défaut
    DEBUG=(bool, False)
)
# Définir le répertoire de base du proje
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Prendre les variables d'environnement du fichier .env
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')
    
ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(',') 
DATABASES = {'default':dj_database_url.config(conn_health_checks=True)}

# Configuration des paramètres AWS S3
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = "eu-central-1"
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

# Static et Media files
STATICFILES_LOCATION = "movie/static"
MEDIAFILES_LOCATION = "movie/media"

# URLs pour les fichiers statiques et médias
STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/"
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/"

# Configuration du cache pour les fichiers statiques
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",  # Cache pour 1 jour
}

# Empêcher l'écrasement des fichiers existants
AWS_S3_FILE_OVERWRITE = False

# Configuration des backends de stockage
STORAGES = {
    "default": {
        "BACKEND": "movie.storages.MediaStorage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
        "OPTIONS": {
            "location": STATICFILES_LOCATION,
        },
    },
}

# collectstatic configuration
STATICFILES_STORAGE = "storages.backends.s3boto3.S3StaticStorage"