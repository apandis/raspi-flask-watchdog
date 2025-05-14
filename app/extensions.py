from apscheduler.schedulers.background import BackgroundScheduler
import logging
from logging.handlers import RotatingFileHandler

# Scheduler singleton
scheduler = BackgroundScheduler()

# Telegram Bot placeholder; real instance set in create_app()
bot = None

# Rotating file logger
import os
log_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'watchdog.log'))
handler = RotatingFileHandler(log_file, maxBytes=2**20, backupCount=3)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)