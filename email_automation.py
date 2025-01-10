import smtplib
from email.mime.text import MIMEText
import os

# Function to send an email
def send_email(to_address, subject, message):
    from_address = os.getenv('EMAIL_ADDRESS')  # Fetch email from environment variable
    password = os.getenv('EMAIL_PASSWORD')  # Fetch password from environment variable

    if not from_address or not password:
        print("Error: Email address or password not set in environment variables.")
        return

    # Create the email content
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address

    # Send the email using SMTP
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:  # Adjust SMTP server and port as needed
            server.login(from_address, password)
            server.sendmail(from_address, to_address, msg.as_string())
            print(f"Email sent to {to_address}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    recipient = 'lenardabagat649@gmail.com'
    subject = 'Test Subject'
    body = 'This is a test email sent via Python.'
    send_email(recipient, subject, body)
