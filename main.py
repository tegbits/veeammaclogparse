import os,re
from dotenv import load_dotenv
load_dotenv()
from helper import getDirectory, getLogInfo, target_date
from sender import secret_email, sendDataInEmail
from constant.templateEnum import ERROR_TYPE
import constant.errorEnum as errorEnum


sender_email = os.getenv('SEND_EMAIL')

pattern_date = re.escape(target_date)
def mainFn ():
    arrPath = []
    getDirectory(arrPath)
    print(arrPath)
    if not arrPath:
        errorMsg = errorEnum.DIRECTORY_NOT_FOUND
        sendDataInEmail(errorMsg, secret_email, ERROR_TYPE)
        print(errorMsg.get('title'))
        return
    data = getLogInfo(arrPath)
    if not data:
        errorMsg = errorEnum.FILE_NOT_FOUND
        sendDataInEmail(errorEnum.FILE_NOT_FOUND, secret_email, ERROR_TYPE)
        print(errorMsg.FILE_NOT_FOUND.get('title'))
        return
    print('Send Logs in Email Success')
    sendDataInEmail(data, secret_email)
    

try:
    mainFn()
except Exception as e:
    print(f'Something went wrong: {e}')
    sendDataInEmail({'title': 'Something went wrong' , 'msg': str(e)}, secret_email, ERROR_TYPE)

