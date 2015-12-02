import datetime
import sys
import config

from reminders import dbc
from reminders import log

from reminders.emailer import send_mail as sm

def main():
    log.info("PROGRAM START")
    
    day  = config.day_to_abv[datetime.date.today().weekday()]
    time = datetime.datetime.now().hour + 1
        
    event = { 'day'  : str(day),
              'time' : str(time) }

    log.debug("Ask database for HR for day: %(day)s and time %(time)s" % event)
    event['loc'] = 'hr'
    HR = dbc.query(config.QUERY(event))

    log.debug("Ask database for LL for day: %(day)s and time %(time)s" % event)
    event['loc'] = 'll'
    LL = dbc.query(config.QUERY(event))

    if HR is not None:
        sm.send_mail(HR,"Help Room")
    if LL is not None:
        sm.send_mail(LL,"Lab Library")

    log.info("PROGRAM END")
    sys.exit(0)
