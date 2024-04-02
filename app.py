from flask import Flask, request, jsonify,redirect,url_for,render_template,send_from_directory
import os
import requests
import json
from pprint import pprint
plant_type = "rose"


app = Flask(__name__)
API_KEY = "************"  # Set your API_KEY here
PROJECT = "all"  # try "weurope" or "canada"
api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"
UPLOAD_FOLDER = 'templates'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
pprint(plant_type)


def save_image(image_data, filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    with open(file_path, 'wb') as f:
        f.write(image_data)
    return file_path

@app.route("/identify", methods=["POST"])
def identify_plant():
    # Get image data from request
    global plant_type
    image_data = request.data
    
    # Save the image
    image_filename = 'image.jpg'  # Change this to the appropriate filename if needed
    image_path = save_image(image_data, image_filename)
    
    # Perform plant identification here
    files = {'images': open(image_path, 'rb')}
    response = requests.post(api_endpoint, files=files)
    
    if response.status_code == 200:
        json_result = response.json()
        plant_type = json_result['bestMatch']
        pprint(plant_type)
        return render_template("index.html", plant_type=plant_type)
    else:
        return render_template("index.html")

@app.route('/templates/<path:filename>')
def serve_image(filename):
    return send_from_directory('templates', filename)

@app.route('/templates/<path:filename>')
def serve_file(filename):
    return send_from_directory('templates', filename)

@app.route("/")
def welcome():
    global plant_type
    pprint(plant_type)
    return render_template("index.html", plant_type=plant_type)



if __name__ == "__main__":
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(host="0.0.0.0", port=33)