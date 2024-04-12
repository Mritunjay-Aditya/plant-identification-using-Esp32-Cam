# Plant Identification System

## Overview
This project aims to create a system for identifying plants using image recognition technology. It utilizes an ESP32-CAM module to capture plant images and sends them to a Flask server for processing. The server then communicates with the PlantNet API to identify the plant species and returns the result to the user interface.

## Components
- ESP32-CAM module: Captures plant images and sends them to the server.
- Flask server: Receives images from the ESP32-CAM, performs plant identification using the PlantNet API, and returns the result.
- PlantNet API: A plant identification API that takes an image as input and returns the identified plant species.

## Requirements
- Hardware:
  - ESP32-CAM module
- Software:
  - Arduino IDE (for ESP32-CAM firmware)
  - Python 3.x
  - Flask
  - Requests library
  - PlantNet API key

## Installation
1. **ESP32-CAM Firmware:**
   - Upload the provided ESP32-CAM code to your ESP32-CAM module using the Arduino IDE. Make sure to update the Wi-Fi credentials (`ssid` and `password`) and the Flask server IP address (`http://192.168.xxx.xxx:33/identify`) in the code.

2. **Flask Server:**
   - Install Python 3.x and pip.
   - Install Flask and Requests library using pip:
     ```
     pip install Flask requests
     ```

3. **PlantNet API Key:**
   - Sign up for an account on [PlantNet](https://plantnet.org/) and obtain an API key.

4. **Run the Server:**
   - Replace the `API_KEY` variable in `app.py` with your PlantNet API key.
   - Start the Flask server:
     ```
     python app.py
     ```

5. **Web Interface:**
   - Access the web interface by navigating to `http://localhost:33` in your web browser.

## Usage
1. Power on the ESP32-CAM module.
2. Navigate to the web interface.
3. Click on the "Identify Plant" button to capture an image.
4. Wait for the identification process to complete.
5. The identified plant species will be displayed on the web interface.


