#!/usr/bin/python

import reminders
from reminders import log
from reminders.setuptable import create
from reminders.setuptable import fill
from reminders.setuptable import drop

print "\tTesting script, will create table, fill table, drop table."
log.info("Running test.py script")

log.info("Creating table.")
create.create()

log.info("Filling table.")
fill.fill()

log.info("Dropping table.")
drop.drop()

