import subprocess
from .config import Config
from .extensions import logger


def ping(host: str) -> bool:
    try:
        import platform
        # Windows uses -n parameter for count, Linux/macOS uses -c
        count_param = '-n' if platform.system().lower() == 'windows' else '-c'
        # Windows doesn't use -W parameter, Linux/macOS uses -W for timeout
        timeout_param = [] if platform.system().lower() == 'windows' else ['-W', '1']
        
        cmd = ['ping', count_param, '1'] + timeout_param + [host]
        subprocess.check_output(
            cmd,
            stderr=subprocess.DEVNULL
        )
        return True
    except (subprocess.CalledProcessError, Exception) as e:
        logger.debug(f"Ping failed for {host}: {e}")
        return False


def check_all() -> dict:
    status = {}
    for name, ip in Config.TARGETS.items():
        up = ping(ip)
        status[name] = up
        logger.info(f'{name} ({ip}) → {"UP" if up else "DOWN"}')
    return status