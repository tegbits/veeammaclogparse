import ssl
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from template import templateInfo
from constant.config.configEnum import SECRET_EMAIL, SECRET_PASS, SENDER_EMAIL

# Create an instance of EmailMessage and MIMEMultipart
em = EmailMessage()
msg = MIMEMultipart('alternative')

def sendDataInEmail(data, email = SENDER_EMAIL, templateType = 'JOBSTATUS'):
    # Get the template information for the specified type
    template = templateInfo[templateType]

    # Generate HTML content from the template using the provided data
    htmlEmail = template['html'](data)
    htmlPart = MIMEText(htmlEmail, 'html')
    
    # Set the sender, recipient, and subject of the email
    msg['From'] = SECRET_EMAIL
    msg['To'] = email
    msg['Subject'] = template['subject']
    
    # Attach the HTML content to the email
    msg.attach(htmlPart)
    
    # Create a secure SSL context
    context = ssl.create_default_context()
    
    # Connect to the SMTP server using SSL
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        try:
            # Log in to the SMTP server using the secret email and password
            smtp.login(SECRET_EMAIL, SECRET_PASS)
            # Send the email
            smtp.sendmail(SECRET_EMAIL, email, msg.as_string())
        except Exception as e:
            print(f'Fail send email in {email} \n\n\n{e}')
        finally:
            smtp.quit()

# This function sends an email with provided data, using a specified template type.

# The template type defaults to 'JOBSTATUS' but you can watch another type is template.py.

# Note: Make sure to have the necessary environment variables loaded for SECRET_EMAIL and SECRET_PASS.

