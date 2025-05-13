from flask import Flask
from .config import Config
from .extensions import bot
from .routes import ui_bp, api_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Telegram bot
    bot.token = app.config['TELEGRAM_TOKEN']

    # Register blueprints
    app.register_blueprint(ui_bp)
    app.register_blueprint(api_bp)

    return app