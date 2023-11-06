from constant.constansEnum import TARGET_DATE
import re
def PATTERN_DATE(time = TARGET_DATE):
    return re.escape(time)
PATTERN_DIR = r'Session_\d{8}_\d{6}_'