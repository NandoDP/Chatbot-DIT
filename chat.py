from sklearn.naive_bayes import MultinomialNB
from utils import bag_of_words, tokenize
import joblib
import random
import json



# Charger le modèle Naive Bayes pré-entrainé
model = joblib.load('modele.pkl')
words = joblib.load('words.pkl')

with open('intents.json', 'r', encoding='utf-8') as json_data:
    intents = json.load(json_data)

# Obtenir la liste des tags
tags = sorted([intent['tag'] for intent in intents['intentions']])

def choice(tag):
    for intent in intents['intentions']:
            if tag == intent["tag"]:
                return random.choice(intent['reponses'])

def get_reponse(texte):
    # Vectoriser le texte 
    sentence = tokenize(texte)
    texte_vectorise = bag_of_words(sentence, words)

    # Faire une prédiction avec le modèle Naive Bayes
    prediction = model.predict([texte_vectorise])[0]

    # Obtenir le tag associé a l'intention
    tag = tags[prediction]

    # Obtenir une reponse
    reponse = choice(tag)

    # Obtenir le score de confiance pour la prédiction
    score = model.predict_proba([texte_vectorise]).max()

    return reponse, tag,  score