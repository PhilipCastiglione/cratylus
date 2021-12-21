"""Generates db migrations using alembic.
"""
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("message", help="the migration message")
args = parser.parse_args()
message = args.message

os.system(
    'alembic -c ./src/data_model/alembic.ini -x environment=development revision --autogenerate -m "{}"'.format(
        message
    )
)
