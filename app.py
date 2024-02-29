from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from chat import get_reponse

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def index_get():
    return render_template('test.html')

# Définir une route pour la prédiction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Obtenir les données JSON de la requête POST
    texte = data['texte']  # Extraire le texte à prédire

    # Obtenir une reponse
    reponse, tag, score = get_reponse(texte)

    # Retourner la réponse, le score de confiance et le tag associé à l'intention détectée
    return jsonify({'response': reponse, 'tag': tag, 'confidence_score': score})

if __name__ == '__main__':
    app.run(debug=True)  # Exécuter l'application Flask en mode debug



# from chat import get_reponse

# quit = False

# print("(q ou Q pour quitter)")
# while quit == False:
#     texte = input("\nVous : ")

#     if texte == 'q' or texte == 'Q':
#         quit = True
#         break

#     reponse, tag, score = get_reponse(texte)

#     print(f"\nBot: {reponse} (tag: {tag}, score: {score})")