import os

#################
# PROGRAM CONFIG
#
day_to_abv = { 0 : "M",
               1 : "T",
               2 : "W",
               3 : "Th",
               4 : "F" ,
               5 : "Sa",
               6 : "Su"}

# Who is sending the emails
email_sender = 'preceptor@phys.columbia.edu'
email_cc     = ['']
email_bcc    = ['akonmfd@gmail.com','vgenty@nevis.columbia.edu']

# Location of message.txt
message = "/home/vgenty/git/reminders_beta/message.txt"

# Location of emails
emails = "/home/vgenty/git/reminders_beta/emails.csv"

# Location of emails xls
emails_xls = "/home/vgenty/git/reminders_beta/emails.xls"

email_user = #UNI
email_pass = #UNIPASS

##################
# DATABASE CONFIG
#
host  = 'localhost'
user  = os.environ['USER']
db    = 'procdb'
passw = ''

# SQL statments
TABLE_NAME = "AHOAHO"

CREATE_TABLE = """CREATE TABLE IF NOT EXISTS %s (num serial PRIMARY KEY, 
                                   first_name varchar, 
                                   last_name varchar, 
                                   HR jsonb, 
                                   LL jsonb, 
                                   email varchar, 
                                   area_code int, 
                                   phone int, 
                                   optin boolean);""" % TABLE_NAME

DROP_TABLE = """DROP TABLE IF EXISTS %s;""" % TABLE_NAME

#The following need to be w/o line breaks...
FILL  = """INSERT INTO """ + TABLE_NAME + """(first_name,last_name, HR, LL, email, area_code, phone, optin) 
           VALUES (%(first_name)s,%(last_name)s,%(HR)s,%(LL)s,%(email)s,%(area_code)s,%(phone)s,%(optin)s);"""

def QUERY(e):
    return """SELECT first_name, last_name, email FROM """ + TABLE_NAME + """ WHERE %(loc)s @> '{"%(day)s":["%(time)s"]}' AND optin;""" % e


#Logger
    
LOGGER_INITIAL = """CREATE TABLE IF NOT EXISTS log(
                        Created timestamp,
                        Name text,
                        LogLevel int,
                        LogLevelName text,
                        Message text,
                        Module text,
                        FuncName text,
                        LineNo int,
                        Exception text
                    )"""


LOGGER_INSERTION = """INSERT INTO log(
                            Created,
                            Name,
                            LogLevel,
                            LogLevelName,
                            Message,
                            Module,
                            FuncName,
                            LineNo,
                            Exception)
                    VALUES (
                            %(created)s,
                            %(name)s,
                            %(levelno)s,
                            %(levelname)s,
                            %(msg)s,
                            %(module)s,
                            %(funcName)s,
                            %(lineno)s,
                            %(exc_text)s
                             );"""

