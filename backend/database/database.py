import os
import time
import psycopg
from psycopg.rows import dict_row


class Database:
    def __init__(self):
        self.database = os.getenv("DB_NAME", "db")
        self.host = os.getenv("DB_HOST", "postgres")
        self.port = int(os.getenv("DB_PORT", 5432))
        self.user = os.getenv("DB_USER", "user")
        self.password = os.getenv("DB_PASSWORD", "password")

    def _connect(self, retries=5, delay=3):
        for i in range(retries):
            try:
                conn = psycopg.connect(
                    host=self.host,
                    port=self.port,
                    dbname=self.database,
                    user=self.user,
                    password=self.password,
                    row_factory=dict_row
                )
                print("✅ Connected to PostgreSQL")
                return conn
            except Exception as e:
                print(f"⚠️ Attempt {i+1}/{retries} failed to connect to DB: {e}")
                time.sleep(delay)
        raise Exception("❌ Failed to connect to the database after multiple attempts")

    def query(self, query="SELECT * FROM location_cache;", parameters=None):
        with self._connect() as conn:
            with conn.cursor() as cur:
                if parameters:
                    cur.execute(query, parameters)
                else:
                    cur.execute(query)

                if query.strip().upper().startswith("SELECT"):
                    return cur.fetchall()
                else:
                    return []

    def createTables(self, purge=False, data_path='backend/database/'):
        if purge:
            self.query("DROP TABLE IF EXISTS location_cache CASCADE;")

        sql_file = 'create_tables/location_cache.sql'
        complete_path = data_path + sql_file

        with open(complete_path, 'r') as f:
            sql_query = f.read()
            self.query(sql_query)