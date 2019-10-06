"""
File for storing various config info, such as
database credentials.
"""
from os import getenv
from psycopg2 import connect
from sqlalchemy import create_engine
from requests import get


# Define credentials using environment vars
pghost = getenv('PG_HOST')
pguser = getenv('PG_USER')
pgpass = getenv('PG_PASS')
pgport = getenv('PG_PORT')

db_connection = connect(database='{{cookiecutter.database}}', host=pghost, user=pguser, password=pgpass)

# Create a SQLAlchemy engine to write CSV data to the db
db_engine = create_engine(f"postgresql+psycopg2://{pguser}:{pgpass}@{pghost}:{pgport}/{{cookiecutter.database}}")

endpoint = get('{{cookiecutter.api_endpoint}}')
api_json = endpoint.json()