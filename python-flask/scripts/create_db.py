"""Creates an application Postgresql database for the given environment.

Positional arguments:
environment -- the environment for which to create the database
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

created_database = False
try:
    print("Creating database: " + dbname)
    connection.set_session(autocommit=True)
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE " + dbname)
    created_database = True
except Exception as e:
    print(e)
finally:
    connection.close()
