import uvicorn
import requests
import threading
import time
import os
import joblib
import pandas as pd
from dotenv import load_dotenv
from auth import verify_api_key
from fastapi import FastAPI, Depends
from pydantic import BaseModel
import nest_asyncio




# Load the trained model from file
try:
    model = joblib.load("loan_success_model.joblib")
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None  # Ensure model is set to None if loading fails

"""**Defining FastAPI App & Request Model**"""


# Define the request model for input validation
class LoanApplicationData(BaseModel):
    Amount: float
    Term: float
    EmploymentType: float
    ALL_AgeOfOldestAccount: float
    ALL_AgeOfYoungestAccount: float
    ALL_Count: float
    ALL_CountActive: float
    ALL_CountClosedLast12Months: float
    ALL_CountDefaultAccounts: float
    ALL_CountOpenedLast12Months: float
    ALL_CountSettled: float
    ALL_MeanAccountAge: float
    ALL_SumCurrentOutstandingBal: float
    ALL_SumCurrentOutstandingBalExcMtg: float
    ALL_TimeSinceMostRecentDefault: float
    ALL_WorstPaymentStatusActiveAccounts: float

# Initialize FastAPI
app = FastAPI()

"""**Define FastAPI Prediction Endpoint**"""

@app.post("/predict")
def predict(data: LoanApplicationData, api_key: str=Depends(verify_api_key)):
    """Predicts loan application success using the trained model."""
    if model is None:
        return {"error": "Model not loaded"}

    try:
        # Convert Pydantic model to DataFrame
        df = pd.DataFrame([data.model_dump()])
        prediction = model.predict(df)
        return {"prediction": int(prediction[0])}  # Return prediction as an integer
    except Exception as e:
        return {"error": str(e)}

"""**Start FastAPI Server in a Background Thread**"""

# Allow FastAPI to run
nest_asyncio.apply()

# Function to run FastAPI server
def run_api():
    """Starts FastAPI with Uvicorn in a separate thread."""
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")

# Start FastAPI server in a background thread
thread = threading.Thread(target=run_api, daemon=True)
thread.start()

# Give the server time to start
time.sleep(3)
print("FastAPI server started successfully!")

