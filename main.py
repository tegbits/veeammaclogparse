import time
# Import necessary functions and variables
from helper import getDirectory, getLogInfo
from sender import sendDataInEmail

# Import constants from enums and modules
from constant.constansEnum import TARGET_TOMORROW_DATE
from constant.templateTypeEnum import ERROR_TYPE
from constant.errorEnum import DIRECTORY_NOT_FOUND, FILE_NOT_FOUND
from constant.config.configEnum import SENDER_EMAIL
def mainFn ():
    # Initialize an empty list to store paths
    arrPath = {}
    # Get directories and populate arrPath
    getDirectory(arrPath)
    if not arrPath:
        getDirectory(arrPath, time=TARGET_TOMORROW_DATE)
    if not arrPath:
        # If arrPath is empty, send an error email and print an error message
        errorMsg = DIRECTORY_NOT_FOUND
        sendDataInEmail(errorMsg, SENDER_EMAIL, templateType=ERROR_TYPE)
        print(errorMsg.get('title'))
        return
    
    # Get log data from all found path
    data = getLogInfo(arrPath)
    print(arrPath)
    
    if not data:
        # If log file is empty, send an error email and print an error message
        errorMsg = FILE_NOT_FOUND
        sendDataInEmail(errorMsg, SENDER_EMAIL, templateType=ERROR_TYPE)
        print(errorMsg.get('title'))
        return
    # If data is available, print success message and send the email
    for i in range(0, len(data)):
        time.sleep(15)
        sendDataInEmail(data[i], SENDER_EMAIL);
    print('Send Logs in Email Success')
    

try:
    mainFn()
except Exception as e:
    print(f'Something went wrong: {e}')
    sendDataInEmail({'title': 'Something went wrong' , 'msg': str(e)}, SENDER_EMAIL, templateType=ERROR_TYPE)

