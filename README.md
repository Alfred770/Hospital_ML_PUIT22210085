Hospital Heart Disease Prediction System

1. Project Overview

The Hospital Heart Disease Prediction System is a machine learning-based web application developed for academic and educational purposes.

The application uses patient information to predict the likelihood of heart disease using a trained Logistic Regression model. Users can enter patient details through a web interface and receive a prediction with an estimated probability.

Live Application: https://hospitalmlpuit22210085.vercel.app/

2. Project Objectives

- Explore and analyse a synthetic hospital management dataset.
- Perform data cleaning and preprocessing.
- Develop and evaluate machine learning classification models.
- Select a suitable model based on evaluation results.
- Deploy the selected model as a web application using Vercel.

3. Technologies Used

- Python
- Pandas and NumPy
- Scikit-learn
- Matplotlib and Seaborn
- FastAPI
- HTML, CSS and JavaScript
- Git and GitHub
- Vercel

4. Dataset Description

The project uses a synthetic hospital dataset containing 500 patient records and 11 columns.

The dataset includes:

- Age
- Sex
- Blood Pressure
- Cholesterol
- BMI
- Smoking Status
- Diabetes Status
- Physical Activity
- Family History
- Stress Level
- Heart Disease (Target Variable)

The target variable is "heart_disease", representing the presence or absence of heart disease.

5. Machine Learning Models

Three classification algorithms were trained and evaluated:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

Logistic Regression was selected because it achieved the highest accuracy among the three models.

Model Evaluation Results

Model| Accuracy
Logistic Regression| 56%
Decision Tree| 52%
Random Forest| 54%

Logistic Regression Evaluation

- Accuracy: 56%
- Precision: 56.16%
- Recall: 77.36%
- F1-score: 65.08%

The results indicate that the model has limitations and is not suitable for clinical diagnosis.

6. Application Features

- Patient information input form.
- Heart disease prediction.
- Estimated prediction probability.
- Responsive web interface.
- FastAPI prediction backend.
- Online deployment using Vercel.

7. Project Structure

Hospital_ML_PUIT22210085/
│
├── api/
│   └── index.py
├── data/
│   └── hospital_synthetic_dataset.xlsx.csv
├── models/
│   └── hospital_heart_disease_model.pkl
├── notebooks/
│   └── hospital_dataset_analysis.ipynb
├── public/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── screenshots/
├── app.py
├── train_model.py
├── requirements.txt
├── vercel.json
└── README.md

8. Running the Project Locally

Step 1: Clone the repository

git clone https://github.com/Alfred770/Hospital_ML_PUIT22210085.git

Step 2: Enter the project directory

cd Hospital_ML_PUIT22210085

Step 3: Install dependencies

pip install -r requirements.txt

Step 4: Start the application

python -m uvicorn api.index:app --reload

Step 5: Open the application

Visit:

"http://127.0.0.1:8000"

API documentation:

"http://127.0.0.1:8000/docs"

9. Deployment

The application is deployed on Vercel.

Vercel Project Name: "hospital_ml_puit22210085"

Live Application: https://hospitalmlpuit22210085.vercel.app/

GitHub Repository: https://github.com/Alfred770/Hospital_ML_PUIT22210085

10. Disclaimer

 Disclaimer: This application is developed solely for academic and educational purposes only.

11. Author

Student ID: PUIT22210085

Institution: Pentecost University

Project: Hospital Heart Disease Prediction System