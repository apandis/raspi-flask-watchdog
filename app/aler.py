from .config import Config
from .extensions import bot, logger

_last_status = {}

def notify_changes(current: dict):
    global _last_status
    for name, up in current.items():
        prev = _last_status.get(name)
        # Initialize or skip if status unchanged
        if prev is None or up == prev:
            _last_status[name] = up
            continue
        # Send Telegram alert on change
        msg = f'⚠️ *{name}* is now {"ONLINE" if up else "OFFLINE"}'
        try:
            bot.send_message(
                chat_id=Config.TELEGRAM_CHAT_ID,
                text=msg,
                parse_mode='Markdown'
            )
            logger.info(f'Alert sent: {msg}')
        except Exception as e:
            logger.error(f'Telegram error: {e}')
        _last_status[name] = up