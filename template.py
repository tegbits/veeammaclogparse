from helper import target_date

def convertDataToText(data):
    result = ""
    for entry in data:
        result += f"Name: {entry['name']}\n"
        result += f"Warnings:\n"
        for warning in entry['Warning']:
            result += f"  {warning}\n"
        result += f"Status:\n"
        for status in entry['Status']:
            result += f"  {status}\n"
        result += "\n"
    return result
def convertDataToBody(data):
    result = ""
    for entry in data:
        name = entry.get('name', '')
        status = entry.get('Status', [])
        warnings = entry.get('Warning', [])
        warns = entry.get('WARN', [])
        errors = entry.get('Error', [])
        
        status_html = ''.join([f"<h3>{s}</h3>" for s in status])
        warnings_html = ''.join([f"<li style='padding-top: 5px;'>{w}</li>" for w in warnings])
        warns_html = ''.join([f"<li style='padding-top: 5px;'>{w}</li>" for w in warns])
        errors_html = ''.join([f"<li style='padding-top: 5px;'>{e}</li>" for e in errors])
        
        if status_html or warnings_html or warns_html or errors_html:
            result += f"""
                <html>
                    <head></head>
                    <body style="padding: 25px;">
                        <h1>Name: {name}</h1>
                        {status_html and f'<h2>Status:</h2><div>{status_html}</div>'}
                        {warnings_html and f'<h2 style="color: #ff6900;">Warnings({len(warnings)}):</h2><ul>{warnings_html}</ul>'}
                        {warns_html and f'<h2 style="color: #ff5900;">WARN({len(warns)}):</h2><ul>{warns_html}</ul>'}
                        {errors_html and f'<h2 style="color: #ff3000;">Error({len(errors)}):</h2><ul>{errors_html}</ul>'}
                    </body>
                </html>
            """
    
    return result

def convertErrorToBody(err):
    errInfo = err['msg'] if ('msg' in err) else ''
    errTitle = err['title'] if ('title' in err) else ''
    return f"""\
<html>
    <head></head>
    <body style="padding: 25px;">
        <h1 style="color: #ff6900;">Error</h1>
        {f'<h2>{errTitle}</h2>' if len(errTitle) > 1 else ''}
        {f'<div>{errInfo}</div>' if len(errInfo) > 1 else ''}
        
    </body>
</html>
"""

templateInfo = {
    'JOBSTATUS': {
        'subject': f'JOB STATUS IN {target_date}',
        'html': convertDataToBody
    },
    'ERROR': {
        'subject': f'FAIL IN PROGGRAM {target_date}',
        'html': convertErrorToBody
    }
}