import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.core.config import settings

def send_otp_email(email_to: str, code: str):
    subject = "Tu código de acceso - Cyber sac"

    body = f"""
    <h2>Hola!</h2>
    <p>Tu código de acceso para Cyber sac es:</p>
    <h1 style="letter-spacing: 8px; color: #2563eb;">{code}</h1>
    <p>Este código expira en <strong>10 minutos</strong>.</p>
    <p>Si no solicitaste este código, ignora este mensaje.</p>
    """

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = settings.MAIL_FROM
    message["To"] = email_to
    message.attach(MIMEText(body, "html"))

    with smtplib.SMTP(settings.MAIL_SERVER, settings.MAIL_PORT) as server:
        server.starttls()
        server.login(settings.MAIL_USERNAME, settings.MAIL_PASSWORD)
        server.sendmail(settings.MAIL_FROM, email_to, message.as_string())