import psycopg2
import logging
import config
import datetime

## Logging handler for PostgreSQL
#
class psqlHandler(logging.Handler):

    def connect(self):
        try:
            self._connect = psycopg2.connect(
                database   = self._database,
                host       = self._host,
                user       = self._user,
                password   = self._password,
                sslmode    = "disable")
            return True
        except:
            return False

    def __init__(self, params):

        if not params:
            raise Exception ("No database where to log...")

        self._database = params['database']
        self._host     = params['host']
        self._user     = params['user']
        self._password = params['password']

        self._connect = None

        if not self.connect():
            raise Exception ("Database connection error")

        logging.Handler.__init__(self)
        
        self._connect.cursor().execute(config.LOGGER_INITIAL)
        self._connect.commit()
        self._connect.cursor().close()

    def emit(self, record):

        # Use default formatting:
        self.format(record)

        if record.exc_info:
            record.exc_text = logging._defaultFormatter.formatException(record.exc_info)
        else:
            record.exc_text = ""

        # Insert log record:
        try:
            cur = self._connect.cursor()
        except:
            self.connect()
            cur = self._connect.cursor()

        record.__dict__['created'] =  datetime.datetime.utcfromtimestamp(record.__dict__['created']) \
                                      - datetime.timedelta(hours=4)
        
        
        cur.execute(config.LOGGER_INSERTION, record.__dict__)

        self._connect.commit()
        self._connect.cursor().close()
