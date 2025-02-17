import os
from dotenv import load_dotenv

# Loading Environment Variables 
load_dotenv()
# Retrieve API Key 
API_KEY = os.getenv("API_KEY")
