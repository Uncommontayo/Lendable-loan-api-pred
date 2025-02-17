# Lendable-loan-api-pred - FastAPI Deployment 🚀
📍 Overview

This project is an end-to-end machine learning model deployment using FastAPI. The model predicts the likelihood of loan success based on financial data. The API is deployed via Ngrok for external access and includes unit tests for validation.

📌 Table of Contents

    Installation
    Project Structure
    How to Run the API
    Testing the API
    Endpoints
    Project Details
    Authors & Contact

📌 Installation

Clone the repository and install the required dependencies.

```plaintext
git clone git@github.com:your-username/loan-prediction-api.git
cd loan-prediction-api
pip install -r requirements.txt
```
For Google Colab, install dependencies inside the notebook:

```
!pip install fastapi uvicorn requests pandas joblib pyngrok unittest
```

📌 Project Structure

## 📂 Project Structure
```plaintext
loan-prediction-api/
│── model/
│   ├── loan_success_model.joblib   # Trained model
│── api/
│   ├── main.py                     # FastAPI application
│   ├── schema.py                   # Pydantic validation models
│── tests/
│   ├── test_api.py                  # Unit tests
│── notebooks/
│   ├── model_training.ipynb         # Model training & evaluation
│── requirements.txt                 # Required libraries
│── README.md                        # Project documentation
```

📌 How to Run the API

1️⃣ Start FastAPI server
```
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
```

For Google Colab, run:
```
import threading
import uvicorn

def run():
    uvicorn.run(app, host="0.0.0.0", port=8000)

thread = threading.Thread(target=run, daemon=True)
thread.start()
```
2️⃣ Start Ngrok to expose API externally
```
from pyngrok import ngrok
public_url = ngrok.connect(8000)
print(f"Public Ngrok URL: {public_url}")
```

📌 Testing the API

```
Run unit tests to validate the API:

python -m unittest tests/test_api.py
```

For Google Colab:
```
!python -m unittest discover -s tests
```

📌 Endpoints
Method	Endpoint	Description
POST	/predict/	Loan success prediction
```
Example POST request:

{
    "Amount": 5000,
    "Term": 24,
    "EmploymentType": 1,
    "ALL_AgeOfOldestAccount": 120,
    "ALL_AgeOfYoungestAccount": 12,
    "ALL_Count": 10,
    "ALL_CountActive": 5
}
```
Example response
```
{"prediction": 1}
```
📌 Project Details

    Model Type: Gradient Boosted Tree
    API Framework: FastAPI
    Deployment: Google Colab + Ngrok
    Testing Framework: Unittest


✅ Final Notes

    Ensure Ngrok authentication is correctly set up.
    Provide Colab notebook + API scripts for easy reproducibility.
    All code follows production best practices.
