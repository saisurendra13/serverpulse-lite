import pandas as pd, sqlite3, os
from sqlalchemy import create_engine

CSV_FILE = os.path.expanduser('~/serverpulse-lite/data/metrics.csv')
DB_FILE  = os.path.expanduser('~/serverpulse-lite/data/metrics.db')

df = pd.read_csv(CSV_FILE)
print(f'Read {len(df)} rows from CSV')

# ── SQLite (for Seema's Jupyter SQL queries) ──────────────────────
conn = sqlite3.connect(DB_FILE)
df.to_sql('metrics', conn, if_exists='replace', index=False)
conn.close()
print(f'Loaded into SQLite: {DB_FILE}')

# ── MySQL (for Seema's MySQL Workbench) ───────────────────────────
# engine = create_engine('mysql+pymysql://seema:password@localhost/serverpulse')
# df.to_sql('metrics', engine, if_exists='replace', index=False)
# print('Loaded into MySQL serverpulse.metrics')

