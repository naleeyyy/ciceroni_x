import psycopg2
import pandas as pd

df = pd.read_csv('data_unprocessed.csv')

df = df[df.id != 'Account Does Not Exist']

ids = [d for d in df['id'].to_list() if len(d) >= len('264774923225026560')]

conn = psycopg2.connect(database="ciceroni",
                        host="88.99.191.92",
                        user="postgres",
                        password="password",
                        port="5432",
                        sslmode="require")

cursor = conn.cursor()

rows = [(i, int(id_)) for i, id_ in enumerate(ids)]
query = "INSERT INTO profile(id, user_id) VALUES (%s, %s);"
cursor.executemany(query, rows)

conn.commit()
