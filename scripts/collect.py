# Content:
import psutil, csv, datetime, time, os

FILE    = os.path.expanduser('~/serverpulse-lite/data/metrics.csv')
HEADERS = ['timestamp', 'cpu_percent', 'ram_percent', 'disk_percent']

# Write header ONCE when file does not exist
if not os.path.exists(FILE):
    with open(FILE, 'w', newline='') as f:
        csv.writer(f).writerow(HEADERS)

# Collect one row per minute forever
while True:
    row = [
        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        psutil.cpu_percent(interval=1),
        psutil.virtual_memory().percent,
        psutil.disk_usage('/').percent
    ]
    with open(FILE, 'a', newline='') as f:
        csv.writer(f).writerow(row)
    time.sleep(60)
