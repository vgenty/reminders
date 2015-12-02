import config
import sys

from reminders.emailer import emailer
from reminders import log

def send_mail(who,what):
    #ok we need person object but for now ok who cares
    log.info("With who: %s %s, doing what: %s" % (who[0],who[1],what))
    
    log.debug("Opening message file")
    myfile = None
    try :
        myfile = open(config.message, "r")
    except IOError:
        log.exception("IO error in opening " % config.message)
        sys.exit(1)

    data = myfile.read()
    log.debug("Closing message file")
    myfile.close()

    data = data.replace("NAME", who[0] + " " + who[1])
    data = data.replace("SOMETHING",what)
    
    to   = [who[2]]
    #to   = ['vgenty@nevis.columbia.edu'] # for debugging
    cc   = config.email_cc
    bcc  = config.email_bcc
    
    e = emailer.Email(to,cc,bcc,log)  
    e.message(data)
    e.send(what + " in 30 minutes")
    log.info("Sent out message to %s" % to )
