import logging

def send_email(email_data):
    """Send an email with the provided data.

    Args:
        email_data (dict): A dictionary containing 'receiver', 'subject', and 'body' of the email.
    """
    logging.info(f"Sending email to {email_data['receiver']} with subject {email_data['subject']}")
    logging.info(f"Email body: {email_data['body']}")
    pass