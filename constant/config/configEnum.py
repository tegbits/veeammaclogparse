import os
from dotenv import load_dotenv
load_dotenv()

SECRET_EMAIL = os.getenv('NO_REPLY_EMAIL') or 'test@gmail.com'
SECRET_PASS = os.getenv('NO_REPLY_PASS') or 'adfa fasf fasf fafs'
SENDER_EMAIL = os.getenv('SEND_EMAIL') or 'test@gmail.com'
TYPE_INFO = os.getenv('TYPE_INFO').split('+') if os.getenv('TYPE_INFO') else ['FULL']