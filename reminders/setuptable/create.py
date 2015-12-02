import config
from reminders import dbc

def create():
    dbc.query(config.CREATE_TABLE)
