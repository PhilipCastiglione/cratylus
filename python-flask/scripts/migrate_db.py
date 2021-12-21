"""Runs db migrations for the given environment.

Positional arguments:
environment -- the environment for which to run migrations
"""
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument(
    "environment", choices=["development", "test", "production"]
)
args = parser.parse_args()
env_name = args.environment

os.system(
    "alembic -c ./src/data_model/alembic.ini -x environment={} upgrade head".format(
        env_name
    )
)
