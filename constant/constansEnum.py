import os
from datetime import datetime, timedelta

TARGET_DATE = datetime.now().strftime('%Y%m%d')
TARGET_TOMORROW_DATE = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')

TARGET_FILE = 'Job.log'

DEFAULT_START_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), '..'
)

