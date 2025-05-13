from apscheduler.schedulers.background import BackgroundScheduler
import logging
from logging.handlers import RotatingFileHandler

# Scheduler singleton
scheduler = BackgroundScheduler()

# Telegram Bot placeholder; real instance set in create_app()
bot = None

# Rotating file logger
handler = RotatingFileHandler('watchdog.log', maxBytes=2**20, backupCount=3)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)