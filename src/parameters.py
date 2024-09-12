


import socket
import logging
import os 
# Set up logging
logging.basicConfig(level=logging.INFO)

# Get the server hostname
server_hostname = socket.gethostname()
logging.info(f"Server hostname: {server_hostname}")

# Set variable based on server hostname
if server_hostname == "abc":
    logging.info(f"abc configuration")
    function_name = "function-1"    
else:
    logging.info(f"Default configuration")
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "my-service-account-key.json"