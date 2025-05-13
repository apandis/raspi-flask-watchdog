# Network Watchdog

A lightweight Flask-based network monitor for Raspberry Pi Zero v1. It periodically pings configured hosts, exposes a web UI & JSON API, and sends Telegram alerts on status changes.

## Features

- **Periodic Health Checks**: Uses APScheduler for background ping jobs.
- **Web Dashboard**: View real-time status at `/`.
- **JSON API**: Fetch host status at `/api/status`.
- **Telegram Alerts**: Notifies on up/down transitions.
- **Daemonized**: Runs as a systemd service, auto-restarts on failure.
- **Logging**: Rotating logs in `watchdog.log`.

## Prerequisites

- Raspberry Pi Zero v1 (or similar)
- Python 3.7+
- A Telegram bot token and chat ID

## Installation

1. **System packages**

   ```bash
   sudo apt update
   sudo apt install -y python3-venv python3-pip
   ```

2. **Clone & setup**

   ```bash
   git clone https://github.com/apandis/raspi-flask-watchdog.git
   cd raspi-flask-watchdog
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure**

Copy `.env.example` to `.env` and populate:

     ```ini
     TELEGRAM_TOKEN=your_bot_token
     TELEGRAM_CHAT_ID=your_chat_id
     SCHEDULER_INTERVAL=60           # seconds between checks
     ROUTER_IP=192.168.1.1           # example target
     GOOGLE_IP=8.8.8.8
     ```

1. **Install service**

   ```bash
   sudo cp watchdog.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable watchdog
   sudo systemctl start watchdog
   ```

## Usage

- **Web UI**: `http://<raspberry-pi-ip>:5000`
- **API**: `http://<raspberry-pi-ip>:5000/api/status`

### Customizing Targets

Edit `app/config.py` or set additional environment variables:

```ini
# In .env
SERVER1_IP=10.0.0.2
SERVER2_IP=example.com
```

## Logs & Troubleshooting

- **Log file**: `watchdog.log` in project root. Rotates at 1 MB, keeps 3 backups.
- **Service status**:

  ```bash
  sudo systemctl status watchdog
  sudo journalctl -u watchdog -f
  ```

## Development

- Run without service:

  ```bash
  source venv/bin/activate
  python run.py
  ```
