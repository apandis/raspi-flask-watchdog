from apscheduler.schedulers.background import BackgroundScheduler
from telegram import Bot
import logging
from logging.handlers import RotatingFileHandler

# Scheduler singleton
scheduler = BackgroundScheduler()

# Telegram bot singleton; token set in create_app()
bot = Bot(token=None)

# Rotating file logger
handler = RotatingFileHandler('watchdog.log', maxBytes=2**20, backupCount=3)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)