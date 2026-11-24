const predictionForm = document.getElementById("predictionForm");
const predictButton = document.getElementById("predictButton");
const resultSection = document.getElementById("result");
const predictionText = document.getElementById("predictionText");
const probabilityText = document.getElementById("probabilityText");
const errorMessage = document.getElementById("errorMessage");

predictionForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    errorMessage.textContent = "";
    resultSection.classList.add("hidden");

    const patientData = {
        age: Number(document.getElementById("age").value),
        sex: document.getElementById("sex").value,
        blood_pressure: Number(document.getElementById("blood_pressure").value),
        cholesterol: Number(document.getElementById("cholesterol").value),
        bmi: Number(document.getElementById("bmi").value),
        smoker: document.getElementById("smoker").value,
        diabetes: document.getElementById("diabetes").value,
        physical_activity: Number(document.getElementById("physical_activity").value),
        family_history: document.getElementById("family_history").value,
        stress_level: Number(document.getElementById("stress_level").value)
    };

    predictButton.disabled = true;
    predictButton.textContent = "Processing...";

    try {
        const response = await fetch("/api/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(patientData)
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Prediction request failed.");
        }

        predictionText.textContent = data.result;
        probabilityText.textContent =
            "Estimated probability of heart disease: " +
            data.probability + "%";

        resultSection.classList.remove("hidden");

    } catch (error) {
        errorMessage.textContent =
            "Unable to make prediction: " + error.message;

    } finally {
        predictButton.disabled = false;
        predictButton.textContent = "Predict Heart Disease";
    }
});