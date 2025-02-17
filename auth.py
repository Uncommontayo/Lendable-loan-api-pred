from fastapi import Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from config import API_KEY




API_KEY_NAME = 'APP-API-KEY'
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

def verify_api_key(api_key:str=Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, message="Invalid API key")
    return api_key
