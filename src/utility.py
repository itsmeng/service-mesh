def convert_to_string(data):
    # Convert bytes to string if necessary #
    if isinstance(data, bytes):
        return data.decode('utf-8')
    return data