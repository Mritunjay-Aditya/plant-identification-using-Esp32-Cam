async function identifyPlant() {
    try {
        const response = await fetch('/api/v1/imagerecover/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'image/jpeg' // assuming your ESP32 sends JPEG images
            },
            body: await captureImageFromESP32() // assuming this function is defined elsewhere to capture image
        });

        const data = await response.json();
        const plantType = data.plantType;

        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = `<p>Identified Plant Type: ${plantType}</p>`;
    } catch (error) {
        console.error('Error:', error);
    }
}

async function captureImageFromESP32() {
    // Placeholder for capturing image from ESP32
    // Replace this with actual implementation based on your ESP32 setup
    return new Promise((resolve, reject) => {
        // Placeholder URL for the image captured from ESP32
        const imageUrl = "url_of_captured_image.jpg"; // Replace with actual URL
        resolve(imageUrl);
    });
}
