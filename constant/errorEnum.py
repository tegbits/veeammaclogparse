DIRECTORY_NOT_FOUND = {
    'title': 'Log Folder with current date not found',
    'msg': '''<h4>Here are the next steps:</h4>

<p>1. Verify if you have placed the file correctly (this will determine if the dermatology program can locate it).</p>

<p>2. Check if there are logs for the specified time (the issue might be with the program generating the logs).</p>

<p>3. Compare the log creation time with when you run the program.</p>

<p>4. Ensure that folders are being created in the correct format, which should include the date in 'YYYYMMDD' format (WITHOUT HYPHENS OR SPACES).</p>

<p>5. If none of the above steps help, please seek assistance.</p>
'''
}
FILE_NOT_FOUND = {
    'title': 'Don`t find file Job.log',
    'msg': '''<h4>Here are the next steps:</h4>
    
<p>1. Check the program responsible for date creation to ensure it's generating files correctly; if needed, adjust the name to "Job.log".</p>
<p>2. Compare the log creation time with when you launch the program.</p>

<p>3. Verify if the program is accessing the correct directory for saving logs.</p>

<p>4. Confirm that the program has the necessary permissions to create and modify files.</p>

<p>5. If none of these steps resolve the issue, seek assistance.</p>
'''
}