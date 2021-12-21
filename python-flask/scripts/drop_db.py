"""Drops an application Postgresql database for the given environment.

Positional arguments:
environment -- the environment for which to drop the database
"""
import argparse
import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument(
    "environment", choices=["development", "test", "production"]
)
args = parser.parse_args()

dbname = os.environ.get("DB_PREFIX") + args.environment

connection = psycopg2.connect(
    dbname="postgres",
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    host=os.environ.get("DB_HOST"),
)

try:
    print("Dropping database: " + dbname)
    connection.set_session(autocommit=True)
    cursor = connection.cursor()
    cursor.execute("DROP DATABASE IF EXISTS " + dbname)
except Exception as e:
    print(e)
finally:
    connection.close()
