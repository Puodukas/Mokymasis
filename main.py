import sqlite3
import pandas as pd
tele = pd.read_csv("https://raw.githubusercontent.com/nikipaj1/teaching/main/Analytics/telecom_churn.csv")
conn = sqlite3.connect('task1.db')
tele.to_sql('telecom',conn,if_exists='replace',index=False)
conn.close()
