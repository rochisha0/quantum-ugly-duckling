from cloudant import Cloudant
import atexit
import os
import json

from cloudant.result import Result

db_name = 'mydb'
client = None
db = None

# IBM Cloudant Legacy authentication
client = Cloudant("username", "password", url="url")
client.connect()

my_database = client.create_database(db_name)

if my_database.exists():
    print(f"'{db_name}' successfully created.")

arrResult = Result(my_database.all_docs, include_docs=True)
sKorea = arrResult[0][0]['doc']['Korean']
print(sKorea)
# for item in arrResult:
#     print(f"{item.doc.korean}")




