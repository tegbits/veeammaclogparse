import os,re
from datetime import datetime

target_date = datetime.now().strftime('%Y%m%d')

from constant.regexEnum import pattern_dir, pattern_date

def getDirectory(arr, newPath = False):
    content = []
    print(newPath)
    if (not(newPath)):
        for file in os.scandir():
            if (os.path.isdir(file)):
                if (not(re.findall(pattern_dir, file.name))):
                    content.append(file.name)
                if (re.findall(pattern_date, file.name)):
                    arr.append(os.path.join(newPath, file.name))
                    return;
        newPath = './'
    else:
        for file in os.scandir(newPath):
            if (os.path.isdir(file)):
                if (not(re.findall(pattern_dir, file.name))):
                    content.append(file.name)
                if (re.findall(pattern_date, file.name)):
                    arr.append(os.path.join(newPath, file.name))
                    return;
    if len(content):
        for path in content:
            getDirectory(arr, os.path.join(newPath, path))
        return
    return;
def getLogInfo (arr):
    log = []
    for currentPath in arr:
        with os.scandir(currentPath) as files:
            for file in files:
                if (file.name.capitalize() == 'Job.log'):
                    with open(os.path.join(currentPath, file.name), 'r') as fileData:
                        logInfo = fileData.readlines()
                        name = currentPath.split('/')[-2]
                        logWarning = []
                        logWARN = []
                        logError = []
                        logStatus = [];
                        for str in logInfo:
                            if (re.findall(r'\[warn\]', str)):
                                logWarning.append(str);
                            if (re.findall(r'JOB STATUS', str)):
                                logStatus.append(str);
                            if (re.findall(r'WARN', str)):
                                logWARN.append(str)
                            if (re.findall(r'ERR', str)):
                                logError.append(str)
                        log.append({
                            'name': name,
                            'Warning': logWarning,
                            'WARN': logWARN,
                            'Error': logError,
                            'Status': logStatus
                        });
                        break
    return log