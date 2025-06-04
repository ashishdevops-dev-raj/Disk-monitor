import os
import sys
import smtplib
from email.message import EmailMessage

SMTP_SERVER = os.environ.get("SMTP_SERVER")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
EMAIL_FROM = os.environ.get("EMAIL_FROM")
EMAIL_TO = os.environ.get("EMAIL_TO")

if len(sys.argv) < 2:
    print("No alert message provided.")
    sys.exit(1)

message_body = sys.argv[1]

msg = EmailMessage()
msg.set_content(message_body)
msg['Subject'] = "Disk Alert Notification"
msg['From'] = EMAIL_FROM
msg['To'] = EMAIL_TO

try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)
    print(f"Email sent to {EMAIL_TO}")
except Exception as e:
    print(f"Failed to send email: {e}")
