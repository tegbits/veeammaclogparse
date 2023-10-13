import os, socket, re, urllib.request

from constant.regexEnum import PATTERN_DIR, PATTERN_DATE
from constant.constansEnum import TARGET_FILE, DEFAULT_START_PATH
from constant.config.configEnum import TYPE_INFO
from constant.informationTypeEnum import FULL_TYPE, SHORT_TYPE, STATUS_TYPE, WARNING_TYPE, WARN_TYPE , ERROR_TYPE

def getDirectory(arr, newPath = False):
    # Create a list to store the content of the current directory
    content = []
    if (not(newPath)):
        # If no path was provided, set it to the default path
        newPath = DEFAULT_START_PATH
    # Iterate through all files and directories in the current directory
    for file in os.scandir(newPath):
        if (os.path.isdir(file)):
            if (not(re.findall(PATTERN_DIR, file.name))):
                # Add the path again in function if it doesn't have a pattern
                content.append(file.name)
            if (re.findall(PATTERN_DATE, file.name)):
                    # Add the full path to the object if the required directory is found
                resPath = os.path.join(newPath, file.name)
                nameFolder = os.path.basename(newPath)
                if (not(nameFolder in arr)):
                    arr[nameFolder] = [resPath]
                    continue
                arr[nameFolder].append(resPath)
    if content:
        # Recursive call to the function for subdirectories because folders don't have a pattern
        for path in content:
            getDirectory(arr, os.path.join(newPath, path))
        return
    return

def getLogInfo (arr):
    log = []
    for key in arr.keys():
        counter = 0
        for currentPath in arr[key]:
            with os.scandir(currentPath) as files:
                for file in files:

                    if (file.name.capitalize() == TARGET_FILE):
                        with open(os.path.join(currentPath, file.name), 'r', encoding="utf8") as fileData:
                            name = key if not(counter) else f'{key}({counter + 1})'
                            logInfo = fileData.readlines()
                            logWarning, logWARN, logError, logStatus = [],[],[],[]
                            if (FULL_TYPE in TYPE_INFO):
                                # Processing for FULL information type
                                for str in logInfo:
                                    if (re.findall(r'JOB STATUS', str)):
                                        logStatus.append(extractJobStatus(str));
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
                                    elif (WARNING_TYPE in TYPE_INFO and re.findall(r'\[warn\]', str)):
                                        logWarning.append(str);
                                    elif (WARN_TYPE in TYPE_INFO and re.findall(r'WARN', str)):
                                        logWARN.append(str)
                                    elif (ERROR_TYPE in TYPE_INFO and re.findall(r'ERR', str)):
                                        logError.append(str)
                                    else:
                                        raise ValueError(F'INCORRECT TYPE_INFO: {",".join(TYPE_INFO)} Please change .env file')
                            # Add formatted information to the log list
                            log.append({
                                'name': name,
                                'Warning': logWarning,
                                'WARN': logWARN,
                                'Error': logError,
                                'Status': logStatus
                            });
                        counter += 1
                        break
    return log

def extractJobStatus(str):
    match = re.search(r'JOB STATUS: (\w+)', str)
    return match.group(1).capitalize() if match else None
    
# Get information to the hostname and hostip
def getHostInfo():
    hostName = socket.gethostname()
    hostIp = urllib.request.urlopen('https://ident.me').read().decode('utf-8')
    return hostName, hostIp