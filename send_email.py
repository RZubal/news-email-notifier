import os
import smtplib
import ssl


def send_email(message: str):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    receiver = os.getenv("EMAIL_RECEIVER", username)

    if not username or not password:
        raise RuntimeError("Email credentials not set in environment variables")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(
            from_addr=username,
            to_addrs=receiver,
            msg=message.encode("utf-8")
        )

