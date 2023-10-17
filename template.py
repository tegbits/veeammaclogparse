from helper import getHostInfo
from constant.config.configEnum import TYPE_INFO


hostInfo = getHostInfo()


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
    # Combine all HTML content
    result += f"""
                <html>
                    <head></head>
                    <body style="padding: 25px;">
                        <h2>Device: {hostInfo[0]}</h2>
                        {status_html and f'<h2>Status: {status_html}</h2>'}
                        <h2>Job: Daily Backup</h2>
                        '<h2>Detail Information:</h2>'
                        <h3>Name: {name}</h3>
                        {warnings_html and f'<h4 style="color: #ff6900;">Warnings({len(warnings)}):</h4><ul>{warnings_html}</ul>'}
                        {warns_html and f'<h4 style="color: #ff5900;">WARN({len(warns)}):</h4><ul>{warns_html}</ul>'}
                        {errors_html and f'<h4 style="color: #ff3000;">Error({len(errors)}):</h4><ul>{errors_html}</ul>'}
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
    <h3>Device: {hostInfo[0]}</h3>
    <h3>Status: Failure</h3>
    <h3>Job: Daily Backup</h3>
    <body style="padding: 25px;">
        {errInfo and f'<h3 style="color: #ff5900;">{errTitle}</h3>'}
        {errInfo and f'<div>{errInfo}</div>'}
    </body>
</html>
"""

def getTitle (title):
    return f'Veeam MacAgent Backup Report: {title}'

# Dictionary mapping template types to their corresponding subject and HTML generation functions
templateInfo = {
    'JOBSTATUS': {
        'subject': getTitle,
        'html': convertDataToBody
    },
    'ERROR': {
        'subject': f'Veeam MacAgent Backup Report: FAIL IN PROGRAM',
        'html': convertErrorToBody
    }
}


