import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import SENDGRID_SMTP_SERVER, SENDGRID_SMTP_PORT, SENDGRID_USERNAME, SENDGRID_API_KEY

class EmailService:
    @staticmethod
    def send_email_via_smtp(to_email, subject, username):
        from_email = "jawdathamdan91@gmail.com"
        body = f"Beste HR,\n\nDe medewerker {username} heeft zich vandaag ziekgemeld.\n\nMet vriendelijke groet,\nZiekmeldingssysteem"
        
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP(SENDGRID_SMTP_SERVER, SENDGRID_SMTP_PORT)
            server.starttls()
            server.login(SENDGRID_USERNAME, SENDGRID_API_KEY)
            server.sendmail(from_email, to_email, msg.as_string())
            server.quit()
            print(f"E-mail verzonden naar {to_email}")
        except Exception as e:
            print(f"Fout bij het versturen van de e-mail: {e}")
