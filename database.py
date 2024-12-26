import psycopg2
import pandas as pd
import uuid
import psycopg2.extras

psycopg2.extras.register_uuid()

df = pd.read_csv('ids.csv')

ids = df["user_id"].to_list()

conn = psycopg2.connect(database="ciceroni",
                        host="88.99.191.92",
                        user="postgres",
                        password="password",
                        port="5432",
                        sslmode="require")

cursor = conn.cursor()

rows = [(uuid.uuid4(), id_) for id_ in ids]
query = "INSERT INTO profile(id, user_id) VALUES (%s, %s);"
cursor.executemany(query, rows)

conn.commit()
