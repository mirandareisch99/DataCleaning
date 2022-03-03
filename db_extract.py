import sqlite3
import pandas as pd

conn = sqlite3.connect("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/experiments_all_3.db")

header = []
c = conn.cursor()
for column in c.execute('PRAGMA table_info("experimentalRuns")'):
    header.append(column[1])

df = pd.DataFrame(columns=header)
for raw in c.execute('SELECT * FROM experimentalRuns ORDER BY id'):
    series = pd.Series(list(raw), index=df.columns)
    df = df.append(series, ignore_index=True)
df.to_csv('/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Experiments/results2.csv')