# smtplib for sending email, ssl for secure connection
import smtplib, ssl


def send_email(message):
    # Gmail's SMTP server and SSL port
    host = "smtp.gmail.com"
    port = 465

    # Your Gmail credentials
    username = "pedro.h.li.edu@gmail.com"
    password = "YOUR GMAIL APP PASSWORD"

    # Email recipient
    receiver = "pedro.h.li.edu@gmail.com"
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Connect to Gmail's SMTP server securely using SSL
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        # Log in to the Gmail account
        server.login(username, password)
        # Send the email
        server.sendmail(username, receiver, message)
