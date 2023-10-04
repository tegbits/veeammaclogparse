from constant.constansEnum import TARGET_DATE
import re
PATTERN_DATE = re.escape(TARGET_DATE)
PATTERN_DIR = r'Session_\d{8}_\d{6}_'