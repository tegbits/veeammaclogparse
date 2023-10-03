import os
import ssl
import smtplib
from dotenv import load_dotenv
load_dotenv()
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from template import templateInfo

secret_email = os.getenv('NO_REPLY_EMAIL')
secret_pass = os.getenv('NO_REPLY_PASS')
sender_email = os.getenv('SEND_EMAIL')

em = EmailMessage()
msg = MIMEMultipart('alternative')


def sendDataInEmail(data, email = sender_email, templateType = 'JOBSTATUS'):
    template = templateInfo[templateType]
    htmlEmail = template['html'](data)
    htmlPart = MIMEText(htmlEmail, 'html')
    msg['From'] = secret_email
    msg['To'] = email
    msg['Subject'] = template['subject']
    msg.attach(htmlPart)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        try:
            smtp.login(secret_email, secret_pass)
            smtp.sendmail(secret_email, email, msg.as_string())
        except Exception as e:
            print(f'Fail send email in {email} \n\n\n{e}')
        finally:
            smtp.quit()