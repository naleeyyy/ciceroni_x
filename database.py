import psycopg2
import pandas as pd
import uuid
import psycopg2.extras
from typing import Annotated
from fastapi import Depends, FastAPI
from sqlmodel import Session, SQLModel, create_engine


class Database:
    connection_string = "postgresql://postgres:password@88.99.191.92:5432/ciceroni?sslmode=require"
    connection_string_local = "postgresql://naleeyyy@localhost:5432/ciceroni"

    engine = create_engine(connection_string_local)

    @staticmethod
    def create_db_and_tables():
        SQLModel.metadata.create_all(Database.engine)

    @staticmethod
    def get_session():
        with Session(Database.engine) as session:
            yield session

    SessionDep = Annotated[Session, Depends(get_session)]


app = FastAPI()

if __name__ == '__main__':
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
