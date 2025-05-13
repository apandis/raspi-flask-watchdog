from flask import Flask
from .config import Config
from .extensions import scheduler, logger
from .routes import ui_bp, api_bp
from telegram import Bot as TelegramBot


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Start background scheduler
    scheduler.start()    # Initialize Telegram Bot now that env is loaded
    import app.extensions as ext
    if app.config['TELEGRAM_TOKEN']:
        try:
            ext.bot = TelegramBot(token=app.config['TELEGRAM_TOKEN'])
        except Exception as e:
            logger.error(f"Error initializing Telegram bot: {e}")
            ext.bot = None
    else:
        logger.warning("TELEGRAM_TOKEN not provided. Telegram notifications disabled.")
        ext.bot = None

    # Register blueprints
    app.register_blueprint(ui_bp)
    app.register_blueprint(api_bp)

    return app