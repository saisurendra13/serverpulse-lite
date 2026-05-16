import csv, os

THRESHOLDS = {'cpu_percent': 85, 'ram_percent': 80, 'disk_percent': 90}
FILE = os.path.expanduser('~/serverpulse-lite/data/metrics.csv')

with open(FILE, 'r') as f:
    rows = list(csv.DictReader(f))

if not rows:
    print('No data yet.')
else:
    latest = rows[-1]
    print(f'Checking metrics at {latest["timestamp"]}')
    for metric, limit in THRESHOLDS.items():
        val = float(latest[metric])
        status = 'WARNING' if val > limit else 'OK'
        print(f'  {metric}: {val:.1f}%  [{status}]')
