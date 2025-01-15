# Utiliser une image de base légère avec Python 3.11
FROM continuumio/miniconda3:4.12.0

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY requirements.txt .

# Mettre à jour Conda et installer les dépendances nécessaires
RUN conda update -n base -c defaults conda -y && \
    conda install -n base -c conda-forge dlib -y && \
    conda install -n base -c conda-forge python=3.11 -y

# Créer un environnement spécifique à l'application
RUN conda create -n fc_recognition python=3.11 -y && \
    conda clean --all -y

# Activer l'environnement et installer les packages de requirements.txt
RUN /bin/bash -c "source activate fc_recognition && \
    pip install --no-cache-dir -r requirements.txt"

# Copier tous les fichiers de l'application dans le conteneur
COPY . .

# Exposer le port sur lequel l'application s'exécute
EXPOSE 8081

# Commande pour activer l'environnement et exécuter l'application
CMD ["/bin/bash", "-c", "source activate fc_recognition && python interface.py"]
