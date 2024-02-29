function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    if (userInput.trim() === '') return;

    var chatBox = document.getElementById("chat-box");
    // var userMessage = '<div>' + userInput + '</div>';
    // var userMessagewithYou = '<div class="chat-message user-message"><div class="who">You</div>' + userMessage + '</div>';
    var userMessage = '<div class="chat-message user-message"><div class="who">You</div>' + userInput + '</div>';
    chatBox.innerHTML += userMessage;

    const data = { texte: userInput };

    fetch('http://localhost:5000/predict', {
        method: 'POST',
        // mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.tag)
        console.log(data.confidence_score)
        // Afficher la réponse
        var botMessage = '<div class="chat-message bot-message"><div class="who">Joker</div>'+ data.response +'</div>';
        chatBox.innerHTML += botMessage;
        chatBox.scrollTop = chatBox.scrollHeight;

        // Clear the user input field
        document.getElementById("user-input").value = '';
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById("user-input").value = '';
    });
    
}
    // // For demonstration purposes, let's assume the bot's response.
    // // var botMessage = '<div class="chat-message bot-message"><div class="who">Joker</div>Je suis un chatbot basique. Excusez-moi, je ne peux pas répondre à cela pour le moment.</div>';
    // var botMessage = '<div class="chat-message bot-message"><div class="who">Joker</div>'+ outputData +'</div>';
    // chatBox.innerHTML += botMessage;

    

// Fonction pour envoyer une requête POST à l'API Flask
// function sendRequest() {
//     const data = { texte: "Votre texte à prédire ici" };

//     fetch('http://localhost:5000/predict', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(data),
//     })
//     .then(response => response.json())
//     .then(data => {
//         // Afficher la réponse, le score de confiance et le tag associé
//         document.getElementById('response').innerHTML = `
//             <p>Réponse : ${data.response}</p>
//             <p>Score de confiance : ${data.confidence_score}</p>
//             <p>Tag associé : ${data.tag}</p>
//         `;
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
// }

// // Appeler la fonction sendRequest au chargement de la page
// document.addEventListener('DOMContentLoaded', function() {
//     sendRequest();
// });