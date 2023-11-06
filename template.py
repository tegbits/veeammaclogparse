from helper import getHostInfo, getBackupTime
from constant.config.configEnum import TYPE_INFO, COMPANY_NAME
from constant.informationTypeEnum import FULL_TYPE, WARNING_TYPE, WARN_TYPE , ERROR_TYPE, ALL_TYPE

hostInfo = getHostInfo()

backupTime = getBackupTime()


# Converts data to HTML format for the email body
def convertDataToBody(data):
    result = ""
    name = data.get('name', '')
    status = data.get('Status', [])
    warnings = data.get('Warning', [])
    warns = data.get('WARN', [])
    errors = data.get('Error', [])
        
        # Generate HTML content for status, warnings, warns, and errors
    status_html = ''.join([f"{s}" for s in status])
    warnings_html = ''.join([f"<li style='padding-top: 5px;'>{w}</li>" for w in warnings])
    warns_html = ''.join([f"<li style='padding-top: 5px;'>{w}</li>" for w in warns])
    errors_html = ''.join([f"<li style='padding-top: 5px;'>{e}</li>" for e in errors])
    if(not(all(e in ALL_TYPE for e in TYPE_INFO))):
        raise ValueError('Incorect TYPE_INFO please change .env')
    isWarning = any(s in TYPE_INFO for s in [FULL_TYPE, WARNING_TYPE]) and warnings_html
    isWarn = any(s in TYPE_INFO for s in [FULL_TYPE, WARN_TYPE]) and warns_html
    isError = any(s in TYPE_INFO for s in [FULL_TYPE, ERROR_TYPE]) and errors_html
    result += f"""
                <html>
                    <head></head>
                    <body>
                        <h3>Device: {hostInfo[0]}</h3>
                        <h3>Status: {status_html}</h3>
                        <h3>Job: Daily Backup</h3>
                        <h3>Company: {COMPANY_NAME}</h3>
                        <h3>Warning: {bool(warnings_html or warns_html)}</h3>
                        <h3>Error: {bool(errors_html)}</h3>
                        <h3>Backup time: {backupTime}</h3>
                        <h3>Detail Information:</h3>
                        <div style="padding: 25px;">
                            <h3>Name: {name}</h3>
                            {f'<h4 style="color: #ff6900;">Warnings({len(warnings)}):</h4><ul>{warnings_html}</ul>' if isWarning else ''}
                            {f'<h4 style="color: #ff5900;">WARN({len(warns)}):</h4><ul>{warns_html}</ul>' if isWarn else ''}
                            {f'<h4 style="color: #ff3000;">Error({len(errors)}):</h4><ul>{errors_html}</ul>' if isError else ''}
                        </div>
                    </body>
                </html>
            """
            
    return result

# Converts error information to HTML format for the email body
def convertErrorToBody(err):
    errInfo = err.get('msg','')
    errTitle = err.get('title','')
    return f"""\
<html>
    <head></head>
    <h3>Device Name: {hostInfo[0]}</h3>
    <h3>Status: Failure</h3>
    <h3>Job Name: Daily Backup</h3>
    <h3>Company: {COMPANY_NAME}</h2>
    <h3>Error: True</h3>
    <h3>Warning: True</h3>
    <h3>Backup time: {backupTime}</h3>
    <body style="padding: 25px;">
        {errInfo and f'<h3 style="color: #ff5900;">{errTitle}</h3>'}
        {errInfo and f'<div>{errInfo}</div>'}
    </body>
</html>
"""

def getTitle (title):
    return f'Backup Report Veeam MacAgent: {title}'

# Dictionary mapping template types to their corresponding subject and HTML generation functions
templateInfo = {
    'JOBSTATUS': {
        'subject': getTitle,
        'html': convertDataToBody
    },
    'ERROR': {
        'subject': f'Backup Report Veeam MacAgent: FAIL IN PROGRAM',
        'html': convertErrorToBody
    }
}


