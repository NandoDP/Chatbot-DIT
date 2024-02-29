FROM python:3.8-slim

# Copier les fichiers de l'application Flask dans le conteneur
COPY . /app
WORKDIR /app

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Commande pour exécuter l'application Flask lorsque le conteneur démarre
CMD ["python", "app.py"]
