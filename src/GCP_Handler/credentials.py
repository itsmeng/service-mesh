# credentials.py

import json
import os
import tempfile

service_account_info = {
    "type": "service_account",
    "project_id": "",
    "private_key_id": "",
    "private_key": "",
    "client_email": "",
    "client_id": "",
}

def create_temp_credentials_file():
    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(mode='w+t', suffix='.json', delete=False)
    
    # Write the service account info to the temporary file
    json.dump(service_account_info, temp_file)
    temp_file.close()
    
    # Set the environment variable to point to this file
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = temp_file.name
    print(temp_file.name)
    
    return temp_file.name

def cleanup_temp_file(file_path):
    # Remove the temporary file
    if os.path.exists(file_path):
        os.remove(file_path)
    
    # Unset the environment variable
    if 'GOOGLE_APPLICATION_CREDENTIALS' in os.environ:
        del os.environ['GOOGLE_APPLICATION_CREDENTIALS']