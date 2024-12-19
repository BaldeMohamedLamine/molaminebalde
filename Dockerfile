FROM python:3.12-bullseye

# Ne pas écrire de fichiers .pyc
ENV PYTHONDONTWRITEBYTECODE=1

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système nécessaires pour mysqlclient
RUN apt-get update && apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev build-essential pkg-config && \
    rm -rf /var/lib/apt/lists/*

# Mettre à jour pip
RUN pip install --upgrade pip

# Copier le fichier des dépendances
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du projet
COPY . .

# Exposer le port 8080
EXPOSE 8000

# Définir la commande pour démarrer l'application avec Uvicorn
CMD ["uvicorn", "Blog.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
