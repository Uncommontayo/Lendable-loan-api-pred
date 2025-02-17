# Lendable Loan API Predictor 🚀

## Overview

This project is an end-to-end machine learning model deployment using **FastAPI**. The model predicts the likelihood of loan success based on financial data. The API includes unit tests for validation.

## Table of Contents
```
- [Installation](#installation)
- [Project Structure](#project-structure)
- [How to Run the API](#how-to-run-the-api)
- [Testing the API](#testing-the-api)
- [Endpoints](#endpoints)
- [Project Details](#project-details)
- [Authors & Contact](#authors--contact)
```
## Installation

Clone the repository and install the required dependencies:

```bash
git clone git@github.com:your-username/lendable-loan-api-pred.git
cd lendable-loan-api-pred
pip install -r requirements.txt
```
Run the FastAPI server using Uvicorn:
```
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
```
Ensure all dependencies are installed:
```
pip install -r requirements.txt
```

Then run the application:
```
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
```

Description:
Predicts loan success based on provided financial data.
```
Example Request:

{
    "Amount": 5000,
    "Term": 24,
    "EmploymentType": 1,
    "ALL_AgeOfOldestAccount": 120,
    "ALL_AgeOfYoungestAccount": 12,
    "ALL_Count": 10,
    "ALL_CountActive": 5,
    "ALL_CountClosedLast12Months": 0,
    "ALL_CountDefaultAccounts": 0,
    "ALL_CountOpenedLast12Months": 0,
    "ALL_CountSettled": 0,
    "ALL_MeanAccountAge": 60,
    "ALL_SumCurrentOutstandingBal": 10000,
    "ALL_SumCurrentOutstandingBalExcMtg": 5000,
    "ALL_TimeSinceMostRecentDefault": 0,
    "ALL_WorstPaymentStatusActiveAccounts": 1
}
```
Example Response:
```
{"prediction": 1}
```
Project Details

    Model Type: Gradient Boosted Tree
    API Framework: FastAPI
    Deployment: Google Colab & VS Code
    Testing Framework: Unittest

Final Notes

    Reproducibility: The project includes a Colab notebook and API scripts for easy reproducibility.
    Best Practices: All code adheres to production best practices.






