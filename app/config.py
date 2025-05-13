import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config:
    SCHEDULER_INTERVAL = int(os.getenv('SCHEDULER_INTERVAL', 60))
    TELEGRAM_TOKEN      = os.environ['TELEGRAM_TOKEN']
    TELEGRAM_CHAT_ID    = os.environ['TELEGRAM_CHAT_ID']
    TARGETS             = {
        'Router': os.getenv('ROUTER_IP', '192.168.1.1'),
        'Google': os.getenv('GOOGLE_IP',  '8.8.8.8'),
    }