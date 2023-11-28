import os
import random
import json
from flask import Flask, jsonify, redirect, render_template, request, url_for, stream_with_context, json, Response
from flask_cors import CORS
from story import *


# Define the path to your JSON data folder
json_data_folder = 'json_data'
currentGameFile = {}

app = Flask(__name__)
CORS(app)


# Function to get a random JSON file from the folder
def get_random_json_data():
    global currentGameFile
    data = {}
    files = os.listdir(json_data_folder)
    random_file = random.choice(files)
    print(random_file)
    with open(os.path.join(json_data_folder, random_file), 'r') as file:
        data = json.load(file)
    
    currentGameFile = data
    return data

@app.route('/')
def serve_random_json():
    random_data = get_random_json_data()
    response = jsonify(random_data)
    response.headers.add('Content-Type', 'application/json')
    return response

# Define a route to receive JSON data, a message, modify the JSON data, and return it
@app.route('/character_response', methods=['POST'])
def modify_json():
    global currentGameFile
    
    print("request:", request.json)
    
    try:
        # Get the JSON data, message, and synopsis from the request
        request_data = request.json
        message = request_data.get('message', '')
        characterProfile = request_data.get('characterProfile', {})
        game_synopsis = request_data.get('synopsys', '')  # Extracting synopsis from the client's request

        print("calling response function", message, characterProfile, game_synopsis)
        
        # Pass the message, characterProfile, and game_synopsis to the function
        characterResponse = createCharacterResponse(message, characterProfile, characterResponseTemplate, game_synopsis)
        
        print("response:", characterResponse)
        response = jsonify(characterResponse)
        response.headers.add('Content-Type', 'application/json')
        return response
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    # app.run(host='192.168.50.109',debug=True)
    app.run(debug=True)