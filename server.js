import { Router } from "express";
const API_KEY = "2b10sI4pUqsrJchBzXFo9W0Ie";
const PROJECT = "all";
const router =  Router();
router.route("/register").post(
    upload.fields([
        {
          name: "image.jpg" ,
        },
    ]),
    registerUser
    )
async function identifyPlant() {
    // Send request to ESP32 to capture and send image
    fetch(image.jpg)
    .then(response => response.blob())
    .then(imageBlob => {
        // Send captured image to PlantNet API
        const formData = new FormData();
        formData.append('file', imageBlob);

        fetch('https://my-api.plantnet.org/v2/identify/' + PROJECT + '?api-key=' + API_KEY, {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            const plantType = data.results[0].species.scientificNameWithoutAuthor;

            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = `<p>Identified Plant Type: ${plantType}</p>`;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    })
    .catch(error => {
        console.error('Error:', error);
    });
}