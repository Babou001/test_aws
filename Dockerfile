# Utiliser une image Python 3.11 officielle
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY requirements.txt .


# Installer les dépendances
RUN pip install https://pypi.python.org/packages/da/06/bd3e241c4eb0a662914b3b4875fc52dd176a9db0d4a2c915ac2ad8800e9e/dlib-19.7.0-cp36-cp36m-win_amd64.whl#md5=b7330a5b2d46420343fbed5df69e6a3f


RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le contenu de votre projet dans le conteneur
COPY . .

# Exposer le port sur lequel votre application fonctionnera (si nécessaire)
EXPOSE 8081

# Définir la commande pour exécuter l'application
CMD ["python", "interface.py"]
