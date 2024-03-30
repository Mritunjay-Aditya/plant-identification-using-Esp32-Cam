// Function to handle image upload
function handleImageUpload(event) {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function (e) {
        const uploadedImage = e.target.result;
        displayImage(uploadedImage);
        processImage(uploadedImage);
    };

    reader.readAsDataURL(file);
}

// Function to display uploaded image
function displayImage(imageUrl) {
    const imageContainer = document.getElementById('uploaded-image');
    imageContainer.innerHTML = `<img src="${imageUrl}" alt="Uploaded Plant" />`;
}

// Function to process the uploaded image
function processImage(imageUrl) {
    // Display processing animation
    const processingAnimation = document.getElementById('processing-animation');
    processingAnimation.style.display = 'block';

    // Simulate processing delay (replace with actual processing logic)
    setTimeout(() => {
        // Simulated result (replace with actual detection logic)
        const result = {
            plantName: "Rose",
            scientificName: "Rosa",
            description: "The rose is a woody perennial flowering plant of the genus Rosa, in the family Rosaceae."
        };

        displayResult(result);

        // Hide processing animation
        processingAnimation.style.display = 'none';
    }, 2000); // Simulated delay of 2 seconds
}

// Function to display detection result
function displayResult(result) {
    const resultContainer = document.getElementById('detection-result');
    resultContainer.innerHTML = `
        <h2>${result.plantName}</h2>
        <p><strong>Scientific Name:</strong> ${result.scientificName}</p>
        <p>${result.description}</p>
    `;
}

// Event listener for file input change
const fileInput = document.getElementById('file-input');
fileInput.addEventListener('change', handleImageUpload);
