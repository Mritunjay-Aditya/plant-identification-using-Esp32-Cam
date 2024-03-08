from flask import Flask, request, jsonify
import os
import requests
import json
from pprint import pprint

app = Flask(__name__)
API_KEY = "2b10sI4pUqsrJchBzXFo9W0Ie"  # Set your API_KEY here
PROJECT = "all"  # try "weurope" or "canada"
api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def save_image(image_data, filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    with open(file_path, 'wb') as f:
        f.write(image_data)
    return file_path

@app.route("/", methods=["POST"])
def identify_plant():
    # Get image data from request
    image_data = request.data
    
    # Save the image
    image_filename = 'image.jpg'  # Change this to the appropriate filename if needed
    image_path = save_image(image_data, image_filename)
    
    # Perform plant identification here
    files = {'images': open(image_path, 'rb')}
    response = requests.post(api_endpoint, files=files)
    
    if response.status_code == 200:
        json_result = response.json()
        pprint(json_result)  # Print the response for debugging
        # Extract the plant type from the response and return it
        # Assuming the response structure, you should adjust this part based on the actual response
        plant_type = json_result['results'][0]['species']['scientificNameWithoutAuthor']
        return jsonify({"plantType": plant_type})
    else:
        return jsonify({"error": "Failed to identify plant"}), 500

if __name__ == "__main__":
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(host="0.0.0.0", port=33)
