import logging

def send_email(email_data):
    logging.info(f"Sending email to {email_data['receiver']} with subject {email_data['subject']}")
    logging.info(f"Email body: {email_data['body']}")
    pass