#!/usr/bin/python

import reminders
from reminders import log
from reminders.setuptable import create
from reminders.setuptable import fill
from reminders.setuptable import drop

print "\tSetting up table, will drop TABLE_NAME if it exists"
log.info("Running setup.py script")

log.info("Dropping table.")
drop.drop()

log.info("Creating table.")
create.create()

log.info("Filling table with student data.")
fill.fill()



