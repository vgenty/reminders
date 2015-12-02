import config

from reminders       import dbc
from psycopg2.extras import Json
from ast             import literal_eval as le

import pandas as pd

def fill():
    data = pd.read_excel(config.emails_xls).fillna("")

    for person in data.iterrows():
        person = person[1]
    
        HR = le(person['HR']) if len(person['HR']) else ''
        LL = le(person['LL']) if len(person['LL']) else ''
    
        attributes = {'first_name' : person['first_name'],
                      'last_name'  : person['last_name'],
                      'HR'         : Json(HR),
                      'LL'         : Json(LL),
                      'email'      : person['email'],
                      'area_code'  : person['area_code'],
                      'phone'      : person['phone'],
                      'optin'      : bool(person['optin'])}
        
        dbc.query(config.FILL,attributes) #This is bad, should use psycopg2.cursor.executemany for table filling

