import config

from dbconnection import dbConnection
from psqlhandler  import psqlHandler

import logging

connection = {'host'     : config.host,
              'user'     : config.user,
              'password' : config.passw,
              'database' : config.db}

# Create handler which logger will use for postres insertion (separate cursor)
myh = psqlHandler(connection)

log = logging.getLogger("TEST")
log.setLevel(logging.DEBUG)
log.addHandler(myh)

# DB connection for general query
dbc = dbConnection(connection,log)

