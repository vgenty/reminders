#!/usr/bin/python

import config
from reminders import dbc
import datetime

day  = datetime.date.today().weekday()
time = datetime.datetime.now().hour + 1

event = { 'day'  : str(config.day_to_abv[day]),
          'time' : str(time) }

event['loc'] = 'hr'
HR = dbc.query(config.QUERY(event))

event['loc'] = 'll'
LL = dbc.query(config.QUERY(event))

print HR
print LL
