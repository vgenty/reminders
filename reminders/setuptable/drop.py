import config
from reminders import dbc

def drop():
    dbc.query(config.DROP_TABLE)

