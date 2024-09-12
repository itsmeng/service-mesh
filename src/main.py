from flask import Flask, request, jsonify
import parameters
import requests
import os
from functions_facts import FUNCTIONS_DICT
from feature_flag import FEATURE_FLAGS
import logging
from GCP_handler.invoke_function import call_cloud_function
from utility import convert_to_string
from email_lib.send_email import send_email

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# This would be replaced with actual cloud function URLs

@app.route('/mesh/<function_name>', methods=['POST'])
def mesh_gateway(function_name):
    if function_name not in FUNCTIONS_DICT:
        return jsonify({'error': 'Function not found'}), 404
    elif function_name not in FEATURE_FLAGS:
        return jsonify({'error': 'Function not released yet! Please check with admin'}), 404    
    # Forward the request to the appropriate cloud function
    cloud_function_url = FUNCTIONS_DICT[function_name]
    
    # Forward headers and body
    headers = {key: value for (key, value) in request.headers if key != 'Host'}
    data = request.get_data()
    data = convert_to_string(data)
    logging.info(f"headers = {data}")

    try:
        logging.info(f"Calling cloud functions {cloud_function_url}")
        response = call_cloud_function(cloud_function_url, data)
        logging.info(f"response = {response}")
        email_data = { "receiver": "test@test.com", "subject": "Test Subject", "body": response.content }
        send_email(email_data)
        return (response.content, response.status_code, response.headers.items())
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))