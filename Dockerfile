# Utiliser une image Python 3.11 officielle
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY requirements.txt .


# Installer les dépendances
RUN apt install git
RUN apt install cmake
RUN ./dlib_package.sh

RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le contenu de votre projet dans le conteneur
COPY . .

# Exposer le port sur lequel votre application fonctionnera (si nécessaire)
EXPOSE 8081

# Définir la commande pour exécuter l'application
CMD ["python", "interface.py"]
