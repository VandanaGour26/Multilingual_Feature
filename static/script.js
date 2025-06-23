// Toggle mobile sidebar menu
function toggleMenu() {
    document.getElementById('sidebar').classList.toggle('active');
}

// Handle file selection from camera
document.getElementById('cameraInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        alert("Photo Captured: " + file.name);
    }
});

// Handle file selection from gallery
document.getElementById('galleryInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        alert("Image Selected: " + file.name);
        }
});

// Function to show preview and send image to backend
function uploadAndDetectDisease(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('result').style.display = 'block'; // Show Result Section
            document.getElementById('diseaseResult').innerText = 'Processing...';

            // Simulate AI Model Processing (Replace this with actual API call)
            setTimeout(() => {
                const diseases = ["Early Blight", "Late Blight", "Bacterial Spot", "Healthy"];
                const randomDisease = diseases[Math.floor(Math.random() * diseases.length)];
                document.getElementById('diseaseResult').innerText = "Detected Disease: " + randomDisease;
            }, 3000); // Simulating API response time
        };
        reader.readAsDataURL(file);
    }
}

// Attach event listeners to file inputs
document.getElementById('cameraInput').addEventListener('change', uploadAndDetectDisease);
document.getElementById('galleryInput').addEventListener('change', uploadAndDetectDisease);
document.getElementById("cameraInput").addEventListener("change", function(event) {
    processImage(event);
});

document.getElementById("galleryInput").addEventListener("change", function(event) {
    processImage(event);
});

function processImage(event) {
    let file = event.target.files[0];

    if (file) {
        let reader = new FileReader();
        reader.onload = function(e) {
            // Show the result section
            document.getElementById("result").style.display = "block";

            // Possible diseases
            let diseases = ["Early Blight", "Late Blight", "Bacterial Spot", "No Disease"];
            let stages = ["Mild", "Moderate", "Severe"];

            // Generate random results
            let disease = diseases[Math.floor(Math.random() * diseases.length)];
            let stage = (disease !== "No Disease") ? stages[Math.floor(Math.random() * stages.length)] : "N/A";

            // Display result
            document.getElementById("diseaseResult").innerHTML = `
                <strong>Disease Detected:</strong> ${disease} <br>
                <strong>Stage:</strong> ${stage}
            `;
        };
        reader.readAsDataURL(file);
    }
}

// Sidebar Toggle for Mobile View
function toggleMenu() {
    let sidebar = document.getElementById("sidebar");
    sidebar.classList.toggle("active");
}

function changeLanguage(lang){
    window.location.href='/${lang}/';
}
