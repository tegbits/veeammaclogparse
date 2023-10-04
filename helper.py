import os
import re

from constant.regexEnum import PATTERN_DIR, PATTERN_DATE
from constant.constansEnum import TARGET_FILE, DEFAULT_START_PATH
from constant.config.configEnum import TYPE_INFO
from constant.informationTypeEnum import FULL_TYPE, SHORT_TYPE, STATUS_TYPE, WARNING_TYPE, WARN_TYPE , ERROR_TYPE

def getDirectory(arr, newPath = False):
    # Create a list to store the content of the current directory
    content = []
    if (not(newPath)):
        # Iterate through all files and directories in the current directory
        for file in os.scandir():
            if (os.path.isdir(file)):
                if (not(re.findall(PATTERN_DIR, file.name))):
                    # Add the path again in function if it doesn't have a pattern
                    content.append(file.name)
                if (re.findall(PATTERN_DATE, file.name)):
                    # Add the full path to the list if the required directory is found
                    arr.append(os.path.join(newPath, file.name))
                    return;
        # If no path was provided, set it to the default path
        newPath = DEFAULT_START_PATH
    else:
        # Similar logic for the specified path
        for file in os.scandir(newPath):
            if (os.path.isdir(file)):
                if (not(re.findall(PATTERN_DIR, file.name))):
                    content.append(file.name)
                if (re.findall(PATTERN_DATE, file.name)):
                    arr.append(os.path.join(newPath, file.name))
                    return;
    if content:
        # Recursive call to the function for subdirectories because folders don't have a pattern
        for path in content:
            getDirectory(arr, os.path.join(newPath, path))
        return
    return

def getLogInfo (arr):
    log = []
    for currentPath in arr:
        with os.scandir(currentPath) as files:
            for file in files:
                if (file.name.capitalize() == TARGET_FILE):
                    with open(os.path.join(currentPath, file.name), 'r', encoding="utf8") as fileData:
                        logInfo = fileData.readlines()
                        name = os.path.basename(os.path.dirname(currentPath))
                        logWarning, logWARN, logError, logStatus = [],[],[],[]
                        if (FULL_TYPE in TYPE_INFO):
                            # Processing for FULL information type
                            for str in logInfo:
                                if (re.findall(r'JOB STATUS', str)):
                                    logStatus.append(str);
                                if (re.findall(r'\[warn\]', str)):
                                    logWarning.append(str);
                                if (re.findall(r'WARN', str)):
                                    logWARN.append(str)
                                if (re.findall(r'ERR', str)):
                                    logError.append(str)
                        elif (SHORT_TYPE in TYPE_INFO):
                            # Processing for SHORT information type
                            for str in logInfo:
                                if (re.findall(r'JOB STATUS', str)):
                                    logStatus.append(str);
                        else:
                            # Processing for other information type
                            for str in logInfo:
                                if (STATUS_TYPE in TYPE_INFO and re.findall(r'JOB STATUS', str)):
                                    logStatus.append(str);
                                if (WARNING_TYPE in TYPE_INFO and re.findall(r'\[warn\]', str)):
                                    logWarning.append(str);
                                if (WARN_TYPE in TYPE_INFO and re.findall(r'WARN', str)):
                                    logWARN.append(str)
                                if (ERROR_TYPE in TYPE_INFO and re.findall(r'ERR', str)):
                                    logError.append(str)
                        # Add formatted information to the log list
                        log.append({
                            'name': name,
                            'Warning': logWarning,
                            'WARN': logWARN,
                            'Error': logError,
                            'Status': logStatus
                        });
                        break
    return log
