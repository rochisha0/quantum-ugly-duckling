from cloudant import Cloudant
import atexit
import os
import json

from cloudant.result import Result

global CONFIG

db_name = 'mydb'
client = None
db = None

#import config file
with open('config.json', 'r') as f:
    getFile = json.load(f)
    global CONFIG
    CONFIG = getFile["services"]["cloudantNoSQLDB"][0]

#IBM Cloudant Legacy authentication
client = Cloudant(CONFIG["username"], CONFIG["password"], url=CONFIG["host"])
client.connect()

my_database = client.create_database(db_name)

if my_database.exists():
    print(f"'{db_name}' successfully created.")

arrResult = Result(my_database.all_docs, include_docs=True)
sText = arrResult[0]
print(sText)




