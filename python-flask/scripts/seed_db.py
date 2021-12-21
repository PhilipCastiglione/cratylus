"""Seeds the database with initial data intended for development purposes.

Positional arguments:
environment -- the environment for which to seed data
"""
import argparse
import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument(
    "environment", choices=["development", "production"]
)
args = parser.parse_args()

dbname = os.environ.get("DB_PREFIX") + args.environment

connection = psycopg2.connect(
    dbname=dbname,
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    host=os.environ.get("DB_HOST"),
)

try:
    print("Seeding database: " + dbname)
    connection.set_session(autocommit=True)
    cursor = connection.cursor()
    sql = "INSERT INTO users (id, name, email, password) VALUES ('1', 'Test', 'test@example.com', 'test')"
    cursor.execute(
        sql
    )
except Exception as e:
    print(e)
finally:
    connection.close()
