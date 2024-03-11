<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plant Identification</title>
</head>
<body>
    <h1>Plant Identification</h1>
    <form id="uploadForm" enctype="multipart/form-data">
        <input type="file" name="imageFile" id="imageFile">
        <button type="submit">Identify Plant</button>
    </form>
    <br>
    <div id="imagePreview"></div>
    <div id="response"></div>

    <script>
        document.getElementById("uploadForm").addEventListener("submit", function(event){
            event.preventDefault();
            var formData = new FormData();
            var fileInput = document.getElementById('imageFile');
            formData.append('file', fileInput.files[0]);

            fetch('/', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById("response").innerText = "Identified Plant: " + data.plantType;
            })
            .catch(error => {
                console.error('Error:', error);
                document.getElementById("response").innerText = "Error identifying plant.";
            });
        });

        document.getElementById('imageFile').addEventListener('change', function() {
            var file = this.files[0];
            if (file) {
                var reader = new FileReader();
                reader.onload = function(event) {
                    var img = document.createElement('img');
                    img.src = event.target.result;
                    img.style.maxWidth = '400px'; // Limit image width for display
                    document.getElementById('imagePreview').innerHTML = '';
                    document.getElementById('imagePreview').appendChild(img);
                };
                reader.readAsDataURL(file);
            }
        });
    </script>
</body>
</html>
