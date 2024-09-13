import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

EXTERNAL_API_URL = 'https://widipe.com/gemini'

IDENTITY_RESPONSES = {
    "who are you": "I am KORA, developed by Suleiman for the purpose of education and friendship.",
    "what is your name": "My name is KORA.",
    "who created you": "I was created by Suleiman.",
    "why were you created": "I was created to help with education, friendship, and sharing knowledge.",
    "what do you do": "I assist with answering questions and providing information.",
    "what is your purpose": "My purpose is to educate and provide assistance in learning and understanding topics.",
    "where are you from": "I am a digital assistant, so I don't have a physical location.",
    "how can you help me": "I can help by answering questions, providing explanations, and engaging in friendly conversations.",
    "what technologies were used to create you": "I was built using Python and Flask, with backend support Developed by SULEIMAN .",
    "what is your model": "I am KORA specifically for education Developed By SULEIMAN >SMAN V1.0<, with a focus on assisting learners."
}

@app.route('/ask', methods=['GET'])
def ask():
    question = request.args.get('question', '').lower()

    if question:
        for key, response in IDENTITY_RESPONSES.items():
            if key in question:
                return jsonify({"response": response})

        try:
            external_response = requests.get(EXTERNAL_API_URL, params={'text': question})

            if external_response.status_code == 200:
                try:
                    ai_response = external_response.json()
                    return jsonify({
                        "response": ai_response.get('result', "No result found."),
                        "status": ai_response.get('status', False),
                        "creator": ai_response.get('creator', "Unknown")
                    })
                except ValueError:
                    return jsonify({"error": "AI API returned a non-JSON response."}), 500
            else:
                return jsonify({"error": "Failed to get a response from the AI API."}), 500

        except Exception as e:
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    else:
        return jsonify({"error": "Please provide a question."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
