from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Endpoint to fetch a response from widipe.com/gpt4
@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json.get('question')

    # Check if the question is about the identity of the API
    if 'who are you' in user_question.lower() or 'your name' in user_question.lower():
        identity_response = {
            "name": "KORA",
            "description": "I am KORA, a sophisticated conversational AI developed by SULEIMAN. I exist for the purpose of education and friendship, and I'm here to assist with any queries you might have."
        }
        return jsonify(identity_response)

    # Otherwise, send the question to widipe.com/gpt4
    try:
        external_api_url = 'https://widipe.com/gpt4'
        external_response = requests.post(external_api_url, json={"question": user_question})

        if external_response.status_code == 200:
            return jsonify({"response": external_response.json()})
        else:
            return jsonify({"error": "Failed to fetch response from widipe.com/gpt4"}), external_response.status_code
    except Exception as e:
        return jsonify({"error": str(e)})

# Run the API
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
