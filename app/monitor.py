import subprocess
from .config import Config
from .extensions import logger


def ping(host: str) -> bool:
    try:
        subprocess.check_output(
            ['ping', '-c', '1', '-W', '1', host],
            stderr=subprocess.DEVNULL
        )
        return True
    except subprocess.CalledProcessError:
        return False


def check_all() -> dict:
    status = {}
    for name, ip in Config.TARGETS.items():
        up = ping(ip)
        status[name] = up
        logger.info(f'{name} ({ip}) → {"UP" if up else "DOWN"}')
    return status