import express from "express";
import cors from "cors";
import { Router } from "express";
import fetch from "node-fetch"; // Import fetch for Node.js environment
import multer from "multer"; // Import multer for file uploads

const API_KEY = "2b10sI4pUqsrJchBzXFo9W0Ie";
const PROJECT = "all";
const app = express();
const router = Router(); // Moved router declaration before its usage

// Set up CORS middleware
app.use(cors({
    origin: process.env.CORS_ORIGIN,
    credentials: true
}));

// Set up multer for file uploads
const upload = multer();

// Define route for registering users
router.post("/register", upload.single("image"), registerUser);

// Mount the router
app.use("/api/v1/imagerecover", router);

// Define registerUser function
async function registerUser(req, res) {
    try {
        // Access the uploaded file via req.file
        const imageBlob = req.file.buffer;

        // Send captured image to PlantNet API
        const formData = new FormData();
        formData.append('file', imageBlob);

        const plantNetResponse = await fetch('https://my-api.plantnet.org/v2/identify/' + PROJECT + '?api-key=' + API_KEY, {
            method: 'POST',
            body: formData
        });

        const data = await plantNetResponse.json();
        const plantType = data.results[0].species.scientificNameWithoutAuthor;

        res.json({ plantType });
    } catch (error) {
        console.error('Error:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
}

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
