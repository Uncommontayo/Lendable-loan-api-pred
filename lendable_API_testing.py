import requests


""" **Send a Test Request to Verify API**"""

# Sample request data for testing
data = {
    "Amount": 7000, "Term": 48, "EmploymentType": 1,
    "ALL_AgeOfOldestAccount": 199, "ALL_AgeOfYoungestAccount": 4,
    "ALL_Count": 11, "ALL_CountActive": 8, "ALL_CountClosedLast12Months": 0,
    "ALL_CountDefaultAccounts": 0, "ALL_CountOpenedLast12Months": 3,
    "ALL_CountSettled": 3, "ALL_MeanAccountAge": 69.73,
    "ALL_SumCurrentOutstandingBal": 124050, "ALL_SumCurrentOutstandingBalExcMtg": 1186,
    "ALL_TimeSinceMostRecentDefault": -1, "ALL_WorstPaymentStatusActiveAccounts": 0
}

api_url = "http://127.0.0.1:8000/predict"  
api_key = "sampleApiKey"
headers = {"APP-API-KEY": api_key}
response = requests.post(api_url, json=data, headers=headers)
if response.status_code == 200:
    print("API Response:", response.json())  
else:
    print("API request not Available!")
    