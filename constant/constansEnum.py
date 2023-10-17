import os
from datetime import datetime

TARGET_DATE = datetime.now().strftime('%Y%m%d')

TARGET_FILE = 'Job.log'

DEFAULT_START_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), '..'
)

