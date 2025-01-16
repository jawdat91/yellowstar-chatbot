import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import SENDGRID_SMTP_SERVER, SENDGRID_SMTP_PORT, SENDGRID_USERNAME, SENDGRID_API_KEY
import cx_Oracle
from db import Database

class EmailService:
    # Get the HR email address and the manager's email address for a given employee
    @staticmethod
    def get_email_addresses(employee_id):
        conn = Database.get_connection() 
        hr_email = None
        manager_email = None
        
        if conn:
            try:
                cur = conn.cursor()

                # Get HR e-mailadres
                query_hr_email = '''
                    SELECT STRINGVALUE 
                    FROM SYSTEMPARAMETER 
                    WHERE PARAMETERCODE = 'HR_EMAIL'
                '''
                cur.execute(query_hr_email)
                hr_email_result = cur.fetchone()
                hr_email = hr_email_result[0] if hr_email_result else None

                # GET manager ID
                query_manager_id = '''
                    SELECT MANAGER_ID 
                    FROM EMPLOYEES 
                    WHERE ID = :employee_id
                '''
                cur.execute(query_manager_id, [employee_id])
                manager_id_result = cur.fetchone()
                manager_id = manager_id_result[0] if manager_id_result else None

                # Get the e-mailadres of the manager
                if manager_id is not None:
                    query_manager_email = '''
                        SELECT EMAIL_YSS 
                        FROM EMPLOYEES 
                        WHERE ID = :manager_id
                    '''
                    cur.execute(query_manager_email, [manager_id])
                    manager_email_result = cur.fetchone()
                    manager_email = manager_email_result[0] if manager_email_result else None

                # Check if the email addresses are valid
                if hr_email is None or manager_email is None:
                    print("Een of beide e-mailadressen zijn niet gevonden.")
                    return None, None

                return hr_email, manager_email

            except cx_Oracle.Error as e:
                print(f"Error retrieving email addresses: {e}")
                return None, None
            finally:
                if cur:
                    cur.close() 
                if conn:
                    conn.close()  

    @staticmethod
    def send_email_via_smtp(employee_id, username):
        """Verzendt een e-mail naar HR en de manager met de ziekmelding."""
        hr_email, manager_email = EmailService.get_email_addresses(employee_id)

        if hr_email and manager_email:
            from_email = "jawdathamdan91@gmail.com"
            body = f"Geachte heer/mevrouw,\n\nDe medewerker {username} heeft zich vandaag ziekgemeld.\n\nMet vriendelijke groet,\nZiekmeldingssysteem"

            # Create email message
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = ", ".join([hr_email, manager_email])  # Add HR and manager as recipients
            msg['Subject'] = "Ziekmelding medewerker"
            msg.attach(MIMEText(body, 'plain'))

            try:
                # Send email via SMTP
                server = smtplib.SMTP(SENDGRID_SMTP_SERVER, SENDGRID_SMTP_PORT,)  
                server.starttls()
                server.login(SENDGRID_USERNAME, SENDGRID_API_KEY)
                server.sendmail(from_email, [hr_email, manager_email], msg.as_string())
                server.quit()  

                print(f"E-mail verzonden naar HR ({hr_email}) en manager ({manager_email})")

            except Exception as e:
                print(f"Fout bij het versturen van de e-mail: {e}")
