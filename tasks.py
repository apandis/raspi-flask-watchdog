from app.monitor import check_all
from app.alert import notify_changes
from app.extensions import scheduler
from app.config import Config


def start_scheduler():
    scheduler.add_job(
        func=lambda: notify_changes(check_all()),
        trigger='interval',
        seconds=Config.SCHEDULER_INTERVAL,
        id='ping_check',
        replace_existing=True
    )
    scheduler.start()