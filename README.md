# ServerPulse Lite — Real-Time Server Health Monitor

> A production-style system monitoring project built on Raspberry Pi.  
> **Sai Surendra Munagala** (Infrastructure) · **Shaik Seema Kousar** (Analytics & Dashboard)

---

## What This Project Does

ServerPulse Lite collects live CPU, RAM, and disk metrics from a **Raspberry Pi Linux server** every minute, stores them in a structured CSV and SQLite database, automatically pushes to GitHub every hour, and feeds a Power BI analytics dashboard.

```
Raspberry Pi                    GitHub                    Seema's Laptop
─────────────────────     ──────────────────     ──────────────────────────
collect.py (every 1min) → metrics.csv/metrics.db → git pull → Jupyter + Power BI
alert.py   (every 5min)   (auto-pushed hourly)
load_to_db.py (every 1hr)
```

---

## Project Structure

```
serverpulse-lite/
├── README.md
├── requirements.txt
├── .gitignore
│
├── scripts/                  ← Sai's work (runs on Raspberry Pi)
│   ├── collect.py            ← Python metrics collector (psutil, every 60s)
│   ├── load_to_db.py         ← CSV → SQLite loader (runs hourly via cron)
│   ├── check_health.sh       ← Bash health checker (CPU/RAM/disk via top/free/df)
│   └── alert.py              ← Threshold alert checker (CPU>85%, RAM>80%, Disk>90%)
│
├── data/                     ← Auto-updated by Pi cron every hour
│   ├── metrics.csv           ← Live server metrics (3000+ rows and growing)
│   └── metrics.db            ← SQLite database
│
├── analysis/                 ← Seema's work (coming soon)
│   └── seema_analysis.ipynb
│
└── powerbi/                  ← Seema's work (coming soon)
    └── serverpulse_dashboard.pbix
```

---

## Tech Stack

| Layer | Tools |
|---|---|
| Server | Raspberry Pi 4 · Raspberry Pi OS (Linux) |
| Collection | Python 3 · psutil · Bash · cron |
| Storage | CSV · SQLite |
| Monitoring | Netdata (live dashboard at `http://192.168.1.31:19999`) |
| Analytics | Python · Pandas · Jupyter Notebook · SQL |
| Dashboard | Power BI Desktop · DAX |
| Collaboration | GitHub |

**Cost: ₹0 — 100% free tools**

---

## Sai's Side — Running on Raspberry Pi

### Prerequisites

```bash
pip3 install psutil pandas sqlalchemy
```

### Scripts

| Script | What it does | How to run |
|---|---|---|
| `collect.py` | Collects CPU/RAM/disk every 60s → writes to `metrics.csv` | Via cron (see below) |
| `check_health.sh` | Bash version — appends raw row to `metrics.log` | Via cron |
| `alert.py` | Checks latest row, logs WARNING if threshold exceeded | Via cron every 5min |
| `load_to_db.py` | Reads CSV → loads all rows into `metrics.db` (SQLite) | Via cron every hour |

### Cron Setup (Pi)

```bash
crontab -e
```

Paste:

```
* * * * * /usr/bin/python3 /home/seema/serverpulse-lite/scripts/collect.py >> /home/seema/cron.log 2>&1
*/5 * * * * /usr/bin/python3 /home/seema/serverpulse-lite/scripts/alert.py >> /home/seema/alerts.log 2>&1
0 * * * * /usr/bin/python3 /home/seema/serverpulse-lite/scripts/load_to_db.py >> /home/seema/cron.log 2>&1
5 * * * * cd /home/seema/serverpulse-lite && git pull origin main --quiet && git add data/metrics.csv data/metrics.db && git commit -m "Auto: hourly metrics $(date '+\%Y-\%m-\%d \%H:\%M')" && git push origin main >> /home/seema/cron.log 2>&1
@reboot /usr/bin/python3 /home/seema/serverpulse-lite/scripts/collect.py &
```

### Live Monitoring (Netdata)

Netdata is installed and running on the Pi:

- **From Pi browser:** `http://localhost:19999`
- **From any device on same network:** `http://192.168.1.31:19999`

Shows CPU, RAM, disk, network — live updates every 3 seconds.

---

## Current Data Stats

| Metric | Value |
|---|---|
| Rows collected | 3,026+ (growing every minute) |
| Collection frequency | Every 60 seconds |
| DB last updated | Hourly via cron |
| GitHub push | Hourly (auto) |
| Avg CPU % | ~2–5% (Pi idle) |
| Avg RAM % | ~58–61% |
| Disk usage | ~22.8% |

---

## Seema's Side — Analytics & Dashboard

> **Status: Coming soon**

Seema will add:
- `analysis/seema_analysis.ipynb` — Pandas EDA, SQL queries, Excel export
- `powerbi/serverpulse_dashboard.pbix` — 3-page Power BI dashboard

**Dashboard URL:** *(will be added after Seema publishes to Power BI Service)*

### How Seema gets data

```bash
cd ~/Documents/serverpulse-lite
git pull origin main
# Now open Jupyter — metrics.csv and metrics.db are fresh
---

## Sample Data Format

```
timestamp,cpu_percent,ram_percent,disk_percent
2026-05-16 12:18:25,0.8,58.7,22.8
2026-05-16 12:18:26,0.8,58.8,22.8
2026-05-16 12:18:27,0.8,58.9,22.8
---

## Authors

| Name | Role | GitHub |
|---|---|---|
| Sai Surendra Munagala | Infrastructure & Backend | [@saisurendra13](https://github.com/saisurendra13) |
| Shaik Seema Kousar | Analytics & Dashboard | *(link to be added)* |
