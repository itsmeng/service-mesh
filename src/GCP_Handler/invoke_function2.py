# Temp token method created from .py file
# This function if for any reason you can't have the .json file 
# possible use case - pyinstaller where you can't have the .json file, cred will stored in .py file for compile


import requests
from google.auth.transport.requests import Request
import google.oauth2.id_token
import google.auth
import google.auth.transport.requests
import requests
import logging
from credentials import create_temp_credentials_file, cleanup_temp_file

# Set up logging
logging.basicConfig(level=logging.INFO)

def fetch_token(function_url):
    request = Request()  # Simplified import usage
    try:
        token = google.oauth2.id_token.fetch_id_token(request, function_url)
    except Exception as e:
        raise
    if token is None:
        raise ValueError("Unable to generate token. Check your credentials.")
    return token

def create_headers(token):
    headers = {  # Use a variable for clarity
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    return headers

def send_request(function_url, headers, data):
    response = requests.post(function_url, headers=headers, json=data, timeout=70)  # Use a variable for clarity
    return response

def handle_response(response):
    if response.status_code == 200:
        logging.info("Function called successfully!")
    else:
        logging.info(f"Error calling function. Status code: {response.status_code}")
    logging.info(f"Response: {response.text}")

def call_cloud_function(function_url, data):
    try:
        temp_file_path = create_temp_credentials_file()
        token = fetch_token(function_url)
        headers = create_headers(token)
        response = send_request(function_url, headers, data)
        handle_response(response)
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
    finally:
        cleanup_temp_file(temp_file_path)
        logging.info(f"Temp file deleted: {temp_file_path}")  
    return response


def main():
    function_url = ''
    data = {"ee": "ee"}
    try:
        response = call_cloud_function(function_url, data)  
        print(response.status_code)
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        
if __name__ == "__main__":
    main()