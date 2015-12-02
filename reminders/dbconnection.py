import psycopg2
import config
import sys

class dbConnection:
    
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

    def __init__(self, params, log):    
        self.log = log

        if not params:
            self.log.exception("No database found.")
            raise Exception ("No database found.")

        self._database = params['database']
        self._host     = params['host']
        self._user     = params['user']
        self._password = params['password']

        self._connect = None

        if not self.connect():
            self.log.exception("Database connection error.")
            raise Exception ("Database connection error.")


    def query(self, sql, values=None):

        # Open up cursor
        try:
            cur = self._connect.cursor()
        except:
            self.connect()
            cur = self._connect.cursor()

        q = r = f = None

        if values is not None:
            try:
                r = cur.execute(sql,values)
            except:
                self.log.exception("Unable to execute sql command, aborted!")
                sys.exit(1)
        else:
            try:
                r = cur.execute(sql)
            except:
                self.log.exception("Unable to execute sql command, aborted!")
                sys.exit(1)

        q = cur.query
        try:
            f = cur.fetchone()
        except:
            f = None

        self.log.debug("Queried database with:\n%s" % q)
        
        self._connect.commit()
        self._connect.cursor().close()

        return f
    
