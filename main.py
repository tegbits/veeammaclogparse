# Import necessary functions and variables
from helper import getDirectory, getLogInfo
from sender import sendDataInEmail

# Import constants from enums and modules
from constant.templateTypeEnum import ERROR_TYPE
import constant.errorEnum as errorEnum
from constant.config.configEnum import SENDER_EMAIL

def mainFn ():
    # Initialize an empty list to store paths
    arrPath = {}
    # Get directories and populate arrPath
    getDirectory(arrPath)
    if not arrPath:
        # If arrPath is empty, send an error email and print an error message
        errorMsg = errorEnum.DIRECTORY_NOT_FOUND
        sendDataInEmail(errorMsg, SENDER_EMAIL, ERROR_TYPE)
        print(errorMsg.get('title'))
        return
    # Get log data from all found path
    data = getLogInfo(arrPath)
    print(arrPath)
    
    if not data:
        # If log file is empty, send an error email and print an error message
        errorMsg = errorEnum.FILE_NOT_FOUND
        sendDataInEmail(errorEnum, SENDER_EMAIL, ERROR_TYPE)
        print(errorMsg.FILE_NOT_FOUND.get('title'))
        return
    # If data is available, print success message and send the email
    print('Send Logs in Email Success')
    sendDataInEmail(data, SENDER_EMAIL)
    

try:
    mainFn()
except Exception as e:
    print(f'Something went wrong: {e}')
    sendDataInEmail({'title': 'Something went wrong' , 'msg': str(e)}, SENDER_EMAIL, ERROR_TYPE)

