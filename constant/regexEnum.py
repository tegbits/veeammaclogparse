from datetime import datetime
import re
pattern_date = re.escape(datetime.now().strftime('%Y%m%d'))
pattern_dir = r'Session_\d{8}_\d{6}_'