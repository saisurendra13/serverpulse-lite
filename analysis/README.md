# 📌 Project Overview

Server performance resource monitoring is a real-time server monitoring analytics project built using Python, Pandas, SQL, Jupyter Notebook, and Power BI.

This notebook focuses on:

- Data cleaning
- Exploratory Data Analysis (EDA)
- SQL-based querying
- Resource usage analysis

using live server monitoring data collected from a Raspberry Pi Linux server.

The dataset contains real-time:

- CPU usage
- RAM usage
- Disk usage

captured continuously over multiple days.  
The cleaned and processed dataset is later used for Power BI dashboard visualization and performance analysis.

---

# 🎯 Project Results

| Metric | Raw Dataset | Cleaned Dataset |
|---|---|---|
| Total Rows | 115,729 | 66,870 |
| Avg CPU Usage | 4.51% | 3.99% |
| Avg RAM Usage | 85.12% | 83.15% |
| Avg Disk Usage | 25.06% | 25.08% |
| Max CPU Usage | 94.2% | 92.9% |
| Max RAM Usage | 98.4% | 98.2% |

---

# 📂 Dataset — `metrics.csv`

The dataset is generated automatically from the live server monitoring system every minute.

## Dataset Columns

| Column | Data Type | Description |
|---|---|---|
| `timestamp` | DateTime | Date and time of the reading |
| `cpu_percent` | Float | CPU utilization percentage |
| `ram_percent` | Float | RAM utilization percentage |
| `disk_percent` | Float | Disk utilization percentage |

### Sample Format

```csv
timestamp,cpu_percent,ram_percent,disk_percent
2026-05-18 10:00:00,5.2,84.1,25.3
2026-05-18 10:01:00,7.4,84.3,25.3
```

---

# 🧹 Data Cleaning Process

The raw monitoring dataset contained invalid readings, duplicate timestamps, and noisy records.

The following cleaning steps were performed to improve data quality and ensure accurate analysis.

---

# Step 1 — Load Dataset

```python
df = pd.read_csv('data/metrics.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])
```

Purpose:
- Read monitoring dataset
- Convert timestamp column into proper DateTime format

---

# Step 2 — Remove Invalid Readings

```python
df = df[(df['cpu_percent'] > 0) & (df['ram_percent'] > 0)]
```

Purpose:
- Remove corrupted rows
- Exclude zero CPU and RAM values
- Improve dataset reliability

---

# Step 3 — Remove Duplicate Records

```python
df = df.drop_duplicates(subset='timestamp')
```

Purpose:
- Remove repeated timestamp entries
- Ensure each monitoring record is unique

---

# Step 4 — Export Cleaned Dataset

```python
df.to_csv('cleaned_metrics.csv', index=False)
```

Purpose:
- Save cleaned dataset
- Use for SQL analysis and Power BI dashboarding

---

# 📊 Data Cleaning Summary

| Step | Action | Rows |
|---|---|---|
| 1 | Raw dataset loaded | 115,729 |
| 2 | Invalid readings removed | — |
| 3 | Duplicate timestamps removed | — |
| 4 | ✅ Clean dataset exported | 66,870 |

---

# 🔍 SQL Analysis Performed

The cleaned dataset was loaded into SQLite for SQL-based analysis and querying.

---

# Query 1 — Average CPU Usage Per Hour

Purpose:
- Analyze hourly CPU behavior
- Identify peak usage periods
- Understand server load patterns

---

# Query 2 — Top 10 High CPU Events

Condition:

```sql
cpu_percent > 80
```

Purpose:
- Detect abnormal CPU spikes
- Identify critical resource events
- Support troubleshooting and monitoring

---

# Query 3 — Daily Aggregated Summary

This query generated:

- Total readings per day
- Average CPU usage
- Maximum disk usage

---

# 📅 Daily Monitoring Summary

| Date | Total Readings | Avg CPU % | Max Disk % |
|---|---|---|---|
| 2026-05-18 | 30,524 | 4.7% | 25.9% |
| 2026-05-17 | 53,726 | 4.9% | 25.7% |
| 2026-05-16 | 30,974 | 3.7% | 25.5% |
| 2026-05-15 | 21 | 0.5% | 22.8% |

---

# 📈 Exploratory Data Analysis (EDA)

The notebook includes multiple visualizations and trend analyses to study server performance over time.

## Analysis Includes

- CPU usage trends
- RAM consumption patterns
- Disk usage monitoring
- High CPU spike detection
- Daily resource summaries
- Peak utilization analysis

---

# 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| Python 3.11 | Core programming language |
| Pandas | Data cleaning and analysis |
| Matplotlib | Data visualization |
| SQLite3 | SQL querying |
| Jupyter Notebook | Interactive analytics environment |
| GitHub | Version control and collaboration |

---

# 📈 Key Insights

| Insight | Observation |
|---|---|
| 🔴 RAM Critical | Average RAM usage remained above 83% and peaked at 98.2% |
| ⚠️ CPU Spikes | Multiple CPU spikes above 80% detected on May 18 |
| ✅ Disk Stable | Disk utilization remained stable between 22–26% |
| 🕙 Peak Hour | Highest CPU utilization observed around 10 PM |
| 📅 Busiest Day | May 17 generated the highest number of monitoring records |
| 🧹 Data Quality | Removed 48,859 invalid and duplicate rows during cleaning |

---

# ✅ Conclusion

This project demonstrates a complete real-time monitoring and analytics workflow using Linux monitoring, Python automation, SQL analysis, and Power BI visualization.

The notebook successfully:

- Cleaned large-scale monitoring data
- Identified critical server resource patterns
- Performed SQL-based performance analysis
- Generated actionable insights from live infrastructure metrics

The cleaned dataset and insights are used to support real-time dashboarding and server performance monitoring.
