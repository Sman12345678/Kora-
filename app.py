import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Base URL of the external API
EXTERNAL_API_URL = 'https://widipe.com/gpt4?text= {}'

# Define a dictionary to store identity-related questions and their responses
IDENTITY_RESPONSES = {
    "who are you": "I am KORA, developed by Suleiman for the purpose of education and friendship.",
    "what is your name": "My name is KORA.",
    "who created you": "I was created by Suleiman.",
    "why were you created": "I was created to help with education, friendship, and sharing knowledge.",
    "what do you do": "I assist with answering questions and providing information.",
    "what is your purpose": "My purpose is to educate and provide assistance in learning and understanding topics.",
    "where are you from": "I am a digital assistant, so I don't have a physical location.",
    "how can you help me": "I can help by answering questions, providing explanations, and engaging in friendly conversations.",
    "what technologies were used to create you": "I was built using Python and Flask, with backend support By my Lord Suleiman .",
    "what makes you different from other bots": "I am designed specifically for education and friendship, with a focus on assisting learners."
}

@app.route('/ask', methods=['GET'])
def ask():
    # Get the question from the query parameters
    question = request.args.get('question', '').lower()

    if question:
        # Check if the question matches any predefined identity-related questions
        for key, response in IDENTITY_RESPONSES.items():
            if key in question:
                return jsonify({
                    "response": response
                })

        # If it's not an identity-related question, forward it to the external API
        try:
            # Sending request to the external API
            external_response = requests.get(EXTERNAL_API_URL, params={'question': question})

            # Checking if the request to the external API was successful
            if external_response.status_code == 200:
                # Return the response from the external API
                return jsonify({
                    "response": external_response.json()
                })
            else:
                return jsonify({
                    "error": "Failed to get a response from the external API."
                }), 500

        except Exception as e:
            return jsonify({
                "error": f"An error occurred: {str(e)}"
            }), 500
    else:
        return jsonify({"error": "Please provide a question."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
