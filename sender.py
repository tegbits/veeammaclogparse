import ssl, smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from template import templateInfo
from constant.config.configEnum import SECRET_EMAIL, SECRET_PASS, SENDER_EMAIL, SMTP_HOST, SMTP_PORT
from constant.templateTypeEnum import JOB_TYPE

# Create an instance of EmailMessage and MIMEMultipart
em = EmailMessage()
msg = MIMEMultipart('alternative')

def sendDataInEmail(data, emails=SENDER_EMAIL, templateType = JOB_TYPE):
    """
    Send an email with provided data.

    Args:
        data (list): List of dictionaries containing email data.
        emails (str or list): Single email or list of emails to send to.
        templateType (str): Type of email template to use.

    Note:
        Make sure to have the necessary environment variables loaded for SECRET_EMAIL and SECRET_PASS.
    """
    
    # Get the template information for the specified type
    template = templateInfo[templateType]

    # Generate HTML content from the template using the provided data
    htmlEmail = template['html'](data)
    htmlPart = MIMEText(htmlEmail, 'html')
    
    # Set the sender, recipient, and subject of the email
    msg['From'] = SECRET_EMAIL
    msg['To'] = ', '.join(emails)
    
    # If templateType is JOB_TYPE, add title based on the first entry's name
    msg['Subject'] = template['subject'](data[0].get('name')) if templateType == JOB_TYPE else template['subject']
    
    # Attach the HTML content to the email
    msg.attach(htmlPart)
    
    # Create a secure SSL context
    context = ssl.create_default_context()
    
    # Connect to the SMTP server using SSL
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context) as smtp:
        try:
            # Log in to the SMTP server using the secret email and password
            smtp.login(SECRET_EMAIL, SECRET_PASS)
            # Send the email
            smtp.sendmail(SECRET_EMAIL, emails, msg.as_string())
        except Exception as e:
            print(f'Failed to send email to {", ".join(emails)} \n\n\n{e}')
        finally:
            smtp.quit()
